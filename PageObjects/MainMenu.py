from page_objects import PageElement, PageObject
from utilities import wait_for_window


class MainMenu(PageObject):
    logoutLink = PageElement(link_text="Logout")
    profileLink = PageElement(link_text="Profile")
    forumLink = PageElement(link_text="Forum")
    helpLink = PageElement(link_text="Help")

    def logout(self):
        self.logoutLink.click()
        wait_for_window(self.w, "Time Tracker - Login")
        from LoginPage import LoginPage
        return LoginPage(self.w)


    def go_to_profile(self):
        self.profileLink.click()
        wait_for_window(self.w, "Time Tracker - Profile")
        #from ProfilePage import ProfilePage
        #return ProfilePage(self.w)

    def go_to_forum(self):
        self.forumLink.click()

    def help(self):
        self.helpLink.click()