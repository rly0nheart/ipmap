import os
import requests
import subprocess
from rich import print as xprint
from ipmap.config import Version
from rich.markdown import Markdown


def send_request(endpoint) -> dict:
    """
    Sends a GET request to the specified endpoint and returns JSON
    :param endpoint: url endpoint to send request to
    :return: Dictionary response (JSON)
    """
    with requests.get(endpoint) as response:
        response_data = response.json()
    return response_data


# Check program updates
def check_updates():
    version = Version()
    release_data = send_request("https://api.github.com/repos/rly0nheart/ipmap/releases/latest")
    if release_data['tag_name'] != version.full_version():
        raw_release_notes = release_data['body']
        markdown_release_notes = Markdown(raw_release_notes)
        xprint(f"[UPDATE] A new release of ipmap is available ({release_data['tag_name']}).\n")
        xprint(markdown_release_notes)
    else:
        pass

        
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
