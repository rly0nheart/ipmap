import os
import json
import argparse
from rich.table import Table
from datetime import datetime


class Version:
    def __init__(self):
        self.major = settings()["program"]["version"]["major"]
        self.minor = settings()["program"]["version"]["minor"]
        self.patch = settings()["program"]["version"]["patch"]
        self.suffix = settings()["program"]["version"]["suffix"]

    def full_version(self) -> str:
        """
        Returns the full version string composed of the version components.

        :return: The complete version string in the format "major.minor.patchsuffix".
        """
        return f"{self.major}.{self.minor}.{self.patch}{self.suffix}"


def settings() -> dict:
    """
    Loads the program's settings from /data/settings.json

    :return: Dictionary (JSON) containing program settings
    """
    # Get the absolute path of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the settings.json file
    settings_path = os.path.join(current_dir, "data", "settings.json")

    # Load the settings from the file
    with open(settings_path) as file:
        data = json.load(file)

    return data


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


def usage():
    return """
    Geolocate IP Address(es) (with an interactive map)
    --------------------------------------------------
    ipmap <ip> --map

    Open Google Earth on the given coordinates
    --------------------------------------------
    ipmap <ip> --earth

    Lookup IP Address(es) (same as map but without an interactive map)
    ------------------------------------------------------------------
    ipmap <ip> --lookup
    """


def create_parser():
    parser = argparse.ArgumentParser(description=f"{settings()['program']['name']}" 
                                                 f" — by {settings()['program']['developer']['name']}" 
                                                 f" ({settings()['program']['developer']['about']})",
                                     epilog=settings()['program']['about'], usage=usage())
    parser.add_argument("ip", help="target ip address")
    parser.add_argument("-e", "--earth", help="Open Google Earth on the location of a given ip", action="store_true")
    parser.add_argument("-l", "--lookup", help="Lookup an ip (like --map, but without an interactive map)",
                        action="store_true")
    parser.add_argument("-m", "--map", help="Geolocate an ip (with an interactive map)", action="store_true")
    parser.add_argument("-o", "--output", help="map output name (default %(default)s)", default="ipmap")
    parser.add_argument("-v", "--version", action="version", version=Version().full_version())
    return parser
