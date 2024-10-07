import os

import requests
from datetime import datetime

# Assign variables derived from GitHub Secrets
from plotter import plot_weather_data

API_URL = os.environ.get("WEATHER_FORECAST_API_URL")
USER_AGENT = os.environ.get("USER_AGENT")


def call_api_and_save_json(api_url):
    """
    Makes an API call to the specified URL, retrieves the JSON response,
    and saves it to a file named based on the current date. If the file
    for the current date already exists, the function returns without making
    the API call.

    Args:
        api_url (str): The URL of the API to fetch the data from.

    Returns:
        str: The file path where the JSON response is saved, or the existing file path if the file already exists.

    Raises:
        SystemExit: If the API call fails (i.e., returns a status code other than 200),
                    the program exits with an error status after printing the error code.
    """

    # Get the current date
    current_date = datetime.now().date()

    # Create the file name based on the current date
    file_name = f"forecasts/{current_date}.json"

    # Check if the file already exists
    try:
        with open(file_name, "r"):
            print("File already exists.")
            return file_name
    except FileNotFoundError:
        pass

    # Make the API call with the User-Agent header
    headers = {
        "User-Agent": USER_AGENT
    }
    response = requests.get(api_url, headers=headers)

    # Check if the API call was successful
    if response.status_code == 200:
        # Save the JSON response to a file
        with open(file_name, "w") as file:
            file.write(response.text)
        print("JSON file saved successfully.")
        return file_name
    else:
        print("API call failed.")
        print(f"Status Code: {response.status_code}")
        exit(1)


def main():
    # Call the API and save the JSON response as a file
    json_file_path = call_api_and_save_json(API_URL)

    # If a JSON file was saved, plot the weather data based on file path
    if json_file_path:
        plot_weather_data(json_file_path)


if __name__ == '__main__':
    main()
