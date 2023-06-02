import os
import requests
import subprocess
from rich.table import Table
from datetime import datetime
from rich import print as xprint
from rich.markdown import Markdown
from ipmap.version import __version__


def __send_request(endpoint) -> dict:
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
    release_data = __send_request("https://api.github.com/repos/rly0nheart/ipmap/releases/latest")
    if release_data['tag_name'] != __version__:
        raw_release_notes = release_data['body']
        markdown_release_notes = Markdown(raw_release_notes)
        xprint(f"[UPDATE] A new release of ipmap is available ({release_data['tag_name']}).\n")
        xprint(markdown_release_notes)
    else:
        pass

        
def create_ip_table(title: str, ip_data: list) -> Table:
    """
    Creates a table with the IP geolocation data.
    :param title: Table title
    :param ip_data: List of lists containing the geolocation data of IP Addresses
    :return: Table object containing the IP geolocation data
    """
    column_headers = [
        "IP",
        "Organization",
        "AS",
        "ISP",
        "Country",
        "City",
        "ZIP",
        "Region",
        "Timezone",
        "Latitude",
        "Longitude"
    ]

    table = Table(title=title, header_style="bold white")
    for header in column_headers:
        table.add_column(header)

    for ip_info in ip_data:
        table.add_row(*ip_info)

    return table


def format_map_name(defined_name) -> str:
    """
    Formats the output map name
    :param defined_name: User-defined name for the map
    :return: Formatted/Reconstructed name of the map
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
