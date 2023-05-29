from ipmap import *
from utils import create_parser, clear_screen, format_map_name

# Parse command line arguments
parser = create_parser()
args = parser.parse_args()

if __name__ == "__main__":
    clear_screen()
    try:
        if args.mode == "earth":
            open_google_earth(args.coordinates)
        elif args.mode == "lookup":
            get_ip_data(args.ip)
        elif args.mode == "map":
            generated_map = create_map(get_ip_data(args.ip), os.path.join("maps", format_map_name.format(args.output)))
            webbrowser.open(generated_map)
    except KeyboardInterrupt:
        print("\n[[yellow]![/]] User interruption detected.")
    except Exception as err:
        print(f"[[red]X[/]] Error: [red]{err}[/]")
