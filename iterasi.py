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

        # ==== FRAME INPUT ====
        input_frame = ttk.LabelFrame(self.root, text="Parameter Input", padding=(15, 10), style="TLabelframe")
        input_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(input_frame, text="Persamaan f(x) = 0:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.f_expr_var = tk.StringVar(value="x**2 - 2*x - 3")
        ttk.Entry(input_frame, textvariable=self.f_expr_var, width=30).grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(input_frame, text="Nilai Awal (x₀):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.x0_var = tk.StringVar(value="4")
        ttk.Entry(input_frame, textvariable=self.x0_var, width=15).grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(input_frame, text="Toleransi (ε):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.epsilon_var = tk.StringVar(value="0.0001")
        ttk.Entry(input_frame, textvariable=self.epsilon_var, width=15).grid(row=2, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(input_frame, text="Maks Iterasi (N):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.n_var = tk.StringVar(value="15")
        ttk.Entry(input_frame, textvariable=self.n_var, width=15).grid(row=3, column=1, sticky="w", padx=5, pady=5)

        input_frame.columnconfigure(1, weight=1)

        # Tombol eksekusi
        ttk.Button(
            self.root,
            text="Jalankan Iterasi",
            command=self.run_calculation,
            style="TButton"
        ).pack(pady=10, padx=10, fill="x")

output_frame = ttk.LabelFrame(self.root, text="Hasil Iterasi", padding=(15, 10), style="TLabelframe")
        output_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.g_auto_label = ttk.Label(output_frame, text="g(x) akan ditampilkan di sini...", style="Header.TLabel")
        self.g_auto_label.pack(pady=(0, 10))

        columns = ("iterasi", "x", "g(x)", "f(x)")
        self.tree = ttk.Treeview(output_frame, columns=columns, show="headings", style="Treeview")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=140)

        scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        # Label hasil akhir
        self.result_label = ttk.Label(
            self.root,
            text="Hasil akhir akan muncul di sini.",
            background=light_gray,
            foreground="#007f5f",
            font=("Segoe UI", 10, "italic")
        )
        self.result_label.pack(pady=10)

    def clear_results(self):
        """Membersihkan hasil tabel dan label sebelum proses baru."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.result_label.config(text="Hasil akhir akan muncul di sini.", foreground="#007f5f")
        self.g_auto_label.config(text="g(x) akan ditampilkan di sini...")

    def validate_and_prepare(self):
        """Validasi input pengguna dan bentuk fungsi g(x) dari f(x)."""
        try:
            f_str = self.f_expr_var.get()
            x0 = float(self.x0_var.get())
            epsilon = float(self.epsilon_var.get())
            N = int(self.n_var.get())
        except ValueError:
            messagebox.showerror("Error", "Input numerik tidak valid.")
            return None

        try:
            x = symbols("x")
            f_expr = sympify(f_str)
        except SympifyError:
            messagebox.showerror("Error", "Persamaan tidak valid.")
            return None

        # Membentuk fungsi g(x) otomatis
        a = f_expr.expand().coeff(x, 2)
        b = f_expr.expand().coeff(x, 1)
        c = f_expr.expand().coeff(x, 0)
        g_expr = -c / (a*x + b)
        self.g_auto_label.config(text=f"g(x) = {g_expr}")

        return f_expr, g_expr, x, x0, epsilon, N

 

