import os
import subprocess
from rich import print as xprint
from urllib.request import urlopen
from rich.markdown import Markdown
from ipmap.config import json, Version
from urllib.error import HTTPError, URLError


def send_request(endpoint) -> dict:
    """
    Sends a GET request to the specified endpoint and returns JSON

    :param endpoint: url endpoint to send request to
    :return: Dictionary response (JSON)
    """
    try:
        with urlopen(endpoint) as response:
            response_data = json.loads(response.read().decode())
        return response_data
    except (URLError, HTTPError) as error:
        xprint(f"Error: {error}")


# Check program updates
def check_updates() -> None:
    """
    Checks for latest updates by retrieving the release tag from the releases page of the program from GitHub
    Then compares the remote version tag with the tag in the program.
    If they match, program assumes it's up to date.
    If not, print a message notifying the user about the remote version (which is treated as the official new release)
    , and lastly prints the release notes of the presumed new release.

    :return: None
    """
    version = Version()
    release_data = send_request("https://api.github.com/repos/rly0nheart/ipmap/releases/latest")
    if release_data['tag_name'] != version.full_version():
        raw_release_notes = release_data['body']
        markdown_release_notes = Markdown(raw_release_notes)
        xprint(f"* A new release of ipmap is available ({release_data['tag_name']}).\n")
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
    # Construct path to the user's home directory
    home_directory = os.path.expanduser("~")

    for directory in directories:
        # Construct and create each directory from the directories list if it doesn't already exist
        os.makedirs(os.path.join(home_directory, directory), exist_ok=True)


def clear_screen() -> None:
    """
    Clear the terminal screen/
    If Operating system is Windows, uses the 'cls' command. Otherwise, uses the 'clear' command

    :return: Uhh a cleared screen? haha
    """
    subprocess.call("cmd.exe /c cls" if os.name == "nt" else "clear")
