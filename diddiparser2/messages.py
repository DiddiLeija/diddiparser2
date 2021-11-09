"DiddiScript exception handler."

__all__ = ("run_error", "compile_error", "show_warning", "success_message")

from colorama import Fore


class error(Exception):
    pass


def run_error(msg):
    print(Fore.RED + "Error while running: " + msg)
    raise error("The execution failed.")


def compile_error(msg):
    print(Fore.RED + "Error while compiling: " + msg)
    raise error("Script compilation failed.")


def show_warning(msg):
    print(Fore.YELLOW + "WARNING: " + msg)


def success_message():
    print(Fore.CYAN + "The execution finished succesfully!")


def show_command(cmd):
    print(Fore.BLUE + f"-> {cmd}\n{'='*60}")
