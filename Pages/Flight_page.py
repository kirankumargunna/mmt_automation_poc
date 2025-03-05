from typing import List
from selenium.webdriver.support.ui import Select
from _Data.data import HomePageData
from _Wrapper.Webelements import Webelement
from Locators.Flightpage_locators import flightPage_locators
from Pages.Home_page import Homepage_mmt


class flights_MMT(Homepage_mmt):

    search_bar=flightPage_locators.SEARCH_BAR
    fareType_bar=flightPage_locators.FARETYPE_BAR
    search_button_disabled=flightPage_locators.SEARCH_BUTTON_DISABLED
    search_button_enabled=flightPage_locators.SEARCH_BUTTON_ENABLED
    current_trip_type=flightPage_locators.CURRENT_TRIP_TYPE
    trip_type_dropdown=flightPage_locators.TRIP_TYPE_DROPDOWN
    fareType=flightPage_locators.FARE_TYPE
    available_filters=flightPage_locators.FILTERS_FLIGHTS
    available_icons_sticky_header=flightPage_locators.ICON_IN_STICKY_HEADER



    def verify_search_bar_flightPage(self):
        assert Webelement.findElement(flights_MMT.search_bar) , "search bar is not dispaled in flight page"

    def verify_fareType_bar(self):
        assert Webelement.findElement(flights_MMT.fareType_bar), "fare type bar is not displayed"
    
    def verify_search_button_status(self):
        
        if Webelement.findElement(flights_MMT.search_button_enabled):
            return True
        elif Webelement.findElement(flights_MMT.search_button_disabled):
            return False
        else :
            raise ValueError("search button is not avilable")
        
    def select_trip_type(self,trip_type:str):

        if Webelement.findElement(flights_MMT.current_trip_type).text !=trip_type:
            Webelement.click_element(flights_MMT.current_trip_type)
            element=Webelement.findElement(flights_MMT.trip_type_dropdown)
            if element is not None:
                dropdown=Select(element)
            else:
                raise ValueError("No elements in dropdown")
            dropdown.select_by_visible_text(trip_type)


    def enter_to_and_from_city(self):
        Webelement.click_element(Homepage_mmt.source_city)
        Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.Domestic_cities[2])
        Webelement.click_element(Homepage_mmt.destination_city)
        Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.International_cities[2])
    
    def select_date(self):
        Webelement.set_date(HomePageData.TRAVEL_DATE)
    
    def click_search_button(self):
        assert self.verfiy_search_button_status(), "search button is not enabled"
        Webelement.click_element(flights_MMT.search_button_enabled)
        
    def select_fare_type(self):
        Webelement.click_element(flights_MMT.fareType)

    def avilableFilters(self)->list[str]:
        elements=Webelement.findElements(flights_MMT.avilable_filters)
        filters=[element.text for element in elements]
        return filters
    
    def avilable_icons_sticky_Header(self):
        elements=Webelement.findElements(flights_MMT.avilable_icons_stickyHeader)
        icons=[element.text for element in elements]

        return icons
        


