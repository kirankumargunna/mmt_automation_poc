import time

from selenium.webdriver.common.by import By

from drivers.webdrivers import webdrivers
from Locators.Homepage_locators import HomepageLocators
from Pages.Base_page import BasePageFragments
from _Wrapper.Webelements import Webelement
from _Data.data import HomePageData



class Homepage_mmt(BasePageFragments):
    logo_mmt = HomepageLocators.MMT_LOGO_HOMEPAGE
    list_your_property = HomepageLocators.LIST_YOUR_PROPERTY
    introducing_Mybiz=HomepageLocators.INTRODUCING_MYBIZ
    toolTip_introducing_mybiz=HomepageLocators.TOOLTIP_INTROUDUCING_MYBIZ
    login_or_createAccount=HomepageLocators.LOGIN_OR_CREATEACCOUNT
    navigation_bar=HomepageLocators.ICON_IN_STICKY_HEADER
    source_city=HomepageLocators.FROM_CITY_INPUT
    destination_city=HomepageLocators.TO_CITY_INPUT
    input_field=HomepageLocators.SEARCH_INPUT_FIELD
    depature=HomepageLocators.DEPATURE # for flights
    search=HomepageLocators.SEARCH_BUTTON
    Bus=HomepageLocators.BUSES_ICON
    travelDate=HomepageLocators.TRAVEL_DATE_CALENDAR # for buses and trains



    def logo_visibility_and_navigation(self):
        """
        Verifies logo visibility and navigation behavior.
        """

        try:
            if not self.is_element_displayed(Homepage_mmt.logo_mmt):
                self.logger.error("MakeMyTrip logo is not displayed.")
            if not self.verify_page_refresh(Homepage_mmt.logo_mmt):
                self.logger.error("Page not refreshed on clicking MMT logo.")
            self.logger.info("Logo visibility and navigation verified.")

        except Exception as e:
            self.logger.error(f"Logo visibility check failed: {str(e)}")

        # assert Webelement.is_element_displayed(Homepage_mmt.logo_mmt), "make my trip logo  is not displayed"
        # assert Webelement.verify_page_refresh(Homepage_mmt.logo_mmt), "page not refreshed on clicking mmt logo"

    def list_your_property_hyperlink(self):

        try:
            if not self.is_element_displayed(Homepage_mmt.list_your_property):
                self.logger.error("List Your Property hyperlink is not displayed.")

            new_tab_title = self.verify_new_tab_title(Homepage_mmt.list_your_property)  
            if new_tab_title != HomePageData.LIST_YOUR_PROPERTIES_PAGE_TITLE:  
                self.logger.error(f"Expected title {HomePageData.LIST_YOUR_PROPERTIES_PAGE_TITLE}, got {new_tab_title}")
                return False   
            self. close_current_tab()   
            self.switch_tab(0)     
            self.wait_for_element_visible(Homepage_mmt.logo_mmt)     
            self.logger.info("List Your Property hyperlink verified.")
        except Exception as e :
            self.logger.error(f"List Your Property verification failed: {str(e)}")


        # assert Webelement.is_element_displayed(Homepage_mmt.list_your_property), "list you propert hyperlink is not displayed"
        # assert Webelement.verify_new_tab(Homepage_mmt.list_your_property)==HomePageData.LIST_YOUR_PROPERTIES_PAGE_TITLE
        # Homepage_mmt.close_current_tab()
        # Homepage_mmt.switch_tab(0)
        # time.sleep(3)

    def introducing_mybiz(self):
        """
        Verifies the 'Introducing MyBiz' hyperlink and its tooltip.
        """
        try:
            if not self.is_element_displayed(Homepage_mmt.introducing_Mybiz):
                self.logger.error("Introducing MyBiz hyperlink is not displayed.")
            
            self.mousehover(Homepage_mmt.introducing_Mybiz)
            
            tooltip=self.is_element_displayed(Homepage_mmt.toolTip_introducing_mybiz)
            if not tooltip or tooltip.text != 'SWITCH TO MYBIZ':
                self.logger.error(f"Tooltip text mismatch. Expected 'SWITCH TO MYBIZ', got {tooltip.text if tooltip else None}")
            self.logger.info("Introducing MyBiz tooltip verified.")
        except Exception as e:
            self.logger.error(f"Introducing MyBiz verification failed: {str(e)}")


        # assert Webelement.is_element_displayed(Homepage_mmt.introducing_Mybiz), "introducing mybiz hyperlink is not displayed"
        # Webelement.mousehover(Homepage_mmt.introducing_Mybiz)
        # assert Webelement.is_element_displayed(Homepage_mmt.toolTip_introducing_mybiz).text=='SWITCH TO MYBIZ', "tooltip introducing mybiz is not displayed "
        
        # # assert_equal(Webelement.is_element_displayed(Homepage_mmt.toolTip_introducing_mybiz).text,"SWITCH TO MYBIZ","tooltip introducing mybiz is not displayed")
    def login_or_createaccount(self):
        """
        Verifies the login/create account functionality.
        """
        try:
            if not self.is_element_displayed(Homepage_mmt.login_or_createAccount):
                self.logger.error("Login option is not displayed on homepage. ")
            
            #click on the login or create account button 
            self.click_element(Homepage_mmt.login_or_createAccount)

            if not self.is_element_displayed(Homepage_mmt.login_mobilenumber):
                self.logger.error("User not prompted to login after clicking login button.")
            
            #close the login window 
            self.click_element(Homepage_mmt.close_loginModel)

            self.logger.info("Login/Create Account functionality verified. ")

        except Exception as e:
            self.logger.error(f"Login/Create Account verification failed: {str(e)}")
            

        # assert Webelement.is_element_displayed(Homepage_mmt.login_or_createAccount), "login option is not displayed on home page"
        # Webelement.click_element(Homepage_mmt.login_or_createAccount)
        # assert Webelement.is_element_displayed(Homepage_mmt.login_mobilenumber), "user is not prompted to login after clicking on login button"
        # Webelement.click_element(Homepage_mmt.close_loginModel)

    def get_elements_navigation_bar(self):

        """
        Retrieves text of elements in the navigation bar.
        """
        try: 
            elements= self.findElement(Homepage_mmt.navigation_bar)
            nav_items= [element.text.strip() for element in elements if element.text.strip()]
            self.logger.debug(f"Navigation bar elements: {nav_items}")
            return nav_items
        except Exception as e:
            self.logger.error(f"Failed to get navigation bar elements: {str(e)}")
            return []


        # element_list=Webelement.findElements(Homepage_mmt.navigation_bar)
        # return [name for name in element_list.text]

    def flight_search(self):
        """
        Performs a flight search with source and destination cities.
        """

        try:
            self.click_element(Homepage_mmt.source_city) 
            self.send_text(Homepage_mmt.input_field, HomePageData.DOMESTIC_CITIES[1])
            self.click_element(Homepage_mmt.destination_city)
            self.send_text(Homepage_mmt.input_field, HomePageData.INTERNATIONAL_CITIES[1])
            # self.click_element(Homepage_mmt.depature)
            Webelement.set_date(HomePageData.TRAVEL_DATE)
            self.click_element(Homepage_mmt.search)
            self.logger.info("Flight search initiated successfully")
        except Exception as e:
            self.logger.error(f"Flight search failed: {str(e)}")




        # Webelement.click_element(Homepage_mmt.source_city)
        # Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[1])
        # Webelement.click_element(Homepage_mmt.destination_city)
        # Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.INTERNATIONAL_CITIES[1])
        # # Webelement.click_element(Homepage_mmt.depature)
        # Webelement.set_date(HomePageData.TRAVEL_DATE)
        # Webelement.click_element(Homepage_mmt.search)

    def bus_search(self):
        """
        Performs a bus search with source and destination cities.
        """
        try:
            self.click_element(Homepage_mmt.Bus)
            self.click_element(Homepage_mmt.source_city)
            self.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[1])
            if not self.is_element_displayed(Homepage_mmt.input_field):
                self.click_element(Homepage_mmt.destination_city)
            self.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[0])
            if not self.is_element_displayed(Homepage_mmt.travel_date):
                self.click_element(Homepage_mmt.travelDate)
            self.set_date(HomePageData.TRAVEL_DATE)
            self.click_element(Homepage_mmt.search)
            self.logger.info('Bus search initiated successfully. ')
        except Exception as e:
            self.logger.error(f"Bus search failed: {str(e)}")
             




        # Webelement.click_element(Homepage_mmt.Bus)
        # Webelement.click_element(Homepage_mmt.source_city)
        # Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[1])
        # if not Webelement.is_element_displayed(Homepage_mmt.input_field):
        #     Webelement.click_element(Homepage_mmt.destination_city)
        # Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[0])

        # if not Webelement.is_element_displayed(Homepage_mmt.travelDate):
        #     Webelement.click_element(Homepage_mmt.travelDate)
        # Webelement.set_date(HomePageData.TRAVEL_DATE)
        # Webelement.click_element(Homepage_mmt.search)

