from typing import List
from Locators.Homepage_locators import homepage_locators
from _Wrapper.Webelements import Webelement
from _Data.data import HomePageData
from _Wrapper import Helper

class BasePageFragments(Webelement):

    close_loginModel=homepage_locators.CLOSE_LOGIN_MODAL_BUTTON
    login_mobilenumber=homepage_locators.LOGIN_MOBILE_NUMBER_INPUT
    travel_date=homepage_locators.DEPATURE
    logo_stickheader=homepage_locators.MMT_LOGO_STICKY_HEADER
    logo_mmt_homepage=homepage_locators.MMT_LOGO_HOMEPAGE
    elements_in_sticky_header=homepage_locators.ICON_IN_STICKY_HEADER


    @classmethod
    def setup_method(cls):    #Runs before each test method in a test class.
        cls.homepagedata=HomePageData()
        cls.h=Helper

    def close_login_model(self):
        element=self.wait_for_element_visible(BasePageFragments.close_loginModel)
        if not element:
            return
        self.is_element_displayed(BasePageFragments.login_mobilenumber)
        self.click_element(BasePageFragments.close_loginModel)

    def set_date(self):
        self.click_element(BasePageFragments.travel_date)
        self.h.get_date_of_travel()

    def logo_visability_and_navigation_in_pages(self):
        assert self.findElement(BasePageFragments.logo_stickheader), "logo is not displayed in stick header"
        assert self.verify_page_refresh(BasePageFragments.logo_stickheader), "page not refreshed on clicking mmt logo"
        assert self.findElements(BasePageFragments.logo_mmt_homepage), "not navigated to on clicking MMT logo in stick header"

    def verify_elements_sticky_header_in_pages(self, elements: List[str]) -> bool:
        """
        Verifies whether the elements in the sticky header match the expected elements.

        :param elements: List of expected elements in the sticky header
        :return: True if elements match, False otherwise
        """
        expected_elements = elements
        actual_elements = []

        available_elements = Webelement.findElements(BasePageFragments.elements_in_sticky_header)

        # Extract the text from each element found
        for element in available_elements:
            actual_elements.append(element.text.strip())  # Ensure no extra spaces

        # Now compare both lists
        if set(actual_elements) == set(expected_elements):
            print("The elements in the sticky header matched.")
            return True
        else:
            print("The elements in the sticky header do not matched.")
            print("Expected:", expected_elements)
            print("Actual:", actual_elements)
            return False
