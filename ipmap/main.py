import argparse
from ipmap.ipmap import *
from ipmap.utils import path_finder, clear_screen, format_map_name, check_updates


def usage():
    return """
    Geolocate IP Address(es) (with an interactive map)
    --------------------------------------------------
    ipmap map --ip <ip/file_containing_ip_addresses>

    Open Google Earth with the given coordinates
    --------------------------------------------
    ipmap earth --coordinates <latitude> <longitude>

    Lookup IP Address(es) (same as map but without an interactive map)
    ------------------------------------------------------------------
    ipmap lookup --ip <ip/file_containing_ip_addresses>


modes:
    map - creates an interactive map and pin points the locations of the specified ip address(es) on it.
    earth - opens google earth with the specified coordinates.
    lookup - looks up the specified ip address(es)' information.
    """


def create_parser():
    parser = argparse.ArgumentParser(description="IP.MAPPER — by Richard Mwewa (https://about.me/rly0nheart)",
                                      usage=usage())
    parser.add_argument("mode", help="init mode", choices=["earth", "lookup", "map", "maps"])
    parser.add_argument("-i", "--ip", help="an ip address or a file containing ip addresses")
    parser.add_argument("-o", "--output", help="map output name", default="ipmap")
    parser.add_argument("-c", "--coordinates", help="space separated latitude and longitude", nargs=2)
    return parser


def run():
    path_finder(["maps"])
    clear_screen()
    check_updates()
    try:
        if args.mode == "earth":
            open_google_earth(args.coordinates)
        elif args.mode == "lookup":
            get_ip_data(args.ip)
        elif args.mode == "map":
            ip_coordinates = get_ip_data(args.ip)
            generated_map = create_map(ip_coordinates, os.path.join("maps", format_map_name(args.output)))
            webbrowser.open(generated_map)
    except KeyboardInterrupt:
        xprint("\n[[yellow]![/]] User interruption detected.")
    #except Exception as err:
        #xprint(f"[[red]X[/]] Error: [red]{err}[/]")


# Parse command line arguments
parser = create_parser()
args = parser.parse_args()
