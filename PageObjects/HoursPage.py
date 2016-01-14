from page_objects import PageElement, PageObject
from selenium.webdriver.support.ui import Select


class HoursPage(PageObject):
    selectProject = PageElement(id_="project")
    startText = PageElement(id_="start")
    finishText = PageElement(id_="finish")
    durationText = PageElement(id_="duration")
    todayLink = PageElement(id_="today_link")
    buttonSubmit = PageElement(id_="btn_submit")
    buttonStart = PageElement(id_="start")
    buttonFinish = PageElement(id_="start")
    tableCalendar = PageElement(xpath="html/body/table/tbody/tr[1]/td/form/table[1]/tbody/tr/td[2]/table/tbody/tr/td/center/table")
    nextLink = PageElement(link_text=">>>")
    backLink = PageElement(link_text="<<<")
    dateHeader = PageElement(class_name="CalendarHeader")
    noteText = PageElement(id_="note")

    def fill_hours(self, project, hours, notes):
        self.go_today()
        self.set_project(project)
        self.set_hours(hours)
        self.set_notes(notes)
        self.submit()
        self.logout()

    def set_start_hour(self):
        self.buttonStart.click()

    def set_finish_hour(self):
        self.buttonFinish.click()

    def get_start_hour(self):
        self.buttonStart.text

    def get_finish_hour(self):
        self.buttonFinish.text

    def set_calendar_date(self, date):
        new_date = date.split("/")
        month_year = self.get_month_and_year(new_date[1], new_date[2])
        while month_year != self.dateHeader.text:
            self.go_next()
        days = self.tableCalendar.fin

    def get_month_and_year(self, month, year):
        if month == "01":
            new_month = "January"
        elif month == "02":
            new_month = "February"
        elif month == "03":
            new_month = "March"
        elif month == "04":
            new_month = "April"
        elif month == "05":
            new_month = "May"
        elif month == "06":
            new_month = "June"
        elif month == "07":
            new_month = "July"
        elif month == "08":
            new_month = "August"
        elif month == "09":
            new_month = "September"
        elif month == "10":
            new_month = "October"
        elif month == "11":
            new_month = "November"
        elif month == "12":
            new_month = "December"
        return new_month + " " + year

    def go_next(self):
        self.nextLink.click()

    def go_back(self):
        self.backLink.click()

    def go_today(self):
        self.todayLink.click()

    def set_hours(self, hours):
        self.durationText.clear()
        self.durationText.send_keys(hours)

    def set_notes(self, notes):
        self.noteText.clear()
        self.noteText.send_keys(notes)

    def submit(self):
        self.buttonSubmit.click()

    def logout(self):
        from MainMenu import MainMenu
        MainMenu(self.w).logout()

    def set_project(self, project):
        select = Select(self.selectProject)
        select.select_by_visible_text(project)

    def simple_fill(self, project):
        self.go_today()
        self.set_project(project)
        self.set_hours("8:00")
        self.submit()
        self.logout()

    def go_to_profile(self):
        menu = self.get_sub_menu()
        menu.go_to_reports()

    def get_sub_menu(self):
        from SubMenu import SubMenu
        return SubMenu(self.w)







