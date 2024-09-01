import customtkinter as ctk
from tkinter import filedialog
import os

class AdvancePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller