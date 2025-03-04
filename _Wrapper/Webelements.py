import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from drivers.webdrivers import webdrivers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from _Wrapper import Helper


class Webelement(webdrivers):

    @classmethod
    def wait(cls,timeout: int=10):
        return WebDriverWait(cls._browser,timeout)

    @classmethod
    def wait_for_element_visible(cls, element_locator):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls.wait().until(EC.visibility_of_element_located(element_locator))  # Use presence if visibility is not required

    @classmethod
    def wait_for_all_elements_visible(cls, elements_locator):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        return cls.wait().until(EC.visibility_of_all_elements_located( elements_locator))

    @classmethod
    def findElement(cls, element_locator):

        """
        returns web element for given element locator

        :return: webelement
        """
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")

        if cls.wait_for_element_visible(element_locator):
            return cls._browser.find_element(*element_locator)
        else: print("element not available")

    @classmethod
    def findElements(cls, element_locator):

        """
        returns web element for given element locator

        :return: webelement
        """
        if not cls._browser:
            raise ValueError("Browser not initialized. Call set_browser() first.")
        cls.wait_for_all_elements_visible(element_locator)
        return cls._browser.find_elements(*element_locator)

    @classmethod
    def click_element(cls,element_locator):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call pytest_start_browser() first.")
        element=cls.wait_for_element_visible(element_locator)
        element.click()

    @classmethod
    def is_element_displayed(cls,element_locator):
        if not cls._browser:
            raise ValueError("Browser not initialized. Call pytest_start_browser() first.")
        element = cls.findElement(element_locator)
        return  element


    @classmethod
    def verify_page_refresh(cls,element_locator):
        """
            Verifies if clicking the logo refreshes the page using window.onbeforeunload.

            Steps:
            1. Injects a JavaScript listener to track page refresh.
            2. Clicks the logo.
            3. Waits for the page reload.
            4. Checks if the page refreshed.

            :param driver: Selenium WebDriver instance
            :param logo_xpath: XPath of the logo element
            :param wait_time: Time to wait for page reload (default: 2 seconds)
            :return: True if the page refreshed, False otherwise
            """
        # Inject JavaScript to set a flag before the page unloads
        cls._browser.execute_script("""
                window.onbeforeunload = function() { 
                    localStorage.setItem('page_refreshed', 'true'); 
                };
            """)

        # tirgger a potential refresh
        element=cls.findElement(element_locator)
        element.click()

        # wait for the page to refresh
        time.sleep(3)

        # check local storage for refresh dedection
        is_refreshed = cls._browser.execute_script("return localStorage.getItem('page_refreshed') === 'true';")

        # Reset the flag after checking
        cls._browser.execute_script("localStorage.removeItem('page_refreshed');")

        if is_refreshed:
            print("✅ Page refreshed successfully after clicking the logo.")
            return True
        else:
            print("❌ Page did not refresh.")
            return False
    @classmethod
    def page_title(cls):
        return cls._browser.title
    
    @classmethod
    def verify_new_tab(cls, element_locator=None):

        # get the no of tabs before clicking
        initial_tabs=cls._browser.window_handles

        # click the hyperlink (expected to open a new tab)
        element=cls.findElement(element_locator)
        element.click()

        #wait for the tab to open
        cls.wait().until(EC.new_window_is_opened(initial_tabs))

        new_tabs=cls._browser.window_handles
        if len(new_tabs) > len(initial_tabs):
            print("✅ New tab opened successfully.")

            #switch to new tab

            cls.switch_tab(-1)
            print(cls.page_title())

            # return the new tap page title

            return cls.page_title()
        else:
            print("❌ No new tab opened.")
            return "No new tab opened "

    @classmethod
    def close_current_tab(cls):
        cls._browser.close()

    @classmethod
    def switch_tab(cls,tab):
        handles=cls._browser.window_handles
        print(handles)
        cls._browser.switch_to.window(handles[int(tab)])

   
    @classmethod
    def mousehover(cls,element_locator):
        element=cls.findElement(element_locator)
        cls.mouse.move_to_element(element).perform()

    @classmethod
    def gettext(cls,element_locator):
        try:
            element=cls.findElement(element_locator)
            if element:
                return element.text
            else:
                print(f"❌ Element {element_locator} not found!")
            return None
        except Exception as e:
            print(f"⚠️ Error while getting text from {element_locator}: {e}")
            return None



    @classmethod
    def send_text(cls,element_locator,text):
        element=cls.findElement(element_locator)
        element.click()
        element.send_keys(text)
        time.sleep(2)
        element.send_keys(Keys.DOWN)
        time.sleep(2)
        element.send_keys(Keys.ENTER)

    @classmethod
    def set_date(cls,date):
        date, month_year = Helper.get_date_of_travel(date)
        element_found = False
        while element_found == False:
            try:
                # Try to locate the element with the provided XPath
                element = Webelement.findElement((By.XPATH,f"//div[@class='DayPicker-Caption']/div[text()='{month_year}']"))
                element_found = True  # Return True if the element is found

            except Exception as e:
                # If the element is not found, print an error and continue to the next iteration
                print(f"Element not found, retrying... {e}")
                next_month = Webelement.findElement((By.XPATH,"//span[@role='button' and @class='DayPicker-NavButton DayPicker-NavButton--next']"))
                cls.click_element(next_month)

        Webelement.click_element((By.XPATH,f"//div[@role='gridcell' and @class='DayPicker-Day' and @aria-label='{date}']"))
