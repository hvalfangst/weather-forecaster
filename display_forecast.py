import json
import matplotlib.pyplot as plt
from datetime import datetime


def plot_weather_data(json_response):
    # Parse the JSON response
    data = json.loads(json_response)

    # Extract the timeseries data
    timeseries = data["properties"]["timeseries"]

    # Extract datetime of last update
    updated_at = datetime.strptime(
        data["properties"]["meta"]["updated_at"], "%Y-%m-%dT%H:%M:%SZ")

    # Initialize lists to store the attributes
    timestamps = []
    air_temperatures = []
    cloud_coverages = []
    wind_speeds = []

    # Extract the attribute values for each timestamp
    for entry in timeseries:
        timestamp = datetime.strptime(entry["time"], "%Y-%m-%dT%H:%M:%SZ")
        timestamps.append(timestamp)
        details = entry["data"]["instant"]["details"]
        air_temperature = details["air_temperature"]
        cloud_coverage = details["cloud_area_fraction"]
        wind_speed = details["wind_speed"]
        air_temperatures.append(air_temperature)
        cloud_coverages.append(cloud_coverage)
        wind_speeds.append(wind_speed)

    # Plot the time series data
    plt.figure(figsize=(12, 6))

    # Upper left corner - Air temperature
    plt.subplot(2, 2, 1)
    plt.plot(timestamps, air_temperatures)
    plt.title("Air Temperature")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45, ha='right')
    plt.gca().xaxis.set_major_formatter(plt.FixedFormatter([t.strftime("%H:%M") for t in timestamps]))

    # Upper right corner - Cloud coverages
    plt.subplot(2, 2, 2)
    plt.plot(timestamps, cloud_coverages)
    plt.title("Cloud Coverage")
    plt.xlabel("Time")
    plt.ylabel("Cloud Coverage (%)")
    plt.xticks(rotation=45, ha='right')
    plt.gca().xaxis.set_major_formatter(plt.FixedFormatter([t.strftime("%H:%M") for t in timestamps]))

    # Lower left corner - Wind speeds
    plt.subplot(2, 2, 3)
    plt.plot(timestamps, wind_speeds)
    plt.title("Wind Speed")
    plt.xlabel("Time")
    plt.ylabel("Wind Speed (m/s)")
    plt.xticks(rotation=45, ha='right')
    plt.gca().xaxis.set_major_formatter(plt.FixedFormatter([t.strftime("%H:%M") for t in timestamps]))

    # Lower right corner - Location and date
    plt.subplot(2, 2, 4)
    plt.axis('off')  # Turn off axes
    plt.text(0.1, 0.5, f"Weather forecast for Oslo:\n\n{updated_at}", fontsize=20)

    plt.tight_layout()
    plt.show()


def main():
    # Read the JSON response from a file
    with open('forecasts/2023-06-16.json', 'r') as file:
        json_response = file.read()

    # Plot the weather data
    plot_weather_data(json_response)


if __name__ == '__main__':
    main()
