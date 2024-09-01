import customtkinter as ctk
from PIL import Image
import os
from settings_page import SettingsPage
from employees_page import EmployeesPage
from salaries_page import SalariesPage  # Import the SalariesPage class
from login_page import LoginPage
from advance_page import AdvancePage  # Import the AdvancePage class

# Initialize the customtkinter application
ctk.set_appearance_mode("light")  # Default mode is light
ctk.set_default_color_theme("blue")  # Default theme is blue

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Employee Application")
        self.geometry("1000x600")

        # Initialize the list to track scheduled tasks
        self.scheduled_tasks = []

        # Override the close button behavior
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Initially show the login window
        self.show_login_page()

    def show_login_page(self):
        """Display the login page in a separate window."""
        print("Displaying the login page.")
        login_window = LoginPage(self)
        login_window.mainloop()

    def show_main_app(self):
        """Initialize and display the main application after successful login."""
        print("Loading settings for the main application.")
        self.load_settings()

        # Apply the appearance mode based on settings
        print("Applying appearance mode.")
        ctk.set_appearance_mode("dark" if self.dark_mode else "light")

        # Create a top navigation bar
        print("Creating the navigation bar.")
        self.navbar = ctk.CTkFrame(self, height=80, corner_radius=0)
        self.navbar.pack(side="top", fill="x")

        # Create content frame for pages
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True)

        # Load icons
        home_icon = self.create_icon("assets/home_icon.png")
        employee_icon = self.create_icon("assets/employee_icon.png")
        salary_icon = self.create_icon("assets/salary_icon.png")
        advance_icon = self.create_icon("assets/advance_icon.png")  # Advance icon
        vacation_icon = self.create_icon("assets/vacation_icon.png")
        settings_icon = self.create_icon("assets/settings_icon.png")

        # Add Home button to the navbar
        self.home_button = ctk.CTkButton(self.navbar, text="Home", image=home_icon, compound="top",
                                         command=self.show_home)
        self.home_button.pack(side="left", padx=10, pady=10)

        # Add Employees button to the navbar
        self.employee_button = ctk.CTkButton(self.navbar, text="Employees", image=employee_icon, compound="top",
                                             command=self.show_employees)
        self.employee_button.pack(side="left", padx=10, pady=10)

        # Add Salaries button to the navbar
        self.salary_button = ctk.CTkButton(self.navbar, text="Salaries", image=salary_icon, compound="top",
                                           command=self.show_salaries)
        self.salary_button.pack(side="left", padx=10, pady=10)

        # Add Advance button to the navbar
        self.advance_button = ctk.CTkButton(self.navbar, text="Advance", image=advance_icon, compound="top",
                                            command=self.show_advance)
        self.advance_button.pack(side="left", padx=10, pady=10)

        # Add Vacations button to the navbar
        self.vacation_button = ctk.CTkButton(self.navbar, text="Vacations", image=vacation_icon, compound="top",
                                             command=self.show_vacations)
        self.vacation_button.pack(side="left", padx=10, pady=10)

        # Add Settings button to the navbar
        self.settings_button = ctk.CTkButton(self.navbar, text="Settings", image=settings_icon, compound="top",
                                             command=self.show_settings)
        self.settings_button.pack(side="left", padx=10, pady=10)

        # Initially show the home page
        print("Showing the home page.")
        self.show_home()

        # Explicitly run the main loop to keep the window open
        print("Running main application loop.")
        self.mainloop()

    def create_icon(self, path):
        """Load an icon from the assets folder."""
        image = Image.open(path).resize((40, 40), Image.Resampling.LANCZOS)
        return ctk.CTkImage(light_image=image, size=(40, 40))

    def show_home(self):
        """Display the Home page."""
        print("Clearing the content frame and showing the home page.")
        self.clear_content_frame()
        home_label = ctk.CTkLabel(self.content_frame, text="Welcome to the Home Page", font=("Arial", 24))
        home_label.pack(pady=20)

    def show_employees(self):
        """Display the Employees page."""
        print("Clearing the content frame and showing the employees page.")
        self.clear_content_frame()
        employees_page = EmployeesPage(self.content_frame, self)
        employees_page.pack(fill="both", expand=True)

    def show_salaries(self):
        """Display the Salaries page."""
        print("Clearing the content frame and showing the salaries page.")
        self.clear_content_frame()
        salaries_page = SalariesPage(self.content_frame, self)
        salaries_page.pack(fill="both", expand=True)

    def show_advance(self):
        """Display the Advance page."""
        print("Clearing the content frame and showing the advance page.")
        self.clear_content_frame()
        advance_page = AdvancePage(self.content_frame, self)
        advance_page.pack(fill="both", expand=True)

    def show_vacations(self):
        """Display the Vacations page."""
        self.clear_content_frame()
        vacation_label = ctk.CTkLabel(self.content_frame, text="Vacation Management", font=("Arial", 24))
        vacation_label.pack(pady=20)

    def show_settings(self):
        """Display the Settings page."""
        self.clear_content_frame()
        settings_page = SettingsPage(self.content_frame, self)
        settings_page.pack(fill="both", expand=True)

    def clear_content_frame(self):
        """Clear the content frame but keep the navigation bar."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def load_settings(self):
        """Load settings from file."""
        print("Checking for settings file.")
        if os.path.exists("settings.txt"):
            with open("settings.txt", "r") as settings_file:
                for line in settings_file:
                    key, value = line.strip().split("=")
                    if key == "dark_mode":
                        self.dark_mode = value.lower() == "true"
                    elif key == "excel_file_path":
                        self.excel_file_path = value
        print("Settings loaded.")

    def schedule_task(self, delay, task):
        """Schedule a task and keep track of it."""
        task_id = self.after(delay, task)
        self.scheduled_tasks.append(task_id)

    def cancel_scheduled_tasks(self):
        """Cancel all scheduled tasks."""
        for task_id in self.scheduled_tasks:
            try:
                self.after_cancel(task_id)
            except ValueError:
                print(f"Task {task_id} could not be canceled.")
        self.scheduled_tasks.clear()

    def on_closing(self):
        """Handle the window close event."""
        print("Cancelling all scheduled tasks.")
        self.cancel_scheduled_tasks()
        print("Quitting the main loop.")
        self.quit()  # Stop the main loop
        print("Destroying the application window.")
        self.destroy()  # Destroy the window after quitting the main loop

if __name__ == "__main__":
    print("Starting the application.")
    app = App()
    app.mainloop()
