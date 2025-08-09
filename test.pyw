import customtkinter as ctk
import sys
import subprocess
import os

# --- Configuration ---
# You can change the question and button text here
APP_WIDTH = 380
APP_HEIGHT = 180
QUESTION_TEXT = "Select frequent search points.."
BUTTON_OPTIONS = ["Close", "old version", "New version"]



# ---------------------

class StartupNotification(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Basic Window Setup ---
        self.title("Daily Check-in")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")

        

        # This makes the window appear without the standard title bar and borders
        self.overrideredirect(True)

        

        # This makes the window stay on top of all other applications
        self.attributes('-topmost', True)

        # --- Position the Window in the Bottom-Right Corner ---
        self.position_window()

        # --- Create and Configure Widgets ---
        self.create_widgets()

    def position_window(self):
        """Calculates and sets the window position to the bottom-right of the screen."""
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set a padding from the screen edges
        padding_x = 20
        padding_y = 40 # A bit more padding from the taskbar

        # Calculate the x and y coordinates for the window
        pos_x = screen_width - APP_WIDTH - padding_x
        pos_y = screen_height - APP_HEIGHT - padding_y

        # Set the geometry with the new position
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}+{pos_x}+{pos_y}")

    def create_widgets(self):
        """Creates the main frame, label, and buttons for the notification."""
        # Main container frame with padding
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.pack(padx=15, pady=15, fill="both", expand=True)

        # The question label
        question_label = ctk.CTkLabel(
            main_frame,
            text=QUESTION_TEXT,
            font=ctk.CTkFont(size=16, weight="bold"),
            wraplength=APP_WIDTH - 60 # Wrap text if it's too long
        )
        question_label.pack(pady=(15, 20), padx=10)

        # Frame to hold the buttons horizontally
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=(10, 15), fill="x", expand=True)
        
        # Configure the columns to be of equal weight so they space out evenly
        button_frame.grid_columnconfigure(tuple(range(len(BUTTON_OPTIONS))), weight=1)

        self.points_value = ctk.IntVar(button_frame,value=6)
        slider = ctk.CTkSlider(button_frame,variable=self.points_value,from_=0,to=60,number_of_steps=20)
        slider.grid(row=0, column=1, padx=10, sticky="ew")

        # Create buttons from the BUTTON_OPTIONS list
        for i, option_text in enumerate(BUTTON_OPTIONS):
            button = ctk.CTkButton(
                button_frame,
                text=option_text,
                command=lambda response=option_text: self.button_action(response)
            )
            # Place each button in the grid
            button.grid(row=1, column=i, padx=5, sticky="ew")
        

    def button_action(self, response):
        """
        This function is called when a button is clicked.
        You can add logic here to log the response to a file.
        """
        print(f"User selected: '{response}'. Closing application.")
        if response == "old version":
            home_dir = os.path.expanduser('~')
    
            # Path for a desktop synced with OneDrive
            onedrive_desktop_path = os.path.join(home_dir, 'OneDrive', 'Desktop', 'newBing.bat')
            
            # Path for a standard local desktop
            local_desktop_path = os.path.join(home_dir, 'Desktop', 'newBing.bat')

            # Check if the OneDrive path exists and use it, otherwise use the local path
            if os.path.exists(onedrive_desktop_path):
                batch_file = onedrive_desktop_path
            else:
                batch_file = local_desktop_path
                
            # Run the batch file
            os.system(f'start "" "{batch_file}"')
        if response == "New version":
            home_dir = os.path.expanduser('~')
    
            # Path for a desktop synced with OneDrive
            onedrive_desktop_path = os.path.join(home_dir, 'OneDrive', 'Desktop', 'bing.bat')
            
            # Path for a standard local desktop
            local_desktop_path = os.path.join(home_dir, 'Desktop', 'bing.bat')

            # Check if the OneDrive path exists and use it, otherwise use the local path
            if os.path.exists(onedrive_desktop_path):
                batch_file = onedrive_desktop_path
            else:
                batch_file = local_desktop_path
                
            # Run the batch file
            os.system(f'start "" "{batch_file}"')

        
        # For now, we just close the app.
        self.destroy()
        sys.exit() # Ensures the script fully terminates

if __name__ == "__main__":
    # Set the appearance mode (optional, but good practice)
    ctk.set_appearance_mode("System")  # Can be "System", "Dark", "Light"
    ctk.set_default_color_theme("blue") # Can be "blue", "green", "dark-blue"
    
    app = StartupNotification()
    app.mainloop()
