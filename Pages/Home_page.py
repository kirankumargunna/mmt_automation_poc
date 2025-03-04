import time

from selenium.webdriver.common.by import By

from drivers.webdrivers import webdrivers
from Locators.Homepage_locators import homepage_locators
from Pages.Base_page import BasePageFragments
from _Wrapper.Webelements import Webelement
from _Data.data import HomePageData



class Homepage_mmt(BasePageFragments):
    logo_mmt = homepage_locators.MMT_LOGO_HOMEPAGE
    list_your_property = homepage_locators.LIST_YOUR_PROPERTY
    introducing_Mybiz=homepage_locators.INTROUDUCING_MYBIZ
    toolTip_introducing_mybiz=homepage_locators.TOOLTIP_INTROUDUCING_MYBIZ
    login_or_createAccount=homepage_locators.LOGIN_OR_CREATEACCOUNT
    navigation_bar=homepage_locators.ICON_IN_STICKY_HEADER
    source_city=homepage_locators.FROM_CITY_INPUT
    destination_city=homepage_locators.TO_CITY_INPUT
    input_field=homepage_locators.SEARCH_INPUT_FIELD
    depature=homepage_locators.DEPATURE # for flights
    search=homepage_locators.SEARCH_BUTTON
    Bus=homepage_locators.BUSES_ICON
    travelDate=homepage_locators.TRAVEL_DATE_CALENDAR # for buses and trains



    def logo_visablity_and_navigation(self):
        assert Webelement.is_element_displayed(Homepage_mmt.logo_mmt), "make my trip logo  is not displayed"
        assert Webelement.verify_page_refresh(Homepage_mmt.logo_mmt), "page not refreshed on clicking mmt logo"

    def list_your_property_hyperlink(self):
        assert Webelement.is_element_displayed(Homepage_mmt.list_your_property), "list you propert hyperlink is not displayed"
        assert Webelement.verify_new_tab(Homepage_mmt.list_your_property)==HomePageData.LIST_YOUR_PROPERTIES_PAGE_TITLE
        Homepage_mmt.close_current_tab()
        Homepage_mmt.switch_tab(0)
        time.sleep(3)

    def introducing_mybiz(self):
        assert Webelement.is_element_displayed(Homepage_mmt.introducing_Mybiz), "introducing mybiz hyperlink is not displayed"
        Webelement.mousehover(Homepage_mmt.introducing_Mybiz)
        assert Webelement.is_element_displayed(Homepage_mmt.toolTip_introducing_mybiz).text=='SWITCH TO MYBIZ', "tooltip introducing mybiz is not displayed "
        # assert_equal(Webelement.is_element_displayed(Homepage_mmt.toolTip_introducing_mybiz).text,"SWITCH TO MYBIZ","tooltip introducing mybiz is not displayed")
    def login_or_createaccount(self):
        assert Webelement.is_element_displayed(Homepage_mmt.login_or_createAccount), "login option is not displayed on home page"
        Webelement.click_element(Homepage_mmt.login_or_createAccount)
        assert Webelement.is_element_displayed(Homepage_mmt.login_mobilenumber), "user is not prompted to login after clicking on login button"
        Webelement.click_element(Homepage_mmt.close_loginModel)

    def get_elements_navigation_bar(self):
        element_list=Webelement.findElements(Homepage_mmt.navigation_bar)
        return [name for name in element_list.text]

    def flight_search(self):
        Webelement.click_element(Homepage_mmt.source_city)
        Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[1])
        Webelement.click_element(Homepage_mmt.destination_city)
        Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.INTERNATIONAL_CITIES[1])
        # Webelement.click_element(Homepage_mmt.depature)
        Webelement.set_date(HomePageData.TRAVEL_DATE)
        Webelement.click_element(Homepage_mmt.search)

    def bus_search(self):
        Webelement.click_element(Homepage_mmt.Bus)
        Webelement.click_element(Homepage_mmt.source_city)
        Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[1])
        if not Webelement.is_element_displayed(Homepage_mmt.input_field):
            Webelement.click_element(Homepage_mmt.destination_city)
        Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[0])

        if not Webelement.is_element_displayed(Homepage_mmt.travelDate):
            Webelement.click_element(Homepage_mmt.travelDate)
        Webelement.set_date(HomePageData.TRAVEL_DATE)
        Webelement.click_element(Homepage_mmt.search)

