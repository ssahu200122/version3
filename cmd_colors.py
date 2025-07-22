import os

# --- ANSI Escape Codes for Text Formatting ---
# ANSI escape codes are special sequences of characters that terminals
# interpret as commands to change text formatting (colors, styles).
# Windows Terminal natively supports these.

# Reset all attributes

class Colors:
    def __init__(self):
        self.RESET = "\033[0m"

        # Text Styles
        self.BOLD = "\033[1m"
        self.ITALIC = "\033[3m" # Not all terminals support italic
        self.UNDERLINE = "\033[4m"
        self.STRIKETHROUGH = "\033[9m" # Not all terminals support strikethrough

        # Foreground Colors (Text Color)
        self.BLACK = "\033[30m"
        self.RED = "\033[31m"
        self.GREEN = "\033[32m"
        self.YELLOW = "\033[33m"
        self.BLUE = "\033[34m"
        self.MAGENTA = "\033[35m"
        self.CYAN = "\033[36m"
        self.WHITE = "\033[37m"

        # Bright Foreground Colors
        self.BRIGHT_BLACK = "\033[90m"
        self.BRIGHT_RED = "\033[91m"
        self.BRIGHT_GREEN = "\033[92m"
        self.BRIGHT_YELLOW = "\033[93m"
        self.BRIGHT_BLUE = "\033[94m"
        self.BRIGHT_MAGENTA = "\033[95m"
        self.BRIGHT_CYAN = "\033[96m"
        self.BRIGHT_WHITE = "\033[97m"

        # Background Colors
        self.BG_BLACK = "\033[40m"
        self.BG_RED = "\033[41m"
        self.BG_GREEN = "\033[42m"
        self.BG_YELLOW = "\033[43m"
        self.BG_BLUE = "\033[44m"
        self.BG_MAGENTA = "\033[45m"
        self.BG_CYAN = "\033[46m"
        self.BG_WHITE = "\033[47m"

        # Bright Background Colors
        self.BG_BRIGHT_BLACK = "\033[100m"
        self.BG_BRIGHT_RED = "\033[101m"
        self.BG_BRIGHT_GREEN = "\033[102m"
        self.BG_BRIGHT_YELLOW = "\033[103m"
        self.BG_BRIGHT_BLUE = "\033[104m"
        self.BG_BRIGHT_MAGENTA = "\033[105m"
        self.BG_BRIGHT_CYAN = "\033[106m"
        self.BG_BRIGHT_WHITE = "\033[107m"

# --- 256-Color (8-bit) Support ---
# For more granular control over colors, you can use 256-color codes.
# Format: \033[38;5;<color_code>m for foreground
#         \033[48;5;<color_code>m for background
    def color_256_fg(self,code):
        return f"\033[38;5;{code}m"

    def color_256_bg(self,code):
        return f"\033[48;5;{code}m"

# --- True Color (24-bit) Support ---
# For the most precise color control, use True Color (RGB).
# Format: \033[38;2;<r>;<g>;<b>m for foreground
#         \033[48;2;<r>;<g>;<b>m for background
    def color_rgb_fg(self,r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    def color_rgb_bg(self,r, g, b):
        return f"\033[48;2;{r};{g};{b}m"


    def print_colored_text(self):
        print(f"{self.BOLD}--- Basic Colors and Styles ---{self.RESET}")
        print(f"{self.RED}This text is red.{self.RESET}")
        print(f"{self.GREEN}This text is green.{self.RESET}")
        print(f"{self.YELLOW}This text is yellow.{self.RESET}")
        print(f"{self.BLUE}This text is blue.{self.RESET}")
        print(f"{self.MAGENTA}This text is magenta.{self.RESET}")
        print(f"{self.CYAN}This text is cyan.{self.RESET}")
        print(f"{self.WHITE}This text is white.{self.RESET}")
        print(f"{self.BRIGHT_RED}This text is bright red.{self.RESET}")
        print(f"{self.BOLD}This text is bold.{self.RESET}")
        print(f"{self.ITALIC}This text is italic.{self.RESET}")
        print(f"{self.UNDERLINE}This text is underlined.{self.RESET}")
        print(f"{self.STRIKETHROUGH}This text is strikethrough.{self.RESET}")
        print(f"{self.RED}{self.BOLD}This is bold red text.{self.RESET}")
        print(f"{self.BG_BLUE}{self.WHITE}White text on blue background.{self.RESET}")
        print(f"{self.BG_BRIGHT_YELLOW}{self.BLACK}Black text on bright yellow background.{self.RESET}")

        print(f"\n{self.BOLD}--- 256-Color Examples ---{self.RESET}")
        print(f"{self.color_256_fg(208)}Orange text (code 208).{self.RESET}")
        print(f"{self.color_256_fg(123)}Light blue text (code 123).{self.RESET}")
        print(f"{self.color_256_bg(22)}{self.color_256_fg(15)}White text on dark green background (bg 22, fg 15).{self.RESET}")

        print(f"\n{self.BOLD}--- True Color (RGB) Examples ---{self.RESET}")
        print(f"{self.color_rgb_fg(255, 165, 0)}This is orange using RGB (255, 165, 0).{self.RESET}")
        print(f"{self.color_rgb_fg(100, 149, 237)}This is cornflower blue using RGB (100, 149, 237).{self.RESET}")
        print(f"{self.color_rgb_bg(50, 50, 50)}{self.color_rgb_fg(255, 255, 255)}White text on dark gray background (bg 50,50,50).{self.RESET}")

        print(f"\n{self.BOLD}--- Combining Styles and Colors ---{self.RESET}")
        print(f"{self.BOLD}{self.UNDERLINE}{self.GREEN}Bold, underlined, green text!{self.RESET}")
        print(f"{self.BG_RED}{self.BRIGHT_WHITE}{self.BOLD}WARNING: Important Message!{self.RESET}")

if __name__ == "__main__":
    # On Windows, older terminals might need os.system('') to enable ANSI support,
    # but Windows Terminal handles it natively. This line is mostly for compatibility
    # with older cmd.exe versions if you were to run it there.
    # It's generally not needed for Windows Terminal.
    # os.system('')
    c = Colors()
    c.print_colored_text()

    print("\nNote: Ensure your terminal supports ANSI escape codes (Windows Terminal does!).")
    print("If you see strange characters like '[0m', your terminal might not support them.")

