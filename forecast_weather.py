import requests
import os
from datetime import datetime

# Assign variables derived from GitHub Secrets
API_URL = os.environ.get("WEATHER_FORECAST_API_URL")
USER_AGENT = os.environ.get("USER_AGENT")


def call_api_and_save_json(api_url):

    # Get the current date
    current_date = datetime.now().date()

    # Create the file name based on the current date
    file_name = f"forecasts/{current_date}.json"

    # Check if the file already exists
    try:
        with open(file_name, "r"):
            # File already exists, do not overwrite
            print("File already exists.")
            return
    except FileNotFoundError:
        pass

    # Make the API call with the User Agent header
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
        exit_code = 0
    else:
        print("API call failed.")
        print(response.status_code)
        exit_code = 1
    exit(exit_code)


def main():
    # Call the API and save the JSON response as a file
    call_api_and_save_json(API_URL)


if __name__ == '__main__':
    main()
