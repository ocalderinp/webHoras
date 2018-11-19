import time
#import xlrd

import re
from selenium import webdriver

def get_page(remote, browser, url):
    if remote:
        return launch(webdriver.Remote("http://" + remote.lower() + ":4444/wd/hub",
                                       eval("webdriver.DesiredCapabilities." + browser.upper())), url)
    else:
        return launch(select_browser(browser[0].upper() + browser[1:]), url)


def launch(driver, url):
    from LoginPage import LoginPage
    driver.get(url)
    time.sleep(1)
    return LoginPage(driver)


def select_browser(my_browser):
    the_browser = eval('webdriver.' + my_browser + '(' + ')')
    the_browser.maximize_window()
    return the_browser


def arg_parse(alist):
    """
    This function parses the browser and url from the system arguments when running a test.
    The input arguments can be in any order and the browser name's first letter must be capitalized.    
    e.g. "python test.py user project hours notes browser[optional]"

    @param alist: the list from the system arguments.
    @return: A list of strings containing the Url and Browser. 
    """
    my_url = 'http://webhoras.abstracta.com.uy/login.php'
    my_browser = 'firefox'
    my_remote = ''
    my_user = ''
    my_project = ''
    my_hours = ''
    my_notes = ''
    cont = len(alist)
    print("listaaaa: " + len(alist).__str__())
    while len(alist) > 1:
        arg_var = alist.pop()
        print(str(arg_var))
        if cont == 6:
            my_browser = arg_var
            cont = cont - 1
        elif cont == 5:
            my_notes = arg_var
            cont = cont - 1
        elif cont == 4:
            my_hours = arg_var
            cont = cont - 1
        elif cont == 3:
            my_project = arg_var
            cont = cont - 1
        elif cont == 2:
            my_user = arg_var
            cont = cont - 1

    return my_remote, my_browser, my_url, my_user, my_project, my_hours, my_notes

    
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


# def get_tasks_list(filename):
#     data = xlrd.open_workbook(filename)
#     sheet = data.sheet_by_index(0)
#     rows = sheet.nrows
#     cols = sheet.ncols
#     tasks = []
#     for row in range(1, rows):
#         values = []
#         for cell in range(cols):
#             values.append(str(sheet.cell(row, cell).value))
#             tasks.append(values)
#     print("cant: " + len(tasks).__str__())
#     return tasks
