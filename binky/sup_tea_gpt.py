#!/usr/bin/python3

import time, re, os
import numpy as np

def clear_screen():
        # Clear the screen based on the operating system
        os.system('cls' if os.name == 'nt' else 'clear')

def read_config_file(filename):
        config = {}
        with open(filename, 'r') as file:
                for line in file:
                        identifier, type_name, description, volume, brew_indicator, brew_times = line.strip().split(';')
                        config[identifier] = {
                                'type': type_name,
                                'description': description,
                                'volume': float(volume),
                                'brew_indicator': brew_indicator.lower() == 'true',
                                'brew_times': list(map(int, brew_times.split(','))) if brew_indicator.lower() == 'true' else None
                        }
        return config

def read_drug_conf(drug_file):
        drug_conf = {}
        with open(drug_file, 'r') as file:
                for line in file:
                        (identifier, type, name) = line.strip().split(';')
                        config[identifier] = {
                                'type': type_name,
                                'description': description,
                                'volume': float(volume),
                                'brew_indicator': brew_indicator.lower() == 'true',
                                'brew_times': list(map(int, brew_times.split(','))) if brew_indicator.lower() == 'true' else None
                        }
        return drug_conf

def display_menu(config):
        clear_screen()
        print("Menu:")
        for identifier, drink in config.items():
                print(f"{identifier}: {drink['type']} - {drink['description']}")
        print("\nl: Log Drugs!!!!")
        print("\ns: Daily Summary")
        print("x: Exit\n")

def log_drugs(drug_file):
        drug_conf = {}
        print("Fuck yeah let's do some drugs!!!!")
        quit()
        #with open()

def get_selected_drink(config):
        while True:
                display_menu(config)
                selection = input("Select a drink (enter the unique identifier) or 'x' to exit: ")
                if re.match('^[Xx]$', selection):
                        return None
                elif re.match('^[Ss]$', selection):
                        return 's'
                elif re.match('^[Ll]$', selection):
                        log_drugs()
                        break  #that fucking did nothing.
                elif selection in config:
                        return selection
                else:
                        print("Invalid selection. Please try again.")

def get_brew_time(config, drink_id):
        drink = config[drink_id]
        if not drink['brew_indicator']:
                return None

        if drink['brew_times']:
                print(f"Available brew times for {drink['type']} - {drink['description']}: {drink['brew_times']} minutes")
                while True:
                        brew_time_input = input("Select a brew time (in minutes) or press Enter for the default value: ")
                        if brew_time_input.strip() == '':
                                return drink['brew_times'][0]
                        try:
                                brew_time = int(brew_time_input)
                                if brew_time in drink['brew_times']:
                                        return brew_time
                                else:
                                        print("Invalid brew time. Please try again.")
                        except ValueError:
                                print("Invalid input. Please enter a number or press Enter.")
        else:
                while True:
                        brew_time_input = input(f"Enter the custom brew time for {drink['type']} - {drink['description']} (in minutes) or press Enter to skip: ")
                        if brew_time_input.strip() == '':
                                return None
                        try:
                                brew_time = int(brew_time_input)
                                return brew_time
                        except ValueError:
                                print("Invalid input. Please enter a number or press Enter.")

def log_consumption(config, date_time, drink_id, volume, notes=""):
        drink = config[drink_id]
        with open("brew_log.txt", 'a') as file:
                log_line = f"{date_time}: Consumed {drink['type']} - {drink['description']} (ID: {drink_id}) - Volume: {volume} ounces"
                if notes:
                        log_line += f" - Notes: {notes}"
                file.write(log_line + "\n")

def main():
        config = read_config_file("bev_input.dat")
        drug_config = read_config_file("supplement.dat")

        while True:
                drink_id = get_selected_drink(config)
                if drink_id is None:
                        break
                elif drink_id == 's':
                        daily_summary(config)
                else:
                        process_drink(config, drink_id)

def process_drink(config, drink_id):
        drink = config[drink_id]
        brew_time = get_brew_time(config, drink_id)

        date_time = time.strftime("%Y-%m-%d %H:%M:%S")

        volume = input(f"Please enter the volume for {drink['type']} - {drink['description']} (default {drink['volume']} ounces): ")
        volume = float(volume) if volume else drink['volume']

        if brew_time:
                print(f"\nPreparing {drink['type']} - {drink['description']}...")
                print(f"Brewing time: {format_time(brew_time * 60 * 1000)}")
                start_time = time.time()
                for i in range(brew_time * 60 * 10, 0, -1):
                        remaining_milliseconds = int((start_time + brew_time * 60 - time.time()) * 1000)
                        print(f"Time remaining: {format_time(remaining_milliseconds)}", end='\r')
                        time.sleep(0.1)
                print("\nBrewing completed!")

        notes = input("Enter any notes (optional): ")

        log_consumption(config, date_time, drink_id, volume, notes)

        print(f"\nEnjoy your {drink['type']} - {drink['description']}!\n")

def daily_summary(config):
        with open("brew_log.txt", 'r') as file:
                lines = file.readlines()

        date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}")
        drink_info_pattern = re.compile(r"Consumed (.+?) - (.+?) \(ID: (.+?)\) - Volume: (.+?) ounces(?: - Notes: (.+))?")

        summary = {}
        total_volume = 0

        for line in lines:
                date_match = date_pattern.match(line)
                if not date_match:
                        print(f"Error: Invalid line in the log file: {line.strip()}")
                        continue

                date_str = date_match.group()
                date_time = time.strptime(date_str, "%Y-%m-%d")

                drink_info_match = drink_info_pattern.search(line)
                if not drink_info_match:
                        print(f"Error: Invalid drink info in the log file: {line.strip()}")
                        continue

                drink_type, description, drink_id, volume, notes = drink_info_match.groups()
                volume = float(volume)
                total_volume += volume

                if date_time not in summary:
                        summary[date_time] = {}

                if drink_type not in summary[date_time]:
                        summary[date_time][drink_type] = 0

                summary[date_time][drink_type] += volume

        print("\nDaily Summary:")
        for date_time, drinks in summary.items():
                date_str = time.strftime("%Y-%m-%d", date_time)
                print(f"\nDate: {date_str}")
                for drink_type, volume in drinks.items():
                        print(f"{drink_type}: {volume} ounces")
                print(f"Total: {total_volume} ounces")
        input_ak = input("Press enter:")

def format_time(milliseconds):
        seconds, milliseconds = divmod(milliseconds, 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

if __name__ == "__main__":
        main()

