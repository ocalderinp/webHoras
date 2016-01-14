import time
import xlrd

import re
from selenium import webdriver

def get_page(remote, browser, url):
    """
    Execution ex:
    python SimpleTest.py http://frontend.heartflow.us chrome 10.6.66.92
    python SimpleTest.py http://frontend.heartflow.us chrome

    @param remote: remote server
    @param browser: the browser
    @param url: the url
    """
    if remote:
        return launch(webdriver.Remote("http://" + remote.lower() + ":4444/wd/hub",
                                       eval("webdriver.DesiredCapabilities." + browser.upper())), url)
    else:
        return launch(select_browser(webdriver, browser[0].upper() + browser[1:]), url)


def launch(driver, url):
    from LoginPage import LoginPage
    driver.get(url)
    time.sleep(1)
    return LoginPage(driver)


def select_browser(webdriver, my_browser):
    """
    This function launches a browser window of the specified type.

    @param my_browser: string for browser to be launched.
    @return: The Browser object.
    """
    the_browser = eval('webdriver.' + my_browser + '(' + ')')
    the_browser.maximize_window()
    return the_browser


def arg_parse(alist):
    """
    This function parses the browser and url from the system arguments when running a test.
    The input arguments can be in any order and the browser name's first letter must be capitalized.    
    e.g. "python test.py Chrome http://frontend.heartflow.us"

    @param alist: the list from the system arguments.
    @return: A list of strings containing the Url and Browser. 
    """
    my_url = 'http://127.0.0.1:8080'
    my_browser = 'PhantomJS'
    my_remote = ''
    while len(alist) > 1:
        arg_var = alist.pop()
        if re.compile('http').search(arg_var):
            my_url = arg_var
        elif re.compile('\d').search(arg_var):
            my_remote = arg_var
        else:
            my_browser = arg_var
    return my_remote, my_browser, my_url

    
def wait_for_window(myobj, msg):
    for i in range(60):
        try:
            if msg == myobj.title:
                break
        except:
            pass
        time.sleep(1)
    else:
        raise Exception("Time Out")


def wait_not_for_window(myobj, msg):
    for i in range(60):
        try:
            if msg != myobj.title:
                break
        except:
            pass
        time.sleep(1)
    else:
        raise Exception("Time Out")


def get_tasks_list(filename):
    data = xlrd.open_workbook(filename)
    sheet = data.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    tasks = []
    for row in range(1, rows):
        values = []
        for cell in range(cols):
            values.append(str(sheet.cell(row, cell).value))
            tasks.append(values)
    return tasks
