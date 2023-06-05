from ipmap.ipmap import *
from ipmap.config import format_map_name, create_parser
from ipmap.utils import path_finder, clear_screen, check_updates


# Parse command line arguments
parser = create_parser()
args = parser.parse_args()


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
        xprint(f"\n[{colour.YELLOW}!{colour.RESET}] User interruption detected.")
    except FileNotFoundError as file_not_found_error:
        xprint(f"[{colour.YELLOW}!{colour.RESET}] File Not Found: {colour.YELLOW}{file_not_found_error}{colour.RESET}")
    except Exception as error:
        xprint(f"[{colour.RESET}X{colour.RESET}] Error: {colour.RESET}{error}{colour.RESET}")

