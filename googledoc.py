import webbrowser
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
import argparse
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
    # Add more dorks as needed
]

def load_dorks_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            dorks = file.readlines()
        # Strip newline characters and empty lines
        dorks = [d.strip() for d in dorks if d.strip()]
        return dorks
    except FileNotFoundError:
        raise ValueError(f"File '{file_path}' not found.")
    except Exception as e:
        raise ValueError(f"Error loading dorks from file '{file_path}': {str(e)}")

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
    def save_results_to_file(target, search_engine, dorks):
        result_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if result_file:
            try:
                with open(result_file, 'w') as f:
                    for dork in dorks:
                        f.write(f'{dork}\n')
                messagebox.showinfo("Save Successful", f"Results saved to '{result_file}' successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save results: {str(e)}")

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
            elif dorking_type == "Manual":
                custom_dork = dork_entry.get().strip()
                if custom_dork:
                    dorks = [custom_dork]
                else:
                    messagebox.showwarning("Input Error", "Please enter a custom dork.")
                    return
            elif dorking_type == "From File":
                file_path = file_entry.get().strip()
                try:
                    dorks = load_dorks_from_file(file_path)
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
                    return
            else:
                messagebox.showwarning("Input Error", "Please select a dorking type.")
                return

            try:
                google_dork(target, search_engine, dorks)
                messagebox.showinfo("Success", "Google Dorking completed successfully!")
                
                if save_var.get():
                    save_results_to_file(target, search_engine, dorks)
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

    ttk.Label(main_frame, text="Enter the target domain or URL:", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=10)
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
    dorking_type_dropdown = ttk.Combobox(main_frame, textvariable=dorking_type_var, values=['Automatic', 'Manual', 'From File'], state='readonly', style='TCombobox')
    dorking_type_dropdown.grid(row=5, column=0, pady=10)

    dork_entry_label = ttk.Label(main_frame, text="Enter your custom dork:", style='TLabel')
    dork_entry = ttk.Combobox(main_frame, width=50, style='TCombobox')
    dork_entry['values'] = predefined_dorks

    file_entry_label = ttk.Label(main_frame, text="Enter path to dorks file:", style='TLabel')
    file_entry = ttk.Entry(main_frame, width=50, style='TEntry')

    def toggle_dork_entry(*args):
        if dorking_type_var.get() == "Manual":
            dork_entry_label.grid(row=6, column=0, sticky=tk.W, pady=10)
            dork_entry.grid(row=7, column=0, pady=10)
            dork_entry.focus()  # Set focus to the dork entry box
            dork_entry.event_generate('<Down>')  # Automatically show suggestions
        else:
            dork_entry_label.grid_forget()
            dork_entry.grid_forget()

    def toggle_file_entry(*args):
        if dorking_type_var.get() == "From File":
            file_entry_label.grid(row=6, column=0, sticky=tk.W, pady=10)
            file_entry.grid(row=7, column=0, pady=10)
            file_entry.focus()  # Set focus to the file entry box
        else:
            file_entry_label.grid_forget()
            file_entry.grid_forget()

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

    save_var = tk.BooleanVar()
    save_checkbox = ttk.Checkbutton(main_frame, text="Save results", variable=save_var, onvalue=True, offvalue=False, style='TCheckbutton')
    save_checkbox.grid(row=8, column=0, pady=10)

    ttk.Button(main_frame, text="Start Google Dorking", command=on_submit, style='TButton').grid(row=9, column=0, pady=10)
    ttk.Button(main_frame, text="Show Help", command=show_help, style='TButton').grid(row=10, column=0, pady=10)

    dorking_type_var.trace('w', toggle_dork_entry)
    dorking_type_var.trace('w', toggle_file_entry)
    dork_entry.bind('<KeyRelease>', update_suggestions)
    dork_entry.bind('<Return>', select_suggestion)  # Move cursor to the end on Enter key

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(description='GoogleDoc Tool')
    parser.add_argument('-u', '--url', metavar='URL', type=str, help='Domain or URL to perform Google dorking')
    parser.add_argument('-s', '--search-engine', type=str, choices=['Google', 'Bing', 'DuckDuckGo', 'Yahoo', 'Firefox', 'Shodan', 'Censys Search'], default='Google', help='Search engine to use (default: Google)')
    parser.add_argument('-d', '--dorks', type=str, nargs='+', help='Custom dorks to use')
    parser.add_argument('-a', '--automatic', action='store_true', help='Use predefined dorks automatically')
    parser.add_argument('-l', '--limit', type=int, help='Limit the number of dorks (for automatic mode)')
    parser.add_argument('-f', '--file', type=str, help='File containing dorks')
    parser.add_argument('-o', '--output', type=str, help='File name or file path to save the output')
    parser.add_argument('--gui', action='store_true', help='Run the tool in GUI mode')
    args = parser.parse_args()

    if args.gui:
        run_gui()
    elif args.url:
        target = args.url
        search_engine = args.search_engine
        if args.file:
            try:
                dorks = load_dorks_from_file(args.file)
            except ValueError as e:
                print(f"Error: {e}")
                parser.print_help()
                return
        elif args.automatic:
            dorks = predefined_dorks[:args.limit] if args.limit else predefined_dorks
        else:
            dorks = args.dorks if args.dorks else []

        if args.output:
            output_file = args.output
            with open(output_file, 'w') as f:
                try:
                    for dork in dorks:
                        f.write(f'{dork}\n')
                    google_dork(target, search_engine, dorks, args.limit)
                    print("Google Dorking completed successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
                    parser.print_help()
        else:
            try:
                google_dork(target, search_engine, dorks, args.limit)
                print("Google Dorking completed successfully!")
            except ValueError as e:
                print(f"Error: {e}")
                parser.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
