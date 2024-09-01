import customtkinter as ctk
from tkinter import filedialog
import os

class SettingsPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Dark Mode Toggle Switch
        self.dark_mode_label = ctk.CTkLabel(self, text="Dark Mode:", font=("Arial", 16))
        self.dark_mode_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.dark_mode_toggle = ctk.CTkSwitch(self, text="", command=self.toggle_dark_mode)
        self.dark_mode_toggle.grid(row=0, column=1, padx=20, pady=20)
        self.dark_mode_toggle.select() if controller.dark_mode else self.dark_mode_toggle.deselect()

        # Excel File Path Text Box
        self.excel_path_label = ctk.CTkLabel(self, text="Excel File Path:", font=("Arial", 16))
        self.excel_path_label.grid(row=1, column=0, padx=20, pady=20, sticky="w")

        self.excel_path_entry = ctk.CTkEntry(self, width=300)
        self.excel_path_entry.grid(row=1, column=1, padx=20, pady=20)
        self.excel_path_entry.insert(0, controller.excel_file_path)

        # Browse Button
        self.browse_button = ctk.CTkButton(self, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=2, padx=10, pady=20)

        # Save Button
        self.save_button = ctk.CTkButton(self, text="Save Settings", command=self.save_settings)
        self.save_button.grid(row=2, column=0, columnspan=3, pady=20)

        # Success/Error Label (initially hidden)
        self.feedback_label = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.feedback_label.grid(row=3, column=0, columnspan=3)

    def toggle_dark_mode(self):
        # Toggle dark mode setting
        self.controller.dark_mode = not self.controller.dark_mode

        # Apply the theme change
        ctk.set_appearance_mode("dark" if self.controller.dark_mode else "light")

    def browse_file(self):
        # Open a file dialog to select the Excel file
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel Files", "*.xlsx")],
            initialdir=os.path.expanduser("~")
        )
        if file_path:
            self.excel_path_entry.delete(0, ctk.END)
            self.excel_path_entry.insert(0, file_path)

    def save_settings(self):
        # Normalize the path to handle different formats and strip quotes
        file_path = os.path.normpath(self.excel_path_entry.get().strip('"'))

        # Validate the file path
        if not file_path.endswith('.xlsx'):
            self.feedback_label.configure(text="Error: Please select a valid Excel file (.xlsx)", text_color="red")
            return

        # Save settings if valid
        self.controller.excel_file_path = file_path
        with open("settings.txt", "w") as settings_file:
            settings_file.write(f"dark_mode={self.controller.dark_mode}\n")
            settings_file.write(f"excel_file_path={self.controller.excel_file_path}\n")

        # Update the success label
        self.feedback_label.configure(text="Settings saved successfully!", text_color="green")
        self.after(3000, self.clear_feedback_message)  # Clear the message after 3 seconds

    def clear_feedback_message(self):
        self.feedback_label.configure(text="")
