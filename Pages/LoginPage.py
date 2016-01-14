from page_objects import PageElement, PageObject
from utilities import wait_for_window

class LoginPage(PageObject):
    textUsername = PageElement(id_="login")
    textPassword = PageElement(id_="password")
    buttonLogin = PageElement(id_="btn_login")


    def login_as(self, username, password):
        self.textUsername.clear()
        self.textUsername.send_keys(username)
        self.textPassword.clear()
        self.textPassword.send_keys(password)
        self.buttonLogin.click()
        wait_for_window(self.w, "Time Tracker - Time")
        from HoursPage import HoursPage
        return HoursPage(self.w)

    def stop(self):
        self.w.quit()