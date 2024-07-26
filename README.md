# GoogleDoc

GoogleDoc is a simple tool for performing Google dorking on a specified target domain. 

## Features

- GUI for easy use
- Multiple Google dork queries
- Help option for command-line usage

## Usage

1. **Running the Tool:**
    - Run the `GoogleDoc` executable.
    - Enter the target domain and click "Start Google Dorking".

2. **Command-line Options:**
    - Run `GoogleDoc --help` to see the help message.
    - 

## Building from Source

To build the executable from the source, follow these steps:

1. Clone the repository:
    ```sh
     https://github.com/CY033/projects33-google-dorking.git
     cd googledoc
    ```
 
2. Run the following command to install requirements:
    ```sh
      pip install -r requirements.txt
    ```
3. Install `pyinstaller` if your system don't have Python installed then run this :
    ```sh
     pip install pyinstaller
    ```

5. The executable will be available in the `dist` directory.


# Run in GUI mode
   
 ```sh
    python3  googledoc.py -g
   ```
 ##                     OR 
```sh
      python3  googledoc.py --gui
   ```

## CLI mode
1. Clone the repositor:
    ```sh
      https://github.com/CY033/projects33-google-dorking.git
       ```
#   
   ```sh
     cd projects33-google-dorking.git
   ```
     
2. Open help manu:
```sh
   python googledoc.py --help
   ```
 ##                     OR 
```sh
     python googledoc.py -h
   ```

3. Run in CLI mode, used your own Dork or custom:
    ```sh
     python3 googledoc.py -t < targer domain or url > -s < select search engine >  -d < dork >   

    ```

4. Use dork file for Dorking :
    ```sh
     python3  googledoc.py -t <target> -s <Search_engien_name>  -f <file path name or path > 
    ```
5. All the result are  save in output directory  


## Important Notes

- Ensure you have permission to perform Google dorking on the specified target.
- This tool is intended for educational and authorized security testing purposes only. Unauthorized use is illegal and unethical.
- Before start Dorking open firfox or any browser.



