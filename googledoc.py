import webbrowser
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import argparse
import sys
import time

banner = ''' 
               ______                  __          ____             __            
              / ____/___  ____  ____ _/ /__       / __ \\____  _____/ /_____  _____
             / / __/ __ \\/ __ \\/ __ `/ / _ \\     / / / / __ \\/ ___/ //_/ _ \\/ ___/
            / /_/ / /_/ / /_/ / /_/ / /  __/    / /_/ / /_/ / /  / ,< /  __/ /    
            \\____/\\____/\\____/\\__, /_/\\___/    /_____\\/____/_/  /_/|_|\\___/_/     
                             /____/                                                 

    Made By: Musharraf khan (github.com/Musharraf33)
'''

# Define predefined dorks
predefined_dorks = [
    'intitle:index.of',
    'inurl:login',
    'inurl:admin',
    'filetype:pdf',
    'filetype:xls',
    '"confidential"',
    '"sensitive information"',
    '"password"',
    '"user credentials"',
    '"financial report"',
    '"proprietary"',
    '"for internal use only"',
    '"internal audit"',
    '"employee details"',
    '"internal memo"',
    '"meeting minutes"',
    '"private"',
    '"restricted"',
    '"backup"',
    '"db_backup"',
    '"database"',
    '"benefit analysis filetype:pdf"',
    '"decision analysis filetype:pdf"',
    '"scenario analysis filetype:pdf"',
    '"sensitivity analysis filetype:pdf"',
    '"variance analysis filetype:pdf"',
    '"trend analysis filetype:pdf"',
    '"forecasting analysis filetype:pdf"',
    '"statistical analysis filetype:pdf"',
    '"predictive analysis filetype:pdf"',
    '"quantitative analysis filetype:pdf"',
    '"qualitative analysis filetype:pdf"',
    '"descriptive analysis filetype:pdf"',
    '"inferential analysis filetype:pdf"',
    '"comparative analysis filetype:pdf"',
    '"data mining filetype:pdf"',
    '"machine learning filetype:pdf"',
    '"artificial intelligence filetype:pdf"',
    '"deep learning filetype:pdf"',
    '"neural network filetype:pdf"',
    '"algorithm filetype:pdf"',
    '"model filetype:pdf"',
    '"simulation filetype:pdf"',
    '"optimization filetype:pdf"',
    '"validation filetype:pdf"',
    '"verification filetype:pdf"',
    '"certification filetype:pdf"',
    '"accreditation filetype:pdf"',
    '"audit filetype:pdf"',
    '"assessment filetype:pdf"',
    '"evaluation filetype:pdf"',
    '"review filetype:pdf"',
    # Add more dorks as needed
]

def google_dork(target, search_engine, dorks, limit=None):
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

    count = 0
    for dork in dorks:
        url = f'{base_url}site:{target} {dork}'
        webbrowser.open_new_tab(url)
        count += 1
        time.sleep(1)  # Adjust sleep duration as needed
        if limit and count >= limit:
            break

def run_gui():
    root = tk.Tk()
    root.title("GoogleDoc")

    # Display banner in console
    print(banner)

    # Set styles
    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 12), background='#f2f2f2', foreground='#333')
    style.configure('TButton', font=('Helvetica', 12), background='#007acc', foreground='white', padding=10)
    style.configure('TEntry', font=('Helvetica', 12))
    style.configure('TCombobox', font=('Helvetica', 12))

    # Main frame
    main_frame = ttk.Frame(root, padding="20 20 20 20", style='TFrame')
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    def on_submit():
        target = entry.get().strip()
        search_engine = search_engine_var.get()
        dorking_type = dorking_type_var.get()

        if target:
            if dorking_type == "Automatic":
                limit = simpledialog.askinteger("Limit", "Enter the number of dorks to perform:", minvalue=1, maxvalue=len(predefined_dorks))
                dorks = predefined_dorks[:limit]
            else:
                custom_dork = dork_entry.get().strip()
                dorks = [custom_dork]

            try:
                google_dork(target, search_engine, dorks)
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
        messagebox.showinfo("Help", help_message)

    ttk.Label(main_frame, text="Enter the target domain (e.g., example.com):", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=10)
    entry = ttk.Entry(main_frame, width=50, style='TEntry')
    entry.grid(row=1, column=0, pady=10)

    ttk.Label(main_frame, text="Select search engine:", style='TLabel').grid(row=2, column=0, sticky=tk.W, pady=10)
    search_engine_var = tk.StringVar(root)
    search_engine_var.set('Google')  # default value
    search_engine_dropdown = ttk.Combobox(main_frame, textvariable=search_engine_var, values=['Google', 'Bing', 'DuckDuckGo', 'Yahoo', 'Firefox', 'Shodan', 'Censys Search'], state='readonly', style='TCombobox')
    search_engine_dropdown.grid(row=3, column=0, pady=10)

    ttk.Label(main_frame, text="Select dorking type:", style='TLabel').grid(row=4, column=0, sticky=tk.W, pady=10)
    dorking_type_var = tk.StringVar(root)
    dorking_type_var.set('Automatic')  # default value
    dorking_type_dropdown = ttk.Combobox(main_frame, textvariable=dorking_type_var, values=['Automatic', 'Manual'], state='readonly', style='TCombobox')
    dorking_type_dropdown.grid(row=5, column=0, pady=10)

    dork_entry_label = ttk.Label(main_frame, text="Enter your custom dork:", style='TLabel')
    dork_entry = ttk.Combobox(main_frame, width=50, style='TCombobox')
    dork_entry['values'] = predefined_dorks

    def update_suggestions(event):
        typed = dork_entry.get()
        if typed == '':
            dork_entry['values'] = []
        else:
            suggestions = [dork for dork in predefined_dorks if typed.lower() in dork.lower()]
            dork_entry['values'] = suggestions

    def select_suggestion(event):
        dork_entry.icursor(tk.END)  # Move cursor to the end
        dork_entry.focus_set()  # Set focus back to the combobox

    def toggle_dork_entry(*args):
        if dorking_type_var.get() == "Manual":
            dork_entry_label.grid(row=6, column=0, sticky=tk.W, pady=10)
            dork_entry.grid(row=7, column=0, pady=10)
            dork_entry.focus()  # Set focus to the dork entry box
            dork_entry.event_generate('<Down>')  # Automatically show suggestions
        else:
            dork_entry_label.grid_forget()
            dork_entry.grid_forget()

    ttk.Button(main_frame, text="Start Google Dorking", command=on_submit, style='TButton').grid(row=8, column=0, pady=10)
    ttk.Button(main_frame, text="Show Help", command=show_help, style='TButton').grid(row=9, column=0, pady=10)

    dorking_type_var.trace('w', toggle_dork_entry)
    dork_entry.bind('<KeyRelease>', update_suggestions)
    dork_entry.bind('<Return>', select_suggestion)  # Move cursor to the end on Enter key

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description='GoogleDoc Tool')
    parser.add_argument('target', metavar='TARGET', type=str, nargs='?', help='Target domain')
    parser.add_argument('-s', '--search-engine', type=str, choices=['Google', 'Bing', 'DuckDuckGo', 'Yahoo', 'Firefox', 'Shodan', 'Censys Search'], default='Google', help='Search engine to use (default: Google)')
    parser.add_argument('-d', '--dorks', type=str, nargs='+', help='Custom dorks to use')
    parser.add_argument('-a', '--automatic', action='store_true', help='Use predefined dorks automatically')
    parser.add_argument('-l', '--limit', type=int, help='Limit the number of dorks (for automatic mode)')
    parser.add_argument('--gui', action='store_true', help='Run the tool in GUI mode')
    args = parser.parse_args()

    if args.gui or not args.target:
        run_gui()
    else:
        target = args.target
        search_engine = args.search_engine
        if args.automatic:
            dorks = predefined_dorks[:args.limit] if args.limit else predefined_dorks
        else:
            dorks = args.dorks if args.dorks else []

        try:
            google_dork(target, search_engine, dorks, args.limit)
        except ValueError as e:
            print(f"Error: {e}")
            parser.print_help()

if __name__ == "__main__":
    main()
