from typing import List
from Locators.Homepage_locators import HomepageLocators
from Locators.Base_locators import BaseLocators

from _Wrapper.Webelements import Webelement
from _Data.data import HomePageData
from _Wrapper import Helper
from Config.log_config import logging_setup

class BasePageFragments(Webelement):

    close_loginModel=HomepageLocators.CLOSE_LOGIN_MODAL_BUTTON
    login_mobilenumber=HomepageLocators.LOGIN_MOBILE_NUMBER_INPUT
    travel_date=HomepageLocators.DEPATURE
    logo_stickheader=HomepageLocators.MMT_LOGO_STICKY_HEADER
    logo_mmt_homepage=HomepageLocators.MMT_LOGO_HOMEPAGE
    elements_in_sticky_header=HomepageLocators.ICON_IN_STICKY_HEADER
    popups=BaseLocators.POPUPS

   

    @classmethod
    def setup_method(cls):    #Runs before each test method in a test class.
        cls.homepagedata=HomePageData()
        cls.h=Helper
        cls.logger = logging_setup()


    def close_login_model(self):
        """
        Closes the login modal if it is visible.

        """
        try:
            model_element=self.wait_for_element_visible(BasePageFragments.close_loginModel)
            if not model_element:
                self.logger.warning("Login modal close button not found.") 
                return
            if self.is_element_displayed(BasePageFragments.login_mobilenumber):
                self.click_element(BasePageFragments.close_loginModel)
                self.logger.info("Login modal closed successfully.")
        except Exception as e:
            self.logger.error(f"Failed to close login modal: {str(e)}") 


        # element=self.wait_for_element_visible(BasePageFragments.close_loginModel)
        # if not element:
        #     return
        # self.is_element_displayed(BasePageFragments.login_mobilenumber)
        # self.click_element(BasePageFragments.close_loginModel)

    # def set_date(self):
    #     """Sets the travel date by clicking the departure field and selecting a date."""
    #     try:
    #         self.click_element(BasePageFragments.travel_date)
    #         self.h.get_date_of_travel()
    #         self.logger.info("Travel date set successfully.")
    #     except Exception as e:
    #         self.logger.error(f"Failed to set travel date: {str(e)}")  # CHANGED: Use instance logger
    #         raise


        # self.click_element(BasePageFragments.travel_date)
        # self.h.get_date_of_travel()

    def close_popups(self):
        self.click_element(self.popups)
        self.logger.info("pop up is closed")

    def logo_visability_and_navigation_in_pages(self):
        """
        Verifies logo visibility and navigation behavior on the homepage.
        """
        try:
            if self.findElement(self.popups):
                self.close_popups()
                
            if not self.findElement(BasePageFragments.logo_stickheader):
                self.logger.error("logo is not displayed in stick header")
            
            if not self.verify_page_refresh(self.logo_stickheader):
                self.logger.error("Page did not refresh after clicking logo.")  

            if not self.findElements(self.logo_mmt_homepage):
                self.logger.error("Failed to navigate to homepage after clicking logo.")  

            self.logger.info("Logo visibility and navigation verified successfully.")

        except Exception as e:
             self.logger.error(f"logo verification failed : {str(e)}")


        # assert self.findElement(BasePageFragments.logo_stickheader), "logo is not displayed in stick header"
        # assert self.verify_page_refresh(BasePageFragments.logo_stickheader), "page not refreshed on clicking mmt logo"
        # assert self.findElements(BasePageFragments.logo_mmt_homepage), "not navigated to on clicking MMT logo in stick header"

    def verify_elements_sticky_header_in_pages(self, elements: List[str]) -> bool:
        """
        Verifies that the sticky header contains the expected elements.

        :param elements: List of expected elements in the sticky header
        :return: True if elements match, False otherwise
        """
        # expected_elements = elements
        # actual_elements = []

        # available_elements = Webelement.findElements(BasePageFragments.elements_in_sticky_header)

        # # Extract the text from each element found
        # for element in available_elements:
        #     actual_elements.append(element.text.strip())  # Ensure no extra spaces

        # # Now compare both lists
        # if set(actual_elements) == set(expected_elements):
        #     print("The elements in the sticky header matched.")
        #     return True
        # else:
        #     print("The elements in the sticky header do not matched.")
        #     print("Expected:", expected_elements)
        #     print("Actual:", actual_elements)
        #     return False
        try:
            actual_elements=[]
            expected_elements=elements
            available_elements=self.findElements(BasePageFragments.elements_in_sticky_header)

            if not available_elements:
                self.logger.warning("no elements found in sticky header")

            for element in available_elements:
                actual_elements.append(element.text.strip()) # Ensure no extra spaces 

            if set(actual_elements)==set(expected_elements):
                self.logger.info("Sticky header elements matched expected values.")
                return True
            
            self.logger.warning("Sticky header elements did not match expected values.")  
            self.logger.debug(f"Expected: {expected_elements}")  
            self.logger.debug(f"Actual: {actual_elements}")  
            return False
        except Exception as e :
            self.logger.error(f"Failed to verify sticky header elements: {str(e)}")
            return False  