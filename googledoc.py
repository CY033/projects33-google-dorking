import webbrowser
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
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

def google_dork(target, search_engine, dorks):
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
        url = f'{base_url}site:{target} {dork}'
        webbrowser.open_new_tab(url)

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
    print(help_message)

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
        dork_entry_label.pack(padx=10, pady=5)
        dork_entry.pack(padx=10, pady=10)
        dork_entry.focus()  # Set focus to the dork entry box
        dork_entry.event_generate('<Down>')  # Automatically show suggestions
    else:
        dork_entry_label.pack_forget()
        dork_entry.pack_forget()

root = tk.Tk()
root.title("GoogleDoc")

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

dorking_type_var = tk.StringVar(root)
dorking_type_var.set('Automatic')  # default value
dorking_type_label = tk.Label(root, text="Select dorking type:")
dorking_type_label.pack(padx=10, pady=5)

dorking_type_dropdown = tk.OptionMenu(root, dorking_type_var, 'Automatic', 'Manual')
dorking_type_dropdown.pack(padx=10, pady=5)
dorking_type_var.trace('w', toggle_dork_entry)

dork_entry_label = tk.Label(root, text="Enter your custom dork:")
dork_entry = ttk.Combobox(root, width=50)
dork_entry.bind('<KeyRelease>', update_suggestions)
dork_entry.bind('<<ComboboxSelected>>', select_suggestion)
dork_entry['values'] = predefined_dorks

button = tk.Button(root, text="Start Google Dorking", command=on_submit)
button.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
