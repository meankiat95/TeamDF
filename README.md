Documentation for Codebase
 ========================
 
This project has four package namely:
·     Registry
.     filescrap
.     historyscrap
.     webscrap


Libraries required for the program
========================

* pandas 
* json 
* xlsxwriter
* os 
* Winreg
* urllib 
* nltk 
* BeautifulSoup4 
* csv 
* flashtext 
* Pypdf2 
* textract 
* Pillow / PIL 
* datetime 
* sqlite3 
* sys 
* Itertools 
* collections (counter) 
* plotly 
* Tldextract 
Classification and listing of extensions require the help of 3rd Party python libraries, therefore it is important for you to download them via the python terminal. 
You can type the following command to install them:

=====

Pip install PyPDF2    [Installation for PyPDF2]

Pip install textract  [Installation for Textract]

=====

Registry
=====

The registry package have 5 modules:
1. registry_save.py - Functionalities for creating a backup copy of a specified registry
2.  registry.py - This module has core functionalities of extracting data from registry.
3. tabulate_data.py - It tabulates the data extracted in json format and writes it in excel format.
4. execute.py – Executes the program of data extraction
5. config.json – Configures the file paths required

File Scraping
========

File scraping package have 2 modules:

1. catFunction.py - This file has functionalities to categorise certain files into category, depending on the file contents
2. fileForensics.py - This file has functionalities of walk through the file directories, identifying target files, and saved output to CSV files

Analyse Browser History
================

Analyse Browser History uses 2 packages namely:

1. Historyscrap
   1. ExtractBrowserhistory.py - Extracting browser history and output saved into csv file
   2. GeneratingTimeLine.py - Generation of graph with history data obtained from the browser. 
2. Webscrap
   1. Scraper - to parse the url to extract readable content and classify the urls into categories after analysing the content. 
   2. Stopword.py - contains lists of words which are used in filtering out commonly used words and short function words from the extracted content to improve categorization performance and accuracy. 
   
 
Changes to make before running the program
======================
+++Registry module+++

Step 1. Configure the config.json file as per your system’s file path. You can find config.json file under the registry_module folder. The paths to find your folders in the registry should be the same, if it is not, please make the necessary changes. In the config.json file, you will need to configure one path.

*  Data_file_path        
o   The data_file_path is the path where you want to output your excel sheet once you run the program. The data_file_path can be found in the config.json file.
o   Make the following changes to configure your path based on where your  data_registry folder is at. When code is executed, the data will be extracted and stored into registry_data.xlsx or any name that user wants to change it to.
o   The file path should look similar to this:
"data_file_path": "C:\\Users\\Noah\\Desktop\\teamDF2\\registry\\registry_module\\data_registry\\registry_data.xlsx"
 
Step 2. Make the following changes in file “execute.py”:
* Change the filepath highlighted in the code snippet below to where your config.json file path is located at: 
with open(r'C:\Users\Noah\Desktop\teamDF2\registry\registry_module\config.json') as f:
After successfully running the Extract Registry Option in the menUI.py, your tabulated registry data will be extracted into an excel file in the specified file path (“data_file_path” value in config.json file).
