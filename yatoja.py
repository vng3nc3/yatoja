#!/usr/bin/env python

'''
Convert YAML file to JSON 
'''

import os
import yaml
import json
import pyfiglet

# Banner Function
def print_banner():
    print()
    print("-=vng3nc3=-")
    print()
    ascii_banner = pyfiglet.figlet_format("YatoJa")
    print(ascii_banner)
    print("Convert all yml or Yaml files in your directory to json")
    print()

# Colors Definition
def print_red_text(text):
    print(f"\033[91m{text}\033[0m")

def print_bright_green_text(text):
    print(f"\033[92m{text}\033[0m")

def convert_yaml_to_json():
    """
    Function converts all .yml or .yaml to json in the given directory
    """
    directory = os.getcwd()
    files_found = False

    for filename in os.listdir(directory):
        if filename.endswith('.yml') or filename.endswith('.yaml'):
            files_found = True
            yaml_file = os.path.join(directory, filename)
            json_file = os.path.join(directory, f'{filename.split(".")[0]}.json')            

            try:
                with open(yaml_file, 'r') as file:
                    configuration = yaml.safe_load(file)
            except yaml.YAMLError as e:
                print_red_text(f"Error loading YAML file {filename}: {str(e)}")
                continue

            try:
                with open(json_file, 'w') as file:
                    json.dump(configuration, file, indent=2)
            except IOError as e:
                print_red_text(f"Error writing JSON file {json_file}: {str(e)}")
                continue

            print_bright_green_text(f'[OK] Converted {filename} to {json_file}')

    if not files_found:
        print_red_text("No YAML files found in the given directory.")


# Execute Functions
print_banner()
convert_yaml_to_json()