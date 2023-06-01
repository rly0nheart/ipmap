import os
import subprocess
from datetime import datetime


def format_map_name(defined_name) -> str:
    """
    Formats the output map name
    :param defined_name: user-defined map name
    :return: formatted map name
    """
    dt_now = datetime.now()
    if os.name == "nt":
        map_name = dt_now.strftime(f"{defined_name}_%d-%m-%Y %I-%M-%S%p")
    else:
        map_name = dt_now.strftime(f"{defined_name}_%d-%m-%Y %I:%M:%S%p")
        
    return map_name

        
def path_finder(directories: list) -> None:
    """
    Checks if the specified directories exist.
    If not, it creates them.
    :param directories: List of directories to check and create
    :return: None
    """
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def clear_screen() -> None:
    """
    Clear the terminal screen/
    If Operating system is Windows, uses the 'cls' command. Otherwise, uses the 'clear' command
    :return: None
    """
    subprocess.call("cmd.exe /c cls" if os.name == "nt" else "clear")
