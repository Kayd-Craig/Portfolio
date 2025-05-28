import re
from configparser import ConfigParser

CONFIG_FILEPATH = "config.ini"
DEFAULT_CONFIG = {
    "Theme": {
        "primary_color": "#4C721D",
        "secondary_color": "#FFFFFF"
    }
}


class Config:
    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config.read(CONFIG_FILEPATH)
        self.populate_config()
        self.validate_config()
        self.save_config()

    def populate_config(self) -> None:
        for section, options in DEFAULT_CONFIG.items():
            if section not in self.config:
                self.config[section] = options
            else:
                for option, value in options.items():
                    if option not in self.config[section]:
                        self.config[section][option] = value

    def validate_config(self) -> None:
        self.validate_theme()

    def validate_theme(self) -> None:
        for option in DEFAULT_CONFIG['Theme'].keys():
            if not self.is_valid_color(self.config['Theme'][option]):
                self.config['Theme'][option] = DEFAULT_CONFIG['Theme'][option]

    def is_valid_color(self, color: str) -> bool:
        pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
        return re.match(pattern, color) is not None

    def save_config(self) -> None:
        with open(CONFIG_FILEPATH, "w") as file:
            self.config.write(file)

    def __getattr__(self, option: str) -> str:
        for section in self.config.sections():
            if option in self.config[section]:
                return self.config[section][option]
        return ""


config = Config()
