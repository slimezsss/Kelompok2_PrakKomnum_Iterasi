import tkinter as tk
from tkinter import ttk, messagebox
from sympy import symbols, sympify, SympifyError

class FixedPointApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metode Iterasi Titik Tetap (Fixed Point Iteration)")
        self.root.geometry("720x560")
        self.root.configure(bg="#f7f9fb")

        # Palet warna
        soft_green = "#d9f2e6"
        mint_green = "#a9d6bf"
        light_gray = "#f7f9fb"
        header_green = "#bfe8d2"
        text_color = "#333333"

        # Konfigurasi gaya tampilan
        style = ttk.Style(self.root)
        style.theme_use("clam")

        style.configure("TFrame", background=soft_green)
        style.configure("TLabelframe", background=soft_green)
        style.configure("TLabelframe.Label", background=soft_green, foreground=text_color, font=("Segoe UI", 10, "bold"))
        style.configure("TLabel", background=soft_green, foreground=text_color, font=("Segoe UI", 10))
        style.configure("TEntry", font=("Segoe UI", 10))
        style.configure("TButton", background=mint_green, foreground="black", font=("Segoe UI", 10, "bold"))
        style.map("TButton", background=[("active", "#9ccfb6")])
        style.configure("Header.TLabel", background=soft_green, foreground="#007f5f", font=("Segoe UI", 11, "bold"))

        # Tampilan tabel hasil iterasi
        style.configure("Treeview", background="white", foreground=text_color, rowheight=25,
                        fieldbackground="white", font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background=header_green, foreground="#004d40", font=("Segoe UI", 10, "bold"))
        style.map("Treeview.Heading", background=[("active", "#a9d6bf")])
