import configparser
import sys
import os

class ConfigReader:

    @staticmethod
    def read_config(section: str, key: str) -> str:
        # Get the root directory of the project
        root_dir = sys.path[0]
        config_path = os.path.join(root_dir, 'config.ini')

        # Load the config file
        config = configparser.ConfigParser()
        config.read(config_path)

        # Validate section and key
        if config.has_section(section) and config.has_option(section, key):
            return config.get(section, key)
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")
