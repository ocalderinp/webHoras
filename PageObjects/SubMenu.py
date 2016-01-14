from page_objects import PageElement, PageObject
from utilities import wait_for_window

class SubMenu(PageObject):
    timeLink = PageElement("Time")
    reportsLink = PageElement("Reports")
    chartsLink = PageElement("Charts")
    projectsLink = PageElement("Projects")
    userLink = PageElement("Users")

    def go_to_reports(self):
        self.reportsLink.click()
        #from ReportsPage import ReportsPage
        #return ReportsPage(self.w)
