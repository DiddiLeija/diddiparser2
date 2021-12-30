import tkinter


def generate_menu(root, options):
    """
    Generate a menu from a Tk window and
    a list of dictionaries with options.
    """
    main_menu = tkinter.Menu(root)
    for name, option in options.values():
        child_menu = tkinter.Menu(main_menu, tearoff=0)
        for label, command in option.values():
            child_menu.add_command(label=label, command=command)
        main_menu.add_cascade(label=name, menu=child_menu)
    root.config(menu=main_menu)
