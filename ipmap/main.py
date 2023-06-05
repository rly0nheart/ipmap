import time
from ipmap.ipmap import *
from ipmap.utils import path_finder, clear_screen, check_updates
from ipmap.config import format_map_name, create_parser, settings, Version


# Parse command line arguments
parser = create_parser()
args = parser.parse_args()


def run():
    clear_screen()
    xprint(f"Starting {settings()['program']['name']} v{Version().full_version()} at {time.asctime()}")
    path_finder(["maps"])
    check_updates()
    try:
        if args.mode == "earth":
            open_google_earth(args.coordinates)
        elif args.mode == "lookup":
            get_ip_data(args.ip)
        elif args.mode == "map":
            generated_map = create_map(get_ip_data(args.ip), os.path.join("maps", format_map_name(args.output)))
            xprint(f"Opening map: {generated_map}")
            webbrowser.open(generated_map)
    except KeyboardInterrupt:
        xprint(f"\nUser interruption detected ({colour.YELLOW}Ctrl+C{colour.RESET}).")
    except FileNotFoundError as file_not_found_error:
        xprint(f"File Not Found: {colour.YELLOW}{file_not_found_error}{colour.RESET}")
    except Exception as error:
        xprint(f"Error: {colour.RESET}{error}{colour.RESET}")

