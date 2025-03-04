from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from _Wrapper.DriverInitilization import DriverInitilization


class webdrivers(DriverInitilization):
    
    @classmethod
    def start_browser(cls,browser):
        if browser.lower() == "chrome":
            options = ChromeOptions()
            options.add_experimental_option("detach", True)
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("--start-maximized")
            options.add_argument("--incognito")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--ignore-ssl-errors")
            #options.add_argument("--headless=new") 
            driver = webdriver.Chrome(options=options)
        else:
            raise ValueError(f"please check the browser entered Invalid browser name: {browser}")

        """creates an instance of ActionChains for performing advanced mouse and keyboard actions in Selenium."""
        cls.mouse=webdriver.ActionChains(driver)

        """captures all currently open browser window handles and assigns them to cls.window_handle."""
        cls.window_handle=driver.window_handles

        DriverInitilization().set_driver(driver)
    