import os

from plotter import plot_weather_data


def choose_file(files):
    """
   Filters a list of files to include only JSON files and prompts the user
   to choose one. If no JSON files are found, the function returns `None`.

   Args:
       files (list): A list of file names (strings) in the specified directory.

   Returns:
       str or None: The file name of the chosen JSON file, or None if no files
       are found or if the user makes no valid selection.
   """
    # Filter to include only JSON files
    json_files = [file for file in files if file.endswith('.json')]

    if not json_files:
        print("No JSON forecast files found.")
        return None  # Or raise an exception if you prefer

    print("Available forecast files:")
    for i, file in enumerate(json_files):
        print(f"{i + 1}. {file}")

    while True:
        choice = input("Choose a file number: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(json_files):
                return json_files[choice - 1]
            else:
                print("Invalid choice. Please enter a valid file number.")
        except ValueError:
            print("Invalid choice. Please enter a valid file number.")


def main():
    """
   Main function that lists available forecast files in the "forecasts" directory
   and prompts the user to choose one. Once a file is chosen, it plots the weather
   data by calling the `plot_weather_data` function.

   Returns:
       None: The function terminates if no files are found or when the weather plot
       has been generated and saved.
   """
    # List forecast files in the "forecasts" folder
    folder_path = "forecasts"
    files = os.listdir(folder_path)

    if len(files) == 0:
        print("No forecast files found.")
        return

    # Prompt the user to choose a file
    chosen_file = choose_file(files)
    file_path = os.path.join(folder_path, chosen_file)

    # Plot the weather data
    plot_weather_data(file_path)


if __name__ == '__main__':
    main()
