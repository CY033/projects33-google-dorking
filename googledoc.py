import webbrowser
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, scrolledtext
import argparse
import time
from datetime import datetime
import os
from ttkthemes import ThemedTk
import ttkbootstrap as ttkb

banner = '''
               ______                  __          ____             __            
              / ____/___  ____  ____ _/ /__       / __ \____  _____/ /_____  _____
             / / __/ __ \/ __ \/ __ `/ / _ \     / / / / __ \/ ___/ //_/ _ \/ ___/
            / /_/ / /_/ / /_/ / /_/ / /  __/    / /_/ / /_/ / /  / ,< /  __/ /    
            \____/\____/\____/\__, /_/\___/    /_____/\____/_/  /_/|_|\___/_/     
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

def save_results_to_file(target, search_engine, dorks, file_path, append=False):
    mode = 'a' if append else 'w'

    try:
        with open(file_path, mode) as f:
            for dork in dorks:
                f.write(f'{dork}\n')
        if append:
            messagebox.showinfo("Append Successful", f"Results appended to '{file_path}' successfully!")
        else:
            messagebox.showinfo("Save Successful", f"Results saved to '{file_path}' successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save results: {str(e)}")

def update_history(target, search_engine, dorks, history_text, append=False):
    # Get current time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    # Prepare history entry with separators
    if not append:
        history_entry = f"S.No        Dork                                            Date                Time\n"
    else:
        history_entry = ""

    # Load existing history if append mode
    if append and history_text:
        existing_text = history_text.get('1.0', 'end-1c')
        if existing_text.strip():
            history_entry = existing_text.rstrip() + '\n'  # Remove trailing newline before appending new history

    # Sequential numbering for S.No column
    start_idx = len(history_entry.strip().split('\n')) if append else 1
    for idx, dork in enumerate(dorks, start=start_idx):
        history_entry += f"{idx:<12}{dork:<48}{date_str:<20}{time_str}\n"  # Add space between Date and Time

    # Append or update history text widget
    if history_text:
        history_text.configure(state=tk.NORMAL)  # Enable editing
        history_text.delete('1.0', tk.END)  # Clear existing content
        history_text.insert(tk.END, history_entry)  # Add updated history
        history_text.configure(state=tk.DISABLED)  # Disable editing

    # Save history to file on tool close
    if not append:
        save_history_to_file(target, date_str, time_str, history_entry)

def save_history_to_file(target, date_str, time_str, history_entry):
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)

    file_name = f"{target}_{date_str}_{time_str}.txt"
    file_path = os.path.join(output_dir, file_name)

    try:
        with open(file_path, 'w') as f:
            f.write(history_entry)
        messagebox.showinfo("History Saved", f"History saved to '{file_path}' successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save history: {str(e)}")

def run_gui():
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

                update_history(target, search_engine, dorks, history_text, append=True)
                update_suggestions(target, search_engine, dorks)
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
            --append        Append results to an existing file without deleting its contents.
        """
        messagebox.showinfo("Help", help_message)

    def update_suggestions(target, search_engine, dorks):
        # Update suggestion for target URL
        suggestions_text.delete('1.0', tk.END)  # Clear existing suggestions
        suggestions_text.insert(tk.END, f"Suggestions for {target}:\n")
        for i, dork in enumerate(predefined_dorks, start=1):
            suggestions_text.insert(tk.END, f"{i}. {dork}\n")

    def toggle_dorking_options(event=None):
        if dorking_type_var.get() == "Automatic":
            manual_entry_frame.grid_forget()
            file_entry_frame.grid_forget()
        elif dorking_type_var.get() == "Manual":
            manual_entry_frame.grid(row=6, column=0, sticky=tk.W, pady=10)
            file_entry_frame.grid_forget()
        elif dorking_type_var.get() == "From File":
            manual_entry_frame.grid_forget()
            file_entry_frame.grid(row=6, column=0, sticky=tk.W, pady=10)
        else:
            manual_entry_frame.grid_forget()
            file_entry_frame.grid_forget()

    def on_closing():
        if messagebox.askyesno("Save History", "Do you want to save the dorking history?"):
            target = entry.get().strip()
            search_engine = search_engine_var.get()
            dorks = []

            if dorking_type_var.get() == "Automatic":
                limit = simpledialog.askinteger("Limit", "Enter the number of dorks to perform:", minvalue=1, maxvalue=len(predefined_dorks))
                dorks = predefined_dorks[:limit]
            elif dorking_type_var.get() == "Manual":
                custom_dork = dork_entry.get().strip()
                if custom_dork:
                    dorks = [custom_dork]
            elif dorking_type_var.get() == "From File":
                file_path = file_entry.get().strip()
                try:
                    dorks = load_dorks_from_file(file_path)
                except ValueError as e:
                    messagebox.showerror("Error", str(e))
                    return

            if target and search_engine and dorks:
                update_history(target, search_engine, dorks, history_text, append=False)

        root.destroy()

    root = ThemedTk(theme="bootstrap")
    root.title("Google Dorking Tool")

    style = ttkb.Style()
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TButton', font=('Helvetica', 12))
    style.configure('TEntry', font=('Helvetica', 12))
    style.configure('TCombobox', font=('Helvetica', 12))

    # Main frame
    main_frame = ttkb.Frame(root, padding="20 20 20 20", style='TFrame')
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttkb.Label(main_frame, text="Enter target domain or URL:", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=10)
    entry = ttkb.Entry(main_frame, width=50, style='TEntry')
    entry.grid(row=1, column=0, pady=10)

    ttkb.Label(main_frame, text="Select search engine:", style='TLabel').grid(row=2, column=0, sticky=tk.W, pady=10)
    search_engine_var = tk.StringVar(root)
    search_engine_dropdown = ttkb.Combobox(main_frame, textvariable=search_engine_var,
                                           values=['Google', 'Bing', 'DuckDuckGo', 'Yahoo', 'Firefox', 'Shodan', 'Censys Search'], state='readonly', style='TCombobox')
    search_engine_dropdown.grid(row=3, column=0, pady=10)

    ttkb.Label(main_frame, text="Select dorking type:", style='TLabel').grid(row=4, column=0, sticky=tk.W, pady=10)
    dorking_type_var = tk.StringVar(root)
    dorking_type_var.set('Automatic')  # default value
    dorking_type_dropdown = ttkb.Combobox(main_frame, textvariable=dorking_type_var,
                                          values=['Automatic', 'Manual', 'From File'], state='readonly', style='TCombobox')
    dorking_type_dropdown.grid(row=5, column=0, pady=10)

    # Manual and File entry frames
    manual_entry_frame = ttkb.Frame(main_frame, padding="0 10 0 0", style='TFrame')
    file_entry_frame = ttkb.Frame(main_frame, padding="0 10 0 0", style='TFrame')

    ttkb.Label(manual_entry_frame, text="Enter custom dork:", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=10)
    dork_entry = ttkb.Entry(manual_entry_frame, width=50, style='TEntry')
    dork_entry.grid(row=1, column=0, pady=10)

    ttkb.Label(file_entry_frame, text="Enter file path:", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=10)
    file_entry = ttkb.Entry(file_entry_frame, width=50, style='TEntry')
    file_entry.grid(row=1, column=0, pady=10)

    # Initial showing of manual entry frame
    toggle_dorking_options()

    dorking_type_dropdown.bind('<<ComboboxSelected>>', lambda event: toggle_dorking_options())

    ttkb.Button(main_frame, text="Start Google Dorking", style='TButton', command=on_submit).grid(row=7, column=0, pady=20)

    # History and suggestions frames
    history_frame = ttkb.Frame(root, padding="20 20 20 20", style='TFrame')
    history_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)

    ttkb.Label(history_frame, text="Dorking History:", style='TLabel').grid(row=0, column=0, sticky=tk.W, pady=10)
    history_text = scrolledtext.ScrolledText(history_frame, wrap=tk.WORD, width=90, height=25, font=('Helvetica', 12))  # Increased width and height
    history_text.grid(row=1, column=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
    history_text.configure(state=tk.DISABLED)  # Initially disable editing

    # Add column headers to history box
    headers = "S.No        Dork                                            Date                Time\n"
    history_text.configure(state=tk.NORMAL)
    history_text.insert(tk.END, headers)
    history_text.configure(state=tk.DISABLED)

    ttkb.Label(history_frame, text="Suggestions:", style='TLabel').grid(row=2, column=0, sticky=tk.W, pady=10)
    suggestions_text = scrolledtext.ScrolledText(history_frame, wrap=tk.WORD, width=50, height=5, font=('Helvetica', 12))
    suggestions_text.grid(row=3, column=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
    update_suggestions("", "", predefined_dorks)  # Initially update suggestions

    ttkb.Button(history_frame, text="Help", style='TButton', command=show_help).grid(row=4, column=0, pady=20)

    # Bind close event to save history
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Set window size
    root.geometry("1300x750")

    root.mainloop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Google Dorking Tool")
    parser.add_argument("-g", "--gui", action="store_true", help="Run in GUI mode (default if no arguments provided)")
    parser.add_argument("-t", "--target", type=str, help="Target domain or URL")
    parser.add_argument("-s", "--search-engine", type=str, choices=['Google', 'Bing', 'DuckDuckGo', 'Yahoo', 'Firefox', 'Shodan', 'Censys Search'], help="Search engine to use")
    parser.add_argument("-d", "--dorks", nargs='+', type=str, help="List of dorks")
    parser.add_argument("-f", "--file-path", type=str, help="File containing dorks")
    parser.add_argument("--append", action="store_true", help="Append results to an existing file")

    args = parser.parse_args()

    if args.gui or (not args.target and not args.dorks and not args.file_path):
        run_gui()
    else:
        try:
            if args.file_path:
                dorks = load_dorks_from_file(args.file_path)
            else:
                dorks = args.dorks

            google_dork(args.target, args.search_engine, dorks)
            print("Google Dorking completed successfully!")

            if args.file_path:
                save_results_to_file(args.target, args.search_engine, dorks, args.file_path, append=args.append)

            # Update history if GUI was not used
            update_history(args.target, args.search_engine, dorks, None, append=args.append)

        except ValueError as e:
            print(f"Error: {str(e)}")
