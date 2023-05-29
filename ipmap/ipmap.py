import os
import requests
import webbrowser
from rich import print
from rich.tree import Tree


def get_ip_data(ip_address: str) -> list:
    """
    Gets the geolocation information of a given IP Address.
    :param ip_address: IP Address to lookup
    :return: A list of lists containing an IP Address's data.
    The returned list is used in the leaflet map template to pin point the location(s)
    of an IP by using the coordinates.
    """
    # process input to get list of IPs
    ips = process_user_input(user_input=ip_address)
    # create an empty list to store results
    list_of_coordinates = []
    # iterate over each IP and make a request to ip-api.com
    for idx, ip in enumerate(ips, start=1):
        print(f"[[green]*[/]] Looking up IP {idx}: {ip}...")
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        ip_data = [response['org'],
                   response['as'],
                   response['isp'],
                   response['country'],
                   response['city'],
                   response['zip'],
                   response['regionName'],
                   response['timezone'],
                   response['lat'],
                   response['lon']]

        ip_data_tree = Tree("\n" + response['org'])
        for key, value in response.items():
            ip_data_tree.add(f"{key}: [green]{value}[/]")

        print(ip_data_tree)
        # extract the latitude, longitude and organization data from the response and append to the list_of_tuples
        list_of_coordinates.append(ip_data)

    # return the list_of_tuples
    return list_of_coordinates


def process_user_input(user_input: str) -> list:
    """
    Processes input from user to determine the type, and how to return the results
    :param user_input: IP; could be a single IP or a text file containing IP Addresses
    :return: A list of IP Addresses
    """
    if os.path.isfile(user_input):
        # if user_input is a file, read the contents of the file and return a list of IP addresses
        with open(user_input, 'r') as file:
            print(f"[[green]+[/]]Loaded IP Addresses from file: {file.name}")
            ips = file.readlines()
            ips = [ip.strip() for ip in ips]  # remove any whitespace characters from each IP address
            return ips
    else:
        return [user_input]


def create_map(coordinates: list, output_file: str, template: str = "template/map.html") -> str:
    """
    Uses the map template to create a new map with the geolocation data returned from the get_ip_data function
    :param coordinates: List of lists containing the geolocation data of each IP Address
    :param output_file: Output filename of the generated map
    :param template: The map template to use, default is template/map.html
    :return: An interactive map in default browser (with pins pointing on the areas that correspond the IPs coordinates)
    """
    with open(template, "r") as html_file:
        html_content = html_file.read()

    updated_html_content = html_content.format(output_file, coordinates)

    with open(f"{output_file}.html", "w") as created_map:
        created_map.write(updated_html_content)

    return created_map.name


def open_google_earth(coordinates: list) -> None:
    """
    Opens Google Earth with the specified coordinates.
    :param coordinates: A list of two item; latitude and longitude
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
    latitude, longitude = coordinates
    google_earth_url += f"@{latitude},{longitude}," \
                        f"89.06331136a,12094.0505788d,1y,1.97597436h,60t,-0r/data=KAI"

    # Open the URL in the default web browser
    print(f"[[green]*[/]] Opening Google Earth on: {coordinates}...")
    webbrowser.open(google_earth_url)
