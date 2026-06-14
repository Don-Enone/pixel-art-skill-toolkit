from __future__ import annotations

import json
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, simpledialog, ttk
from tkinter.scrolledtext import ScrolledText
from typing import Any

from PIL import ImageTk

from .format import default_document, pretty_json
from .renderer import load_document, render_document, save_png


class JsonDialog(simpledialog.Dialog):
    def __init__(self, parent: tk.Misc, title: str, initial: Any):
        self.initial = json.dumps(initial, indent=2, ensure_ascii=False)
        self.result: Any = None
        super().__init__(parent, title)

    def body(self, master: tk.Misc) -> tk.Widget:
        self.text = ScrolledText(master, width=54, height=14, wrap="none", undo=True)
        self.text.insert("1.0", self.initial)
        self.text.grid(row=0, column=0, sticky="nsew")
        return self.text

    def validate(self) -> bool:
        try:
            self.result = json.loads(self.text.get("1.0", "end"))
        except json.JSONDecodeError as exc:
            messagebox.showerror("Invalid JSON", str(exc), parent=self)
            return False
        return True


class PixelArtEditor:
    def __init__(self, root: tk.Tk, input_path: Path | None = None):
        self.root = root
        self.root.title("Pixel Art Skill Toolkit")
        self.current_path: Path | None = None
        self.document: dict[str, Any] = default_document()
        self.preview_photo: ImageTk.PhotoImage | None = None
        self.preview_scale = tk.IntVar(value=12)

        self._build_menu()
        self._build_layout()
        if input_path:
            self.open_path(input_path)
        else:
            self.set_document(self.document)

    def _build_menu(self) -> None:
        menu = tk.Menu(self.root)
        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label="New", command=self.new_document)
        file_menu.add_command(label="Open...", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Export PNG...", command=self.export_png)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.destroy)
        menu.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu)

    def _build_layout(self) -> None:
        paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)

        json_frame = ttk.Frame(paned, padding=8)
        ttk.Label(json_frame, text="Pixel Art JSON").pack(anchor="w")
        self.json_text = ScrolledText(json_frame, width=58, wrap="none", undo=True)
        self.json_text.pack(fill=tk.BOTH, expand=True, pady=(6, 6))
        json_buttons = ttk.Frame(json_frame)
        json_buttons.pack(fill=tk.X)
        ttk.Button(json_buttons, text="Apply JSON", command=self.apply_json).pack(side=tk.LEFT)
        ttk.Button(json_buttons, text="Format", command=self.format_json).pack(side=tk.LEFT, padx=(6, 0))
        paned.add(json_frame, weight=3)

        right = ttk.Frame(paned, padding=8)
        preview_bar = ttk.Frame(right)
        preview_bar.pack(fill=tk.X)
        ttk.Label(preview_bar, text="Scale").pack(side=tk.LEFT)
        ttk.Spinbox(
            preview_bar,
            from_=1,
            to=64,
            textvariable=self.preview_scale,
            width=5,
            command=self.render_preview,
        ).pack(side=tk.LEFT, padx=(6, 10))
        ttk.Button(preview_bar, text="Render", command=self.render_preview).pack(side=tk.LEFT)

        self.preview_label = ttk.Label(right, anchor="center")
        self.preview_label.pack(fill=tk.BOTH, expand=True, pady=(8, 8))

        notebook = ttk.Notebook(right)
        notebook.pack(fill=tk.BOTH, expand=False)
        notebook.add(self._build_palette_tab(notebook), text="Palette")
        notebook.add(self._build_operations_tab(notebook), text="Operations")
        paned.add(right, weight=2)

    def _build_palette_tab(self, parent: ttk.Notebook) -> ttk.Frame:
        frame = ttk.Frame(parent, padding=6)
        self.palette_tree = ttk.Treeview(frame, columns=("name", "value"), show="headings", height=7)
        self.palette_tree.heading("name", text="Name")
        self.palette_tree.heading("value", text="Color")
        self.palette_tree.column("name", width=120)
        self.palette_tree.column("value", width=140)
        self.palette_tree.pack(fill=tk.BOTH, expand=True)

        buttons = ttk.Frame(frame)
        buttons.pack(fill=tk.X, pady=(6, 0))
        ttk.Button(buttons, text="Add", command=self.add_palette_color).pack(side=tk.LEFT)
        ttk.Button(buttons, text="Edit", command=self.edit_palette_color).pack(side=tk.LEFT, padx=(6, 0))
        ttk.Button(buttons, text="Delete", command=self.delete_palette_color).pack(side=tk.LEFT, padx=(6, 0))
        return frame

    def _build_operations_tab(self, parent: ttk.Notebook) -> ttk.Frame:
        frame = ttk.Frame(parent, padding=6)
        self.operations_tree = ttk.Treeview(
            frame,
            columns=("layer", "index", "op"),
            show="headings",
            height=7,
        )
        self.operations_tree.heading("layer", text="Layer")
        self.operations_tree.heading("index", text="#")
        self.operations_tree.heading("op", text="Operation")
        self.operations_tree.column("layer", width=120)
        self.operations_tree.column("index", width=40)
        self.operations_tree.column("op", width=120)
        self.operations_tree.pack(fill=tk.BOTH, expand=True)

        buttons = ttk.Frame(frame)
        buttons.pack(fill=tk.X, pady=(6, 0))
        ttk.Button(buttons, text="Add", command=self.add_operation).pack(side=tk.LEFT)
        ttk.Button(buttons, text="Edit", command=self.edit_operation).pack(side=tk.LEFT, padx=(6, 0))
        ttk.Button(buttons, text="Delete", command=self.delete_operation).pack(side=tk.LEFT, padx=(6, 0))
        return frame

    def new_document(self) -> None:
        self.current_path = None
        self.set_document(default_document())

    def open_file(self) -> None:
        path = filedialog.askopenfilename(
            title="Open Pixel Art JSON",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if path:
            self.open_path(Path(path))

    def open_path(self, path: Path) -> None:
        try:
            self.document = load_document(path)
        except Exception as exc:
            messagebox.showerror("Open failed", str(exc), parent=self.root)
            return
        self.current_path = path
        self.set_document(self.document)

    def save_file(self) -> None:
        if self.current_path is None:
            self.save_file_as()
            return
        if not self.apply_json(show_success=False):
            return
        self.current_path.write_text(pretty_json(self.document), encoding="utf-8")

    def save_file_as(self) -> None:
        path = filedialog.asksaveasfilename(
            title="Save Pixel Art JSON",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if not path:
            return
        self.current_path = Path(path)
        self.save_file()

    def export_png(self) -> None:
        if not self.apply_json(show_success=False):
            return
        path = filedialog.asksaveasfilename(
            title="Export PNG",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        )
        if not path:
            return
        try:
            save_png(self.document, path, scale=self.preview_scale.get())
        except Exception as exc:
            messagebox.showerror("Export failed", str(exc), parent=self.root)

    def set_document(self, document: dict[str, Any]) -> None:
        self.document = document
        self.json_text.delete("1.0", "end")
        self.json_text.insert("1.0", pretty_json(document))
        self.refresh_lists()
        self.render_preview()

    def apply_json(self, show_success: bool = True) -> bool:
        try:
            document = json.loads(self.json_text.get("1.0", "end"))
            render_document(document)
        except Exception as exc:
            messagebox.showerror("Invalid document", str(exc), parent=self.root)
            return False
        self.document = document
        self.refresh_lists()
        self.render_preview()
        if show_success:
            self.root.bell()
        return True

    def format_json(self) -> None:
        if self.apply_json(show_success=False):
            self.json_text.delete("1.0", "end")
            self.json_text.insert("1.0", pretty_json(self.document))

    def render_preview(self) -> None:
        try:
            scale = self.preview_scale.get()
            image = render_document(self.document, scale=scale)
            self.preview_photo = ImageTk.PhotoImage(image)
            self.preview_label.configure(image=self.preview_photo, text="")
        except Exception as exc:
            self.preview_photo = None
            self.preview_label.configure(image="", text=str(exc))

    def refresh_lists(self) -> None:
        for item in self.palette_tree.get_children():
            self.palette_tree.delete(item)
        palette = self.document.get("palette", {})
        if isinstance(palette, dict):
            for name, value in palette.items():
                self.palette_tree.insert("", "end", iid=name, values=(name, value))

        for item in self.operations_tree.get_children():
            self.operations_tree.delete(item)
        for entry in self._operation_entries():
            iid, layer_name, index, op_name = entry
            self.operations_tree.insert("", "end", iid=iid, values=(layer_name, index, op_name))

    def add_palette_color(self) -> None:
        if not self.apply_json(show_success=False):
            return
        name = simpledialog.askstring("Add color", "Palette name:", parent=self.root)
        if not name:
            return
        value = simpledialog.askstring("Add color", "Color value (#RRGGBB or #RRGGBBAA):", parent=self.root)
        if not value:
            return
        self.document.setdefault("palette", {})[name] = value
        self.set_document(self.document)

    def edit_palette_color(self) -> None:
        if not self.apply_json(show_success=False):
            return
        selection = self.palette_tree.selection()
        if not selection:
            return
        name = selection[0]
        palette = self.document.setdefault("palette", {})
        value = simpledialog.askstring(
            "Edit color",
            f"Color value for {name}:",
            initialvalue=str(palette.get(name, "")),
            parent=self.root,
        )
        if value:
            palette[name] = value
            self.set_document(self.document)

    def delete_palette_color(self) -> None:
        if not self.apply_json(show_success=False):
            return
        selection = self.palette_tree.selection()
        if not selection:
            return
        name = selection[0]
        if messagebox.askyesno("Delete color", f"Delete palette color {name}?", parent=self.root):
            self.document.get("palette", {}).pop(name, None)
            self.set_document(self.document)

    def add_operation(self) -> None:
        if not self.apply_json(show_success=False):
            return
        palette = self.document.get("palette", {})
        template = {
            "op": "rect",
            "color": next(iter(palette), "color"),
            "x": 0,
            "y": 0,
            "w": 4,
            "h": 4,
        }
        dialog = JsonDialog(self.root, "Add operation", template)
        if dialog.result is None:
            return
        container = self._default_operation_container()
        container.append(dialog.result)
        self.set_document(self.document)

    def edit_operation(self) -> None:
        if not self.apply_json(show_success=False):
            return
        selected = self.operations_tree.selection()
        if not selected:
            return
        container, index = self._operation_container_for_iid(selected[0])
        dialog = JsonDialog(self.root, "Edit operation", container[index])
        if dialog.result is None:
            return
        container[index] = dialog.result
        self.set_document(self.document)

    def delete_operation(self) -> None:
        if not self.apply_json(show_success=False):
            return
        selected = self.operations_tree.selection()
        if not selected:
            return
        container, index = self._operation_container_for_iid(selected[0])
        if messagebox.askyesno("Delete operation", "Delete selected operation?", parent=self.root):
            del container[index]
            self.set_document(self.document)

    def _operation_entries(self) -> list[tuple[str, str, int, str]]:
        entries: list[tuple[str, str, int, str]] = []
        layers = self.document.get("layers")
        if isinstance(layers, list):
            for layer_index, layer in enumerate(layers):
                if not isinstance(layer, dict):
                    continue
                layer_name = str(layer.get("name", f"Layer {layer_index + 1}"))
                operations = layer.get("operations", [])
                if not isinstance(operations, list):
                    continue
                for op_index, operation in enumerate(operations):
                    op_name = operation.get("op", "?") if isinstance(operation, dict) else "?"
                    entries.append((f"layer:{layer_index}:{op_index}", layer_name, op_index, str(op_name)))
        else:
            operations = self.document.get("operations", [])
            if isinstance(operations, list):
                for op_index, operation in enumerate(operations):
                    op_name = operation.get("op", "?") if isinstance(operation, dict) else "?"
                    entries.append((f"top:{op_index}", "operations", op_index, str(op_name)))
        return entries

    def _default_operation_container(self) -> list[Any]:
        layers = self.document.get("layers")
        if isinstance(layers, list):
            if not layers:
                layers.append({"name": "Layer 1", "operations": []})
            layer = layers[0]
            if not isinstance(layer, dict):
                layers[0] = {"name": "Layer 1", "operations": []}
                layer = layers[0]
            operations = layer.setdefault("operations", [])
            if not isinstance(operations, list):
                layer["operations"] = []
                operations = layer["operations"]
            return operations
        operations = self.document.setdefault("operations", [])
        if not isinstance(operations, list):
            self.document["operations"] = []
            operations = self.document["operations"]
        return operations

    def _operation_container_for_iid(self, iid: str) -> tuple[list[Any], int]:
        if iid.startswith("layer:"):
            _, layer_index_text, op_index_text = iid.split(":")
            layer = self.document["layers"][int(layer_index_text)]
            return layer["operations"], int(op_index_text)
        if iid.startswith("top:"):
            _, op_index_text = iid.split(":")
            return self.document["operations"], int(op_index_text)
        raise ValueError(f"Unknown operation id: {iid}")


def main(input_path: str | Path | None = None) -> None:
    root = tk.Tk()
    path = Path(input_path) if input_path else None
    PixelArtEditor(root, path)
    root.mainloop()


if __name__ == "__main__":
    main()
