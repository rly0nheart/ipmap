import os
import subprocess
from rich.table import Table
from datetime import datetime


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
