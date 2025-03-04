from selenium.webdriver.remote.webdriver import WebDriver

class DriverInitilization:

    _browser=None      # class variable to store the driver

    @classmethod
    def set_driver(cls,driver:WebDriver):

        """ verify that the driver passed is instance of web driver and assigns to the vaiable (_browser)"""
        if not isinstance(driver,WebDriver):
            raise  TypeError("INVALID driver type, it must be an instance of WebDriver")
        cls._browser=driver

    @property
    def browser(self):
        return self._browser

