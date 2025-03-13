from typing import List
from selenium.webdriver.support.ui import Select
from _Data.data import HomePageData
from _Wrapper.Webelements import Webelement
from Locators.Flightpage_locators import FlightPageLocators
from Pages.Home_page import Homepage_mmt


class flights_MMT(Homepage_mmt):

    search_bar=FlightPageLocators.SEARCH_BAR
    fareType_bar=FlightPageLocators.FARETYPE_BAR
    search_button_disabled=FlightPageLocators.SEARCH_BUTTON_DISABLED
    search_button_enabled=FlightPageLocators.SEARCH_BUTTON_ENABLED
    current_trip_type=FlightPageLocators.CURRENT_TRIP_TYPE
    trip_type_dropdown=FlightPageLocators.TRIP_TYPE_DROPDOWN
    fareType=FlightPageLocators.FARE_TYPE
    available_filters=FlightPageLocators.FILTERS_FLIGHTS
    available_icons_sticky_header=FlightPageLocators.ICON_IN_STICKY_HEADER
    popup=FlightPageLocators.POPUPS



    def verify_search_bar_flightPage(self):
        """Verify the search bar is displayed on the flight page.
        """
        self.logger.info("Verifying search bar visibility on flight page")
        try:
            if not self.findElement(flights_MMT.search_bar):
                self.logger.error("Search bar is not displayed")
            if self.findElement(flights_MMT.search_bar):
                self.logger.info("Search bar is displayed")
            self.logger.info("Verified search bar sucessfully")
        except Exception as e:
            self.logger.error(f"Failed to verify search bar: {str(e)}")

        # assert Webelement.findElement(flights_MMT.search_bar) , "search bar is not dispaled in flight page"

    def verify_fareType_bar(self):

        """Verify the faretype bar is displayed on the flight page.
        """
        self.logger.info("Verifying faretype bar visibility on flight page")
        try:
            if not self.findElement(flights_MMT.fareType_bar):
                self.logger.error("faretype bar is not displayed")
            if self.findElement(flights_MMT.fareType_bar):
                self.logger.info("faretype bar is displayed")
            self.logger.info("Verified faretype bar sucessfully")
        except Exception as e:
            self.logger.error(f"Failed to verify faretype bar: {str(e)}")



        # assert Webelement.findElement(flights_MMT.fareType_bar), "fare type bar is not displayed"
    
    def verify_search_button_status(self) -> bool:
        """Check if the search button is enabled or disabled.

        Returns:
            bool: True if enabled, False if disabled.
        Raises:
            ValueError: If the search button is not found in either state.
        """
        self.logger.info("Verifying search button status")
        if Webelement.findElement(flights_MMT.search_button_enabled):
            self.logger.info("Search button is enabled")
            return True
        elif Webelement.findElement(flights_MMT.search_button_disabled):
            self.logger.info("Search button is disabled")
            return False
        else :
            self.logger.error("Search button is not available")
            raise ValueError("search button is not avilable")
        
    def select_trip_type(self,trip_type:str):
        """Select a trip type from the dropdown if it differs from the current selection.

        Args:
            trip_type (str): The trip type to select (e.g., 'One Way', 'Round Trip').

        Raises:
            ValueError: If the dropdown or trip type is not found.
        """
        self.logger.info(f"Selecting trip type: {trip_type}")
        if self.findElement(flights_MMT.current_trip_type).text !=trip_type:
            self.click_element(flights_MMT.current_trip_type)
            element=self.findElement(flights_MMT.trip_type_dropdown)
            if element is not None:
                dropdown=Select(element)
                self.logger.info(f"Trip type '{trip_type}' selected")
            else:
                self.logger.error("Dropdown element not found")
                raise ValueError("No elements in dropdown")
            dropdown.select_by_visible_text(trip_type)


    def enter_to_and_from_city(self):

        self.logger.info("Entering source and destination cities in flight page")
        try:
            self.click_element(Homepage_mmt.source_city)
            self.send_text(Homepage_mmt.input_field,self.homepagedata.Domestic_cities[2])
            Webelement.click_element(Homepage_mmt.destination_city)
            Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.International_cities[2])
            self.logger.info(f"Set cities: {self.homepagedata.Domestic_cities[2]} to {self.homepagedata.INTERNATIONAL_CITIES[2]}")
        except Exception as e:
            self.logger.error(f"Unexpected error in entering cities: {str(e)}")
            raise Exception(f"Unexpected error while entering cities: {str(e)}") from e
    def select_date(self):
        self.logger.info("Selecting travel date")
        try:
            self.set_date(HomePageData.TRAVEL_DATE)
            self.logger.info(f"Travel date set to {HomePageData.TRAVEL_DATE}")
        except Exception as e:
            self.logger.error(f"Unexpected error in date selection: {str(e)}")
            raise Exception(f"Unexpected error while selecting date: {str(e)}") from e
    
    def click_search_button(self):
        self.logger.info("Attempting to click search button")
        try:
            if not self.verify_search_button_status:
                self.logger.warning("Search button is disabled")
            elif self.verify_search_button_status:
                self.click_element(flights_MMT.search_button_enabled)
                self.logger.info("clicked searh button")
        except Exception as e:
            self.logger.error(f"Unexpected error clicking search button: {str(e)}")
            raise Exception(f"Unexpected error while clicking search button: {str(e)}") from e
        assert self.verify_search_button_status(), "search button is not enabled"
        self.click_element(flights_MMT.search_button_enabled)
        
    def select_fare_type(self):
        self.logger.info("Attempting to select fare type ")
        try:
            self.click_element(flights_MMT.fareType)
            self.logger.info("Sucessfully selected fare type")
        except Exception as e:
            self.logger.error("Unable to select fare type")

    def avilableFilters(self)->list[str]:
        self.logger.info("Attempting to fetch the list of available filters")
        try:

            elements=self.findElements(flights_MMT.available_filters)
            filters=[element.text for element in elements]
            self.logger.info(f"Available filters: {filters}")
            return filters
        except Exception as e:
            self.logger.error(f"Unexpected error retrieving filters: {str(e)}")
            raise Exception(f"Unexpected error while retrieving filters: {str(e)}") from e            
    
    def avilable_icons_sticky_Header(self):
        try:
            elements=self.findElements(flights_MMT.available_icons_sticky_header)
            icons=[element.text for element in elements]
            self.logger.info(f"Available filters: {icons}")
            return icons
        except Exception as e:
                self.logger.error(f"Unexpected error retrieving icons: {str(e)}")
                raise Exception(f"Unexpected error while retrieving icons: {str(e)}") from e            
        
