import time
import unittest


from Pages.utilities import get_page, arg_parse, get_tasks_list


class TestFillHour(unittest.TestCase):

    def setUp(self):
        self.page = get_page(myRemote, myBrowser, myUrl)

    def test_fill_hour(self):
        hours_page = self.page.login_as("oscar.calderin", "oscar.calderin")
        tasks = get_tasks_list("horas.xls")
        for task in tasks:
            print("taskkkkkk: " + str(task))
            hours_page.fillHours(task[0], task[1], tasks[2])


    def tearDown(self):
        time.sleep(1)
        self.page.stop()

if __name__ == "__main__":
    import sys
    myRemote, myBrowser, myUrl = arg_parse(sys.argv)
    unittest.main()
