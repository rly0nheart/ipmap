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
        if args:
            if args.earth:
                open_google_earth(get_ip_data(args.ip))
            if args.lookup:
                get_ip_data(args.ip)
            if args.map:
                generated_map = create_map(get_ip_data(args.ip), format_map_name(args.output))
                xprint(f"Opening map: {generated_map}")
                webbrowser.open(generated_map)
    except KeyboardInterrupt:
        xprint("\nUser interruption detected (Ctrl+C).")
    except Exception as e:
        xprint(f"Error: {e}")
