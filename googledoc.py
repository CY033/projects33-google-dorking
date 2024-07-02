import webbrowser
import tkinter as tk
from tkinter import messagebox
import sys

def google_dork(target):
    dorks = [
        f'site:{target}',
        f'site:{target} intitle:index.of',
        f'site:{target} inurl:login',
        f'site:{target} inurl:admin',
        f'site:{target} filetype:pdf',
        f'site:{target} filetype:xls',
        f'site:{target} "confidential"',
        f'site:{target} "sensitive information"',
        f'site:{target} "password"',
        f'site:{target} "user credentials"',
        f'site:{target} "financial report"',
        f'site:{target} "proprietary"',
        f'site:{target} "for internal use only"'
    ]

    for dork in dorks:
        url = f'https://www.google.com/search?q={dork}'
        webbrowser.open(url)

def on_submit():
    target = entry.get()
    if target:
        google_dork(target)
    else:
        messagebox.showwarning("Input Error", "Please enter a target domain.")

def show_help():
    help_message = """
    GoogleDoc Tool

    This tool allows you to perform Google dorking on a specified target domain.
    Simply enter the target domain and click "Start Google Dorking" to begin.

    Usage:
        Run the tool and enter the target domain when prompted.
    
    Command-line options:
        --help          Show this help message and exit.
    """
    print(help_message)

if __name__ == "__main__":
    if "--help" in sys.argv:
        show_help()
    else:
        # Create the main window
        root = tk.Tk()
        root.title("GoogleDoc")

        # Create and place the widgets
        label = tk.Label(root, text="Enter the target domain (e.g., example.com):")
        label.pack(padx=10, pady=10)

        entry = tk.Entry(root, width=50)
        entry.pack(padx=10, pady=10)

        button = tk.Button(root, text="Start Google Dorking", command=on_submit)
        button.pack(padx=10, pady=10)

        # Run the application
        root.mainloop()
