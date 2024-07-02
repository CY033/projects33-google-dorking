import requests
import tkinter as tk
from tkinter import messagebox
import sys
import os
from bs4 import BeautifulSoup

banner = ''' 
 
               ______                  __          ____             __            
              / ____/___  ____  ____ _/ /__       / __ \____  _____/ /_____  _____
             / / __/ __ \/ __ \/ __ `/ / _ \     / / / / __ \/ ___/ //_/ _ \/ ___/
            / /_/ / /_/ / /_/ / /_/ / /  __/    / /_/ / /_/ / /  / ,< /  __/ /    
            \____/\____/\____/\__, /_/\___/    /_____/\____/_/  /_/|_|\___/_/     
                             /____/                                                 

    Made By: Musharraf khan (github.com/Musharraf33)
'''




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
        f'site:{target} "password filetype:txt"',
        f'site:{target} "username filetype:txt"',
        f'site:{target} "login credentials filetype:xlsx"',
        f'site:{target} "site administration"',
        f'site:{target} "sensitive filetype:pdf"',
        f'site:{target} "confidential filetype:doc"',
        f'site:{target} "project plan filetype:mpp"',
        f'site:{target} "business plan filetype:pdf"',
        f'site:{target} "strategic plan filetype:pdf"',
        f'site:{target} "budget filetype:xls"',
        f'site:{target} "financial statements filetype:pdf"',
        f'site:{target} "board meeting minutes filetype:pdf"',
        f'site:{target} "contact list filetype:xls"',
        f'site:{target} "email list filetype:xls"',
        f'site:{target} "internal contact filetype:pdf"',
        f'site:{target} "phone list filetype:pdf"',
        f'site:{target} "telephone directory filetype:xls"',
        f'site:{target} "internal memo filetype:doc"',
        f'site:{target} "policy filetype:pdf"',
        f'site:{target} "procedure filetype:pdf"',
        f'site:{target} "manual filetype:pdf"',
        f'site:{target} "handbook filetype:pdf"',
        f'site:{target} "employee handbook filetype:pdf"',
        f'site:{target} "safety manual filetype:pdf"',
        f'site:{target} "security policy filetype:pdf"',
        f'site:{target} "disaster recovery plan filetype:pdf"',
        f'site:{target} "emergency plan filetype:pdf"',
        f'site:{target} "incident report filetype:pdf"',
        f'site:{target} "accident report filetype:pdf"',
        f'site:{target} "investigation report filetype:pdf"',
        f'site:{target} "audit report filetype:pdf"',
        f'site:{target} "compliance report filetype:pdf"',
        f'site:{target} "assessment report filetype:pdf"',
        f'site:{target} "risk assessment filetype:pdf"',
        f'site:{target} "risk management filetype:pdf"',
        f'site:{target} "health and safety filetype:pdf"',
        f'site:{target} "annual report filetype:pdf"',
        f'site:{target} "financial report filetype:pdf"',
        f'site:{target} "monthly report filetype:pdf"',
        f'site:{target} "project report filetype:pdf"',
        f'site:{target} "status report filetype:pdf"',
        f'site:{target} "progress report filetype:pdf"',
        f'site:{target} "performance report filetype:pdf"',
        f'site:{target} "evaluation report filetype:pdf"',
        f'site:{target} "final report filetype:pdf"',
        f'site:{target} "presentation filetype:ppt"',
        f'site:{target} "proposal filetype:pdf"',
        f'site:{target} "contract filetype:pdf"',
        f'site:{target} "agreement filetype:pdf"',
        f'site:{target} "terms and conditions filetype:pdf"',
        f'site:{target} "privacy policy filetype:pdf"',
        f'site:{target} "cookie policy filetype:pdf"',
        f'site:{target} "user manual filetype:pdf"',
        f'site:{target} "technical manual filetype:pdf"',
        f'site:{target} "installation guide filetype:pdf"',
        f'site:{target} "configuration guide filetype:pdf"',
        f'site:{target} "operation guide filetype:pdf"',
        f'site:{target} "user guide filetype:pdf"',
        f'site:{target} "reference manual filetype:pdf"',
        f'site:{target} "training manual filetype:pdf"',
        f'site:{target} "training guide filetype:pdf"',
        f'site:{target} "workbook filetype:pdf"',
        f'site:{target} "lesson plan filetype:pdf"',
        f'site:{target} "course material filetype:pdf"',
        f'site:{target} "presentation slides filetype:ppt"',
        f'site:{target} "training material filetype:pdf"',
        f'site:{target} "internal communication filetype:pdf"',
        f'site:{target} "communication plan filetype:pdf"',
        f'site:{target} "project charter filetype:pdf"',
        f'site:{target} "scope statement filetype:pdf"',
        f'site:{target} "requirements document filetype:pdf"',
        f'site:{target} "project schedule filetype:pdf"',
        f'site:{target} "project timeline filetype:pdf"',
        f'site:{target} "project budget filetype:pdf"',
        f'site:{target} "risk register filetype:pdf"',
        f'site:{target} "issue log filetype:pdf"',
        f'site:{target} "change log filetype:pdf"',
        f'site:{target} "lessons learned filetype:pdf"',
        f'site:{target} "project closure filetype:pdf"',
        f'site:{target} "project summary filetype:pdf"',
        f'site:{target} "project overview filetype:pdf"',
        f'site:{target} "business case filetype:pdf"',
        f'site:{target} "feasibility study filetype:pdf"',
        f'site:{target} "business plan filetype:pdf"',
        f'site:{target} "marketing plan filetype:pdf"',
        f'site:{target} "sales plan filetype:pdf"',
        f'site:{target} "operational plan filetype:pdf"',
        f'site:{target} "strategic plan filetype:pdf"',
        f'site:{target} "action plan filetype:pdf"',
        f'site:{target} "contingency plan filetype:pdf"',
        f'site:{target} "policy document filetype:pdf"',
        f'site:{target} "procedure document filetype:pdf"',
        f'site:{target} "standard operating procedure filetype:pdf"',
        f'site:{target} "work instruction filetype:pdf"',
        f'site:{target} "guideline document filetype:pdf"',
        f'site:{target} "framework document filetype:pdf"',
        f'site:{target} "charter document filetype:pdf"',
        f'site:{target} "code of conduct filetype:pdf"',
        f'site:{target} "code of ethics filetype:pdf"',
        f'site:{target} "compliance document filetype:pdf"',
        f'site:{target} "audit checklist filetype:pdf"',
        f'site:{target} "inspection checklist filetype:pdf"',
        f'site:{target} "assessment checklist filetype:pdf"',
        f'site:{target} "evaluation checklist filetype:pdf"',
        f'site:{target} "review checklist filetype:pdf"',
        f'site:{target} "verification checklist filetype:pdf"',
        f'site:{target} "validation checklist filetype:pdf"',
        f'site:{target} "report template filetype:pdf"',
        f'site:{target} "document template filetype:pdf"',
        f'site:{target} "form template filetype:pdf"',
        f'site:{target} "worksheet filetype:pdf"',
        f'site:{target} "spreadsheet filetype:pdf"',
        f'site:{target} "data sheet filetype:pdf"',
        f'site:{target} "data set filetype:pdf"',
        f'site:{target} "data report filetype:pdf"',
        f'site:{target} "data analysis filetype:pdf"',
        f'site:{target} "research report filetype:pdf"',
        f'site:{target} "research paper filetype:pdf"',
        f'site:{target} "thesis filetype:pdf"',
        f'site:{target} "dissertation filetype:pdf"',
        f'site:{target} "white paper filetype:pdf"',
        f'site:{target} "case study filetype:pdf"',
        f'site:{target} "business analysis filetype:pdf"',
        f'site:{target} "business research filetype:pdf"',
        f'site:{target} "industry analysis filetype:pdf"',
        f'site:{target} "market analysis filetype:pdf"',
        f'site:{target} "competitor analysis filetype:pdf"',
        f'site:{target} "swot analysis filetype:pdf"',
        f'site:{target} "pest analysis filetype:pdf"',
        f'site:{target} "risk analysis filetype:pdf"',
        f'site:{target} "financial analysis filetype:pdf"',
        f'site:{target} "economic analysis filetype:pdf"',
        f'site:{target} "policy analysis filetype:pdf"',
        f'site:{target} "regulatory analysis filetype:pdf"',
        f'site:{target} "compliance analysis filetype:pdf"',
        f'site:{target} "gap analysis filetype:pdf"',
        f'site:{target} "root cause analysis filetype:pdf"',
        f'site:{target} "impact analysis filetype:pdf"',
        f'site:{target} "process analysis filetype:pdf"',
        f'site:{target} "performance analysis filetype:pdf"',
        f'site:{target} "efficiency analysis filetype:pdf"',
        f'site:{target} "effectiveness analysis filetype:pdf"',
        f'site:{target} "benchmarking analysis filetype:pdf"',
        f'site:{target} "cost analysis filetype:pdf"',
        f'site:{target} "benefit analysis filetype:pdf"',
        f'site:{target} "decision analysis filetype:pdf"',
        f'site:{target} "scenario analysis filetype:pdf"',
        f'site:{target} "sensitivity analysis filetype:pdf"',
        f'site:{target} "variance analysis filetype:pdf"',
        f'site:{target} "trend analysis filetype:pdf"',
        f'site:{target} "forecasting analysis filetype:pdf"',
        f'site:{target} "statistical analysis filetype:pdf"',
        f'site:{target} "predictive analysis filetype:pdf"',
        f'site:{target} "quantitative analysis filetype:pdf"',
        f'site:{target} "qualitative analysis filetype:pdf"',
        f'site:{target} "descriptive analysis filetype:pdf"',
        f'site:{target} "inferential analysis filetype:pdf"',
        f'site:{target} "comparative analysis filetype:pdf"',
        f'site:{target} "data mining filetype:pdf"',
        f'site:{target} "machine learning filetype:pdf"',
        f'site:{target} "artificial intelligence filetype:pdf"',
        f'site:{target} "deep learning filetype:pdf"',
        f'site:{target} "neural network filetype:pdf"',
        f'site:{target} "algorithm filetype:pdf"',
        f'site:{target} "model filetype:pdf"',
        f'site:{target} "simulation filetype:pdf"',
        f'site:{target} "optimization filetype:pdf"',
        f'site:{target} "validation filetype:pdf"',
        f'site:{target} "verification filetype:pdf"',
        f'site:{target} "certification filetype:pdf"',
        f'site:{target} "accreditation filetype:pdf"',
        f'site:{target} "audit filetype:pdf"',
        f'site:{target} "assessment filetype:pdf"',
        f'site:{target} "evaluation filetype:pdf"',
        f'site:{target} "review filetype:pdf"'

    ]

    for dork in dorks:
        url = f'https://www.google.com/search?q={dork}'
        webbrowser.open_new_tab(url)

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
        # Create main  
        root = tk.Tk()
        root.title("GoogleDoc")

        # Display banner
        print(banner)

        # Create and place the widgets
        label = tk.Label(root, text="Enter the target domain (e.g., example.com):")
        label.pack(padx=10, pady=10)

        entry = tk.Entry(root, width=50)
        entry.pack(padx=10, pady=10)

        button = tk.Button(root, text="Start Google Dorking", command=on_submit)
        button.pack(padx=10, pady=10)

        # Run
        root.mainloop()
        
