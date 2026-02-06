from colorama import Style


class Utils:
    @staticmethod
    def set_color(s, color):
        return f"{Style.BRIGHT}{color}{s}{Style.RESET_ALL}"
