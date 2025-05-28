import os
from configparser import ConfigParser

from config import CONFIG_FILEPATH, DEFAULT_CONFIG, Config


def test_default_config_population() -> None:
    """Test that default config is populated when config file does not exist."""
    # Ensure the config file does not exist
    if os.path.exists(CONFIG_FILEPATH):
        os.remove(CONFIG_FILEPATH)

    # Instantiate the Config class
    config = Config()

    # Now the temp config file should be created
    assert os.path.exists(CONFIG_FILEPATH)

    # Read the config file
    parser = ConfigParser()
    parser.read(CONFIG_FILEPATH)

    # Check that default config is written
    for section, options in DEFAULT_CONFIG.items():
        assert parser.has_section(section)
        for option, value in options.items():
            assert parser.has_option(section, option)
            assert parser.get(section, option) == value


def test_existing_config_preservation() -> None:
    """Test that existing config options are preserved and missing defaults are added."""
    # Create an initial config with some values
    parser = ConfigParser()
    parser.add_section("Theme")
    parser.set("Theme", "primary_color", "#123456")
    parser.set("Theme", "custom_option", "custom_value")
    with open(CONFIG_FILEPATH, "w") as f:
        parser.write(f)

    # Instantiate the Config class
    config = Config()

    # Read the updated config file
    parser.read(CONFIG_FILEPATH)

    # Check that existing values are preserved
    assert parser.get("Theme", "primary_color") == "#123456"
    assert parser.get("Theme", "custom_option") == "custom_value"

    # Check that missing default options are added
    assert parser.has_option("Theme", "secondary_color")
    assert parser.get("Theme", "secondary_color") == "#FFFFFF"


def test_invalid_color_replacement() -> None:
    """Test that invalid color values are replaced with defaults."""
    # Create a config with invalid colors
    parser = ConfigParser()
    parser.add_section("Theme")
    parser.set("Theme", "primary_color", "invalid_color")
    parser.set("Theme", "secondary_color", "#XYZ123")  # Invalid hex color
    with open(CONFIG_FILEPATH, "w") as f:
        parser.write(f)

    # Instantiate the Config class
    config = Config()

    # Read the updated config file
    parser.read(CONFIG_FILEPATH)

    # Check that invalid colors are replaced with defaults
    assert parser.get(
        "Theme", "primary_color") == DEFAULT_CONFIG["Theme"]["primary_color"]
    assert parser.get(
        "Theme", "secondary_color") == DEFAULT_CONFIG["Theme"]["secondary_color"]


def test_valid_color_accepted() -> None:
    """Test that valid color values are accepted and kept."""
    # Create a config with valid colors
    parser = ConfigParser()
    parser.add_section("Theme")
    parser.set("Theme", "primary_color", "#ABCDEF")
    parser.set("Theme", "secondary_color", "#123abc")
    with open(CONFIG_FILEPATH, "w") as f:
        parser.write(f)

    # Instantiate the Config class
    config = Config()

    # Read the updated config file
    parser.read(CONFIG_FILEPATH)

    # Check that valid colors are kept
    assert parser.get("Theme", "primary_color") == "#ABCDEF"
    assert parser.get("Theme", "secondary_color") == "#123abc"


def test_getattr_method() -> None:
    """Test the __getattr__ method for accessing config options."""
    # Create a config with some options
    parser = ConfigParser()
    parser.add_section("Theme")
    parser.set("Theme", "primary_color", "#ABCDEF")
    parser.set("Theme", "secondary_color", "#123abc")
    with open(CONFIG_FILEPATH, "w") as f:
        parser.write(f)

    # Instantiate the Config class
    config = Config()

    # Test __getattr__ method
    assert config.primary_color == "#ABCDEF"
    assert config.secondary_color == "#123abc"
    # Test an option that doesn't exist
    assert config.non_existent_option == ""


def test_is_valid_color() -> None:
    """Test the is_valid_color method."""
    config = Config()
    valid_colors = ["#123456", "#abc", "#ABCDEF", "#789"]
    invalid_colors = ["123456", "#12345G", "#1234", "#1234567", "blue"]

    for color in valid_colors:
        assert config.is_valid_color(color)
    for color in invalid_colors:
        assert not config.is_valid_color(color)
