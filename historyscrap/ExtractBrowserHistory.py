import csv
import os
import sqlite3
import sys



def get_username():
    """
    Get username of the computers
    """
    drives = input("Please input the drive (e.g. C): ")
    username = input("Please enter user profile name (case-sensitive & space sensitive): ")
    name = drives +":\\"  +"Users"+ "\\"+ username
    while not os.path.exists(name):
        print("Invalid user name found.")
        drives = input("Please input the drive (e.g. C): ")
        username = input("Please enter user profile name (case-sensitive & space sensitive): ")
        name = drives + ":\\" + "Users" + "\\" + username
    return name

def get_database_paths():
    """
    Get paths to the database of browsers and store them in a dictionary.
    It returns a dictionary: its key is the name of browser in str and its value is the path to database in str.
    Only for chrome and firefox
    """

    browser_path_dict = dict()

    User_path = get_username()
    abs_chrome_path = os.path.join(User_path, 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'History')
    abs_firefox_path = os.path.join(User_path, 'AppData', 'Roaming', 'Mozilla', 'Firefox', 'Profiles')

        # it creates string paths to broswer databases
    if os.path.exists(abs_chrome_path):
        browser_path_dict['chrome'] = abs_chrome_path
    if os.path.exists(abs_firefox_path):
        firefox_dir_list = os.listdir(abs_firefox_path)
        for f in firefox_dir_list:
            if f.find('.default') > 0:
                abs_firefox_path = os.path.join(abs_firefox_path, f, 'places.sqlite')
        if os.path.exists(abs_firefox_path):
            browser_path_dict['firefox'] = abs_firefox_path
    return browser_path_dict


def get_browserhistory() :
    """Get the user's browsers history by using sqlite3 module to connect to the dabases.
       It returns a dictionary: its key is a name of browser in str and its value is a list of
       tuples, each tuple contains four elements, including url, title, and visited_time.
       Example
       -------
    """
    # browserhistory is a dictionary that stores the query results based on the name of browsers.
    browserhistory = {}

    # call get_database_paths() to get database paths.
    paths2databases = get_database_paths()

    for browser, path in paths2databases.items():
        try:
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            _SQL = ''
            # SQL command for browsers' database table
            if browser == 'chrome':
                _SQL = """SELECT url, title, datetime((last_visit_time/1000000)-11644473600, 'unixepoch', 'localtime') 
                                    AS last_visit_time FROM urls ORDER BY last_visit_time DESC"""
            elif browser == 'firefox':
                _SQL = """SELECT url, title, datetime((visit_date/1000000), 'unixepoch', 'localtime') AS visit_date 
                                    FROM moz_places INNER JOIN moz_historyvisits on moz_historyvisits.place_id = moz_places.id ORDER BY visit_date DESC"""
            else:
                pass
            # query_result will store the result of query
            query_result = []
            try:
                cursor.execute(_SQL)
                query_result = cursor.fetchall()
                print("This may take awhile. Please wait.")
            except sqlite3.OperationalError:
                print('* Notification * ')
                print('Please Completely Close ' + browser.upper() + ' Window')
            except Exception as err:
                print(err)
            # close cursor and connector
            cursor.close()
            conn.close()
            # put the query result based on the name of browsers.
            browserhistory[browser] = query_result
        except sqlite3.OperationalError:
            print('* ' + browser.upper() + ' Database Permission Denied.')
    return browserhistory


def write_browserhistory_csv():
    """It writes csv files that contain the browser history in
    the current working directory. It will writes into one common csv files called "general_history.csv ."""
    browserhistory = get_browserhistory()
    if os.path.exists('general_history.csv'):
        os.remove('general_history.csv')

    for browser, history in browserhistory.items():
        if os.path.exists('general_history.csv'):
            with open('general'+'_history.csv', mode ='a', encoding='utf-8',newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',',
                                        quoting=csv.QUOTE_ALL)
                for data in history:
                    csv_writer.writerow(data)
        else:
            with open('general' + '_history.csv', mode='w', encoding='utf-8', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_ALL)
                csv_writer.writerow(['URL','Title','DateTime'])
                for data in history:
                    csv_writer.writerow(data)

