import os
import argparse
import subprocess
from datetime import datetime


def format_map_name():
    """
    Formats the output map name
    """
    dt_now = datetime.now()
    if os.name == "nt":
        map_name = dt_now.strftime("{}_%d-%m-%Y %I-%M-%S%p")
    else:
        map_name = dt_now.strftime("{}_%d-%m-%Y %I:%M:%S%p")
        
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


def usage():
    return """
    Geolocate IP Address(es) (with an interactive map)
    --------------------------------------------------
    ipmap map --ip <an_ip_or_a_file_containing_ip_addresses>
    
    Open Google Earth with the given coordinates
    --------------------------------------------
    ipmap earth --coordinates <latitude> <longitude>
         
    Lookup IP Address(es) (same as map but without an interactive map)
    ------------------------------------------------------------------
    ipmap lookup --ip <an_ip_or_a_file_containing_ip_addresses>
    
    
modes:
    map - creates an interactive map and pin points the locations of the specified ip address(es) on it.
    earth - opens google earth with the specified coordinates.
    lookup - looks up the specified ip address(es)' information.
    """


# Create parser
def create_parser():
    parser = argparse.ArgumentParser(description="IP.MAPPER — by Richard Mwewa (https://about.me/rly0nheart)",
                                     usage=usage())
    parser.add_argument("mode", help="init mode", choices=["earth", "lookup", "map", "maps"])
    parser.add_argument("-i", "--ip", help="an ip address or a file containing ip addresses")
    parser.add_argument("-o", "--output", help="map output name", default="ipmap")
    parser.add_argument("-c", "--coordinates", help="space separated latitude and longitude", nargs=2)
    return parser
