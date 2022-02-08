"""
The DiddiScript edittor's theme formatter.

This configurations will affect the Text widget
from the editor. The text views (generated by
the idlelib) might not experiment changes.
"""

import json
from tkinter import messagebox

THEMES = {
    "Dark DiddiScript": {
        "description": "The default DiddiScript theme (dark)",
        "background": "black",
    },
    "Light DiddiScript": {
        "description": "The default DiddiScript theme (light)",
        "background": "white",
    },
}


def load_json_theme(file):
    """
    Load the themes from a JSON file.
    """
    if len(file) < 1:
        messagebox.showwarning("No such file selected", "The settings hasn't changed.")
    with open(file, "r") as f:
        data = json.loads(f.read())
    if isinstance(data, list):
        load_many(data)
    elif isinstance(data, dict):
        load_one(data)
    else:
        messagebox.showerror("Could not load from JSON", "Invalid format.")


def load_one(data):
    try:
        name = data["name"]
        description = data.get("description", "None")
        bg = data["background"]
        if not messagebox.askyesno(
            f"Load '{name}'?",
            f"Do you want to load the '{name}' theme? "
            "If another theme has the same name, it will be overwritten.",
        ):
            return None
        THEMES[name] = {"description": description, "background": bg}
    except KeyError:
        messagebox.showerror("Could not load theme", "Some keys are missing.")


def load_many(data):
    for d in data:
        load_one(d)


def format_themes():
    txt = ""
    if len(THEMES) < 1:
        return "(Nothing to show)"
    for k, v in THEMES.items():
        txt += f"{k}\n{'=' * 10}\n"
        txt += f"Description: {v['description']}\n"
        txt += f"Background color: '{v['background']}'\n"
        txt += "\n"
    return txt


def format_text(text_obj, selected_theme):
    try:
        if selected_theme not in THEMES.keys():
            raise Exception(
                f"The theme '{selected_theme}' is not registered."
                " If you are sure it is already registered, please report this as a bug."
            )
        theme_to_apply = THEMES[selected_theme]
        text_obj.config(background=theme_to_apply["background"])
    except Exception as exc:
        messagebox.showerror("Error while applying font", str(exc))
