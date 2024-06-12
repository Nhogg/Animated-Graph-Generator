# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from graph_gen import generate_video_from_data

class AnimatedChartGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Chart Generator")

        # Input File
        self.input_file_label = tk.Label(root, text="Input File:")
        self.input_file_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_file_entry = tk.Entry(root, width=50)
        self.input_file_entry.grid(row=0, column=1, padx=10, pady=10)
        self.input_file_button = tk.Button(root, text="Browse", command=self.browse_input_file)
        self.input_file_button.grid(row=0, column=2, padx=10, pady=10)

        # X Column
        self.x_col_label = tk.Label(root, text="X Column:")
        self.x_col_label.grid(row=1, column=0, padx=10, pady=10)
        self.x_col_entry = tk.Entry(root, width=50)
        self.x_col_entry.grid(row=1, column=1, padx=10, pady=10)

        # Y Column
        self.y_col_label = tk.Label(root, text="Y Column:")
        self.y_col_label.grid(row=2, column=0, padx=10, pady=10)
        self.y_col_entry = tk.Entry(root, width=50)
        self.y_col_entry.grid(row=2, column=1, padx=10, pady=10)

        # Title Template
        self.title_template_label = tk.Label(root, text="Title Template:")
        self.title_template_label.grid(row=3, column=0, padx=10, pady=10)
        self.title_template_entry = tk.Entry(root, width=50)
        self.title_template_entry.grid(row=3, column=1, padx=10, pady=10)
        self.title_template_entry.insert(0, '{time}')

        # Output File
        self.output_file_label = tk.Label(root, text="Output File:")
        self.output_file_label.grid(row=4, column=0, padx=10, pady=10)
        self.output_file_entry = tk.Entry(root, width=50)
        self.output_file_entry.grid(row=4, column=1, padx=10, pady=10)
        self.output_file_button = tk.Button(root, text="Browse", command=self.browse_output_file)
        self.output_file_button.grid(row=4, column=2, padx=10, pady=10)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate", command=self.generate_video)
        self.generate_button.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx *.xls")])
        self.input_file_entry.delete(0, tk.END)
        self.input_file_entry.insert(0, file_path)

    def browse_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        self.output_file_entry.delete(0, tk.END)
        self.output_file_entry.insert(0, file_path)

    def generate_video(self):
        input_file = self.input_file_entry.get()
        x_col = self.x_col_entry.get()
        y_col = self.y_col_entry.get()
        output_file = self.output_file_entry.get()
        title_template = self.title_template_entry.get()

        if not input_file or not x_col or not y_col or not output_file:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            generate_video_from_data(input_file, x_col, y_col, output_file, title_template)
            messagebox.showinfo("Success", "Video generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedChartGUI(root)
    root.mainloop()
