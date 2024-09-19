from configparser import ConfigParser


class ConfigHelper:
    config = ConfigParser()

    @classmethod
    def get_value(cls, key: str) -> str:
        try:
            file = open("settings.ini", "x")
            file.close()
        except FileExistsError:
            pass

        cls.config.read("settings.ini")
        try:
            value = cls.config["SETTINGS"][key]
        except KeyError:
            value = input(f"Enter {key}: ")
            if not cls.config.has_section("SETTINGS"):
                cls.config.add_section("SETTINGS")
            cls.config.set("SETTINGS", key, value)
            with open("settings.ini", "w") as configfile:
                cls.config.write(configfile)

        return value
