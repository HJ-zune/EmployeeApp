import customtkinter as ctk

class LoginPage(ctk.CTk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.title("Login")
        self.geometry("500x250")  # Adjusted dimensions (wider and slightly taller)

        # Configure grid to make text boxes extend with the window
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Title
        self.title_label = ctk.CTkLabel(self, text="Login", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Username Label and Entry
        self.username_label = ctk.CTkLabel(self, text="Username:", font=("Arial", 16))
        self.username_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")

        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        # Password Label and Entry
        self.password_label = ctk.CTkLabel(self, text="Password:", font=("Arial", 16))
        self.password_label.grid(row=2, column=0, padx=20, pady=10, sticky="e")

        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        # Login Button
        self.login_button = ctk.CTkButton(self, text="Login", command=self.check_credentials)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20)

        # Error Message Label
        self.error_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="red")
        self.error_label.grid(row=4, column=0, columnspan=2)

        # Bind the Enter key to the login button
        self.bind('<Return>', lambda event: self.login_button.invoke())

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "a123456":
            print("Credentials are correct. Hiding the login window.")
            self.withdraw()  # Hide the login window

            # Delay the execution to allow the hiding process to complete
            self.after(500, self.start_main_app)
        else:
            self.error_label.configure(text="Invalid username or password")
            print("Invalid credentials provided.")

    def start_main_app(self):
        print("Starting the main application.")
        self.controller.show_main_app()  # Start the main application
        print("Destroying the login window.")
        self.destroy()  # Destroy the login window after the main application starts
