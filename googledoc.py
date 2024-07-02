import webbrowser
import tkinter as tk
from tkinter import messagebox
import sys

banner = ''' 
               ______                  __          ____             __            
              / ____/___  ____  ____ _/ /__       / __ \\____  _____/ /_____  _____
             / / __/ __ \\/ __ \\/ __ `/ / _ \\     / / / / __ \\/ ___/ //_/ _ \\/ ___/
            / /_/ / /_/ / /_/ / /_/ / /  __/    / /_/ / /_/ / /  / ,< /  __/ /    
            \\____/\\____/\\____/\\__, /_/\\___/    /_____\\/____/_/  /_/|_|\\___/_/     
                             /____/                                                 

    Made By: Musharraf khan (github.com/Musharraf33)
'''

def google_dork(target, search_engine):
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
        f'site:{target} "for internal use only"',
        f'site:{target} "internal audit"',
        f'site:{target} "employee details"',
        f'site:{target} "internal memo"',
        f'site:{target} "meeting minutes"',
        f'site:{target} "private"',
        f'site:{target} "restricted"',
        f'site:{target} "backup"',
        f'site:{target} "db_backup"',
        f'site:{target} "database"',
        # Add more dorks as needed
    ]

    search_engines = {
        'Google': 'https://www.google.com/search?q=',
        'Bing': 'https://www.bing.com/search?q=',
        'DuckDuckGo': 'https://duckduckgo.com/?q=',
        'Yahoo': 'https://search.yahoo.com/search?p=',
        'Firefox': 'https://www.firefox.com/search?q=',
        'Shodan': 'https://www.shodan.io/search?query=',
        'Censys Search': 'https://search.censys.io/search?q='
    }

    if search_engine not in search_engines:
        raise ValueError(f"Search engine '{search_engine}' is not supported.")

    base_url = search_engines[search_engine]

    for dork in dorks:
        url = f'{base_url}{dork}'
        webbrowser.open_new_tab(url)

def on_submit():
    target = entry.get().strip()
    search_engine = search_engine_var.get()

    if target:
        try:
            google_dork(target, search_engine)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please enter a target domain.")

def show_help():
    help_message = """
    GoogleDoc Tool

    This tool allows you to perform Google dorking on a specified target domain.
    Simply enter the target domain and select a search engine, then click "Start Google Dorking" to begin.

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
        # Create main window
        root = tk.Tk()
        root.title("GoogleDoc")

        # Display banner in console
        print(banner)

        # Create and place the widgets
        label = tk.Label(root, text="Enter the target domain (e.g., example.com):")
        label.pack(padx=10, pady=10)

        entry = tk.Entry(root, width=50)
        entry.pack(padx=10, pady=10)

        search_engine_var = tk.StringVar(root)
        search_engine_var.set('Google')  # default value
        search_engine_label = tk.Label(root, text="Select search engine:")
        search_engine_label.pack(padx=10, pady=5)

        search_engine_dropdown = tk.OptionMenu(root, search_engine_var, 'Google', 'Bing', 'DuckDuckGo', 'Yahoo', 'Firefox', 'Shodan', 'Censys Search')
        search_engine_dropdown.pack(padx=10, pady=5)

        button = tk.Button(root, text="Start Google Dorking", command=on_submit)
        button.pack(padx=10, pady=10)

        # Run the main loop
        root.mainloop()
