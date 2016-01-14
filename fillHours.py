import time
import unittest


from PageObjects.utilities import get_page, arg_parse


class TestFillHour(unittest.TestCase):

    def setUp(self):
        self.page = get_page(my_remote, my_browser, my_url)

    def test_fill_hour(self):
        hours_page = self.page.login_as(my_user, my_user)
        hours_page.fillHours(my_project, my_hours, my_notes)

    def tearDown(self):
        time.sleep(1)
        self.page.stop()

if __name__ == "__main__":
    import sys
    my_remote, my_browser, my_url, my_user, my_project, my_hours, my_notes = arg_parse(sys.argv)
    unittest.main()
