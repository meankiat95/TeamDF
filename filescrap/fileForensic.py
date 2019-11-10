import os
from datetime import datetime
from os import scandir
from filescrap.catFunction import classification, get_labeled_exif, get_exif
from PyPDF2 import PdfFileReader
import textract


# List all files in a directory using scandir()
def checkPathValidity(filePath):
    while not os.path.exists(filePath):
        filePath=input("Invalid file path! \n Please input the directory input :")
    return filePath

def checkNull(userInput):
    while not userInput:
        userInput=input("No input file name detected. \n Please input the output file name (without extension): ")
    return userInput

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%Y-%m-%d %H:%M:%S')
    return formated_date


def sortResult(outputFile):
    inputFile = open(outputFile + 'Unsorted.csv', 'r')
    lineList = inputFile.readlines()
    lineList.sort()
    for line in lineList:
        #print(line)
        with open(outputFile + '.csv', 'w') as f:
            for line in lineList:
                lineList.sort()
                f.write(line)


def writeToFile(outputFileName, info, dirpath, entry, category):  # Write fileModifiedDetails and filePath w/ fileName
    with open(outputFileName + 'Unsorted.csv', 'a') as f:
        print(convert_date(info.st_mtime) + "," + str(category) + "," + dirpath + "/" + entry.name,
              file=f)


def eraseFileContent(fileName):
    with open(fileName, 'w') as f:
        print('', file=f)


def analyzePDF(outputFileName, info, dirpath, entry):
    dir = (os.path.join(dirpath, entry))
    formatDirPath = dirpath.replace("\\", "/")
    with open(entry, 'rb') as f:
        pdf = PdfFileReader(f, strict=False)

        number_of_pages = pdf.getNumPages()
        page = pdf.getPage(0)
        # print(page)
        # print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        # print(text)
        category = classification(text)
        # print(category)
        writeToFile(outputFileName, info, formatDirPath, entry, category)


def analyzeDocx(outputFileName, info, dirpath, entry):
    a = (os.path.join(dirpath, entry))
    #print(a)
    text = textract.process(a)
    formatText = text.rstrip()
    formattedAgain = str(formatText).replace("\n", " ")
    clean = str(formattedAgain).replace("\\n", " ")
    category=classification(clean)
    # print(category)
    writeToFile(outputFileName, info, dirpath, entry, category)


def analyzeJpg(outputFileName, info, dirpath, entry):
    dir = (os.path.join(dirpath, entry))
    dir = dir.replace("\\", "/")
    #print(dir)
    exif = get_exif(dir)
    if exif != None:
        detailedMeta = get_labeled_exif(exif)
        with open(outputFileName + 'Unsorted.csv', 'a') as fd:
            fd.write(convert_date(info.st_mtime) + "," + dir + "," + str(entry) + "," + (str(detailedMeta)).replace(",",
                                                                                                                    " "))
            fd.write('\n')
    else:
        with open(outputFileName + 'Unsorted.csv', 'a') as fd:
            fd.write(convert_date(info.st_mtime) + "," + dir + "," + str(entry) + "," + "None")
            fd.write('\n')


def analyzeTxt(outputFileName, info, dirpath, entry):
    a = (os.path.join(dirpath, entry))
    #print(a)
    readFile = open(a, "r",encoding="cp1252")
    text_from_txt = readFile.read()
    category = classification(text_from_txt)
    # print(category)
    writeToFile(outputFileName, info, dirpath, entry, category)


def retrieveAllTargetFile(targetPath, targetExt,
                          outputFileName):  # file traversing to reach out for all files beneath folder hierarchy
    eraseFileContent(
        outputFileName + 'Unsorted.csv')  # Clear content inside outputFile (if there is any content in output file)
    print ('Processing will take a while...')
    for dirpath, dirnames, files in os.walk(
            targetPath):  # Loop through all files within the directory tree 'C:/Users/great/Downloads'
        formatDirPath = dirpath.replace("\\", "/")
        # print(formatDirPath)
        # print(formatDirPath)# Print the directory system is accessing
        dir_entries = scandir(formatDirPath)
        for entry in dir_entries:  # Loop through each files to find the attributes
            if entry.is_file():
                info = entry.stat()  # Get the attributes of file (ModifiedDate etc)
                if (entry.name.endswith('.pdf') and targetExt == '.pdf') or (
                        entry.name.endswith('.pdf') and not targetExt):
                    print('pdf file detected')
                    analyzePDF(outputFileName, info, formatDirPath, entry)
                elif (entry.name.endswith('.docx') and targetExt == '.docx') or (
                        entry.name.endswith('.docx') and not targetExt):
                    print('docx file detected')
                    analyzeDocx(outputFileName, info, formatDirPath, entry)
                elif ((entry.name.endswith('.JPG') or entry.name.endswith('.jpg')) and (
                        targetExt == '.JPG' or targetExt == ".jpg")) or (entry.name.endswith('.jpg') and not targetExt):
                    # print('jpg detected')
                    analyzeJpg(outputFileName, info, formatDirPath, entry)
                elif (entry.name.endswith('.txt') and targetExt == '.txt') or (
                        entry.name.endswith('.txt') and not targetExt):
                    print('txt file detected')
                    analyzeTxt(outputFileName, info, formatDirPath, entry)
                elif entry.name.endswith(targetExt) or not targetExt:
                    print(targetExt + 'file detected')
                    writeToFile(outputFileName, info, formatDirPath, entry, '')
    print('All files are scanned and saved into '+outputFileName+'Unsorted.csv.')
    print('Results will now sort according to DateTime. Processing will take a while... ')
    sortResult(outputFileName)
    print('Sorted result has been successfully exported as '+outputFileName+'.csv')


    # for file_name in files:

    #   print('Filename:', file_name, file=f)


# retrieveAllTargetFile('C:/Program Files/', '.pdf',
#                       'pdfAnalyzeResult'); #User input for the whole program to work
