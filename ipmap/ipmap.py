import os
import webbrowser
from rich import print as xprint
from ipmap.utils import send_request
from ipmap.config import create_ip_table


def get_ip_data(ip_address: str) -> list:
    """
    Gets the geolocation information of given IP Addresses.

    :param ip_address: IP Addresses to look up
    :return: A list of lists containing IP Addresses' data.

    The returned list is used in the leaflet map template to pinpoint the location(s)
    of IPs by using the coordinates.
    """
    # process input to get list of IPs
    ips = process_user_input(user_input=ip_address)

    # create an empty list to store ip data that will be used in the map
    ip_data_for_map = []

    # iterate over each IP and make a request to ip-api.com
    for idx, ip in enumerate(ips, start=1):
        xprint(f"{idx} Looking up: {ip}...", end="\r")
        response = send_request(f"http://ip-api.com/json/{ip}")
        ip_data = [
            response['query'],
            response['org'],
            response['as'],
            response['isp'],
            response['country'],
            response['city'],
            response['zip'],
            response['regionName'],
            response['timezone'],
            str(response['lat']),
            str(response['lon'])
        ]

        # get the selected ip data from the response and append it to the ip_data_for_map list
        ip_data_for_map.append(ip_data)

    # create the IP geolocation data table
    # the table gets displayed on the terminal
    table = create_ip_table(title=f"\nIP Geolocation Data: {ip_address}", ip_data=ip_data_for_map)
    xprint(table)

    # return a list of lists containing ip data
    # this returned list will be used in the map template
    return ip_data_for_map


def process_user_input(user_input: str) -> list:
    """
    Processes input from user to determine the type, and how to return the results

    :param user_input: IP; could be a single IP or a text file containing IP Addresses
    :return: A list of IP Addresses
    """
    if os.path.isfile(user_input):
        # if user_input is a file, read the contents of the file and return a list of IP addresses
        with open(user_input, 'r') as file:
            xprint(f"Loaded IP Addresses: '{file.name}'")
            ips = file.readlines()
            ips = [ip.strip() for ip in ips]  # remove any whitespace characters from each IP address
            return ips
    else:
        return [user_input]


def create_map(coordinates: list, output_file: str) -> str:
    """
    Uses the map template to create a new map with the geolocation data returned from the get_ip_data function

    :param coordinates: List of lists containing the geolocation data of each IP Address
    :param output_file: Output filename of the generated map
    :return: An interactive map in default browser (with pins pointing on the areas that correspond the IPs coordinates)
    """
    # Construct path to the user's home directory
    home_directory = os.path.expanduser("~")

    # Get the absolute path of the current file
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the maps directory
    maps_directory = os.path.join(home_directory, "maps")

    # Construct the path to the map template
    html_path = os.path.join(current_directory, "data", "templates", "map.html")
    with open(html_path, "r") as html_file:
        html_content = html_file.read()

    updated_html_content = html_content.format(output_file, coordinates)

    with open(os.path.join(maps_directory, f"{output_file}.html"), "w") as created_map:
        created_map.write(updated_html_content)

    return created_map.name


def open_google_earth(ip_data: list) -> None:
    """
    Opens Google Earth with the specified coordinates.

    :param ip_data: A list of lists from get_ip_data containing data of an ip
    :return: None
    """
    # Construct the URL with the coordinates
    google_earth_url = "https://earth.google.com/web/"
    """
    I honestly don't know what the below units are, 
    but I do know that 'data=KAI' makes the view tilt in a almost 360 view of the location.

    - 89.06331136a
    - 12094.0505788d
    - 1y
    - 1.97597436h
    - 60t
    - -0r
    - /data=KAI
    """

    for data in ip_data:
        latitude = data[9]
        longitude = data[10]
        google_earth_url += f"@{latitude},{longitude}," \
                            f"89.06331136a,12094.0505788d,1y,1.97597436h,60t,-0r/data=KAI"

        # Open the URL in the default web browser
        xprint(f"({latitude}, {longitude}) Opening Google Earth...")
        webbrowser.open(google_earth_url)
