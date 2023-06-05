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

        Returns:
            str: The complete version string in the format "major.minor.patch.suffix".
        """
        return f"{self.major}.{self.minor}.{self.patch}{self.suffix}"


class Colours:
    def __init__(self):
        self.RED = self.get_colour("RED")
        self.WHITE = self.get_colour("WHITE")
        self.GREEN = self.get_colour("GREEN")
        self.YELLOW = self.get_colour("YELLOW")
        self.RESET = self.get_colour("RESET")

    @staticmethod
    def get_colour(colour_name: str) -> str:
        """
        Retrieves the value of the specified colour from the settings.

        :param: colour_name (str): The name of the colour to retrieve.

        :return: The value of the specified colour.
        """
        return settings()["colours"][colour_name]


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
    ipmap map --ip <ip/file_containing_ip_addresses>

    Open Google Earth on the given coordinates
    --------------------------------------------
    ipmap earth --coordinates <latitude> <longitude>

    Lookup IP Address(es) (same as map but without an interactive map)
    ------------------------------------------------------------------
    ipmap lookup --ip <ip/file_containing_ip_addresses>


modes:
    map - creates an interactive map and pin points the locations of the specified ip address(es) on it.
    earth - opens google earth on the specified coordinates
    lookup - looks up the specified ip address(es)' information.
    """


def create_parser():
    parser = argparse.ArgumentParser(description=f"{settings()['program']['name']}" 
                                                 f" — by {settings()['program']['developer']['name']}" 
                                                 f" ({settings()['program']['developer']['about']})",
                                     epilog=settings()['program']['about'], usage=usage())
    parser.add_argument("mode", help="init mode", choices=["earth", "lookup", "map"])
    parser.add_argument("-i", "--ip", help="an ip address or a file containing ip addresses")
    parser.add_argument("-o", "--output", help="map output name", default="ipmap")
    parser.add_argument("-c", "--coordinates", help="space separated latitude and longitude", nargs=2)
    parser.add_argument("-v", "--version", action="version", version=Version().full_version())
    return parser
