from registry.registry_module.execute import *
from filescrap.fileForensic import *
from webscrap.scraper import *
from historyscrap.ExtractBrowserHistory import *
from historyscrap.GeneratingTimeLine import *
from itertools import zip_longest


def menu():
    print("")
    print("*************TEAM DF**************")
    print("************MAIN MENU**************")
    choice = input("""
    A: Extract Registry
    B: File Scrap
    C: Analyze Browser History
    D: Exit

    Enter your choice: """)

    if choice == "A" or choice == "a":
        regmain()
        menu()

    elif choice == "B" or choice == "b":
        directoryPath = input('Please input the directory path: ')
        directoryPath = checkPathValidity(directoryPath)
        targetExt = input('Please input a target extension (Eg. [.pdf] - leave blank if you want all filetypes): ')
        outputFileName = input('Please input the output file name (without extension): ')
        outputFileName = checkNull(outputFileName)
        retrieveAllTargetFile(directoryPath, targetExt,
                              outputFileName)  # User input for the whole program to work
        menu()

    elif choice == "C" or choice == "c":
        write_browserhistory_csv()
        setup()
        checkPunkt()
        url_list = openURLCSV("general_history2.csv")
        failed_and_success_list = scrapeURL(url_list)
        article_content_list = failed_and_success_list[0]
        failed_urls = failed_and_success_list[1]
        d = urlAnalyze(url_list, article_content_list)
        f = failedURL(failed_urls)
        export_data = zip_longest(*d, fillvalue='')
        failed_data = zip_longest(*f, fillvalue='')
        resultsCSV(export_data, failed_data)
        menu()

    elif choice == "D" or choice == "d":
        exit()
    else:
        print("Invalid input, please try again")
        menu()


menu()
