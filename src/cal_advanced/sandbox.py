from colorama import Fore, Style, init

init()  # достаточно один раз

text = "XX"

c = Fore.RED
def set_color(s, color):
    return f"{Style.BRIGHT}{color}{s}{Style.RESET_ALL}"

print(set_color(text, c))

