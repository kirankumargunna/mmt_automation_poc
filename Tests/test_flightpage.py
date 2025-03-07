import pytest
from Pages.Base_page import BasePageFragments
from Pages.Home_page import Homepage_mmt
from Pages.Flight_page import flights_MMT
from _Data.data import FlightPageData as FD, HomePageData as HD

class Test_mmt_flightapage(BasePageFragments):

    @pytest.mark.flightpage
    @pytest.mark.smoke
    def test_smoketest_flightpage(self):
        # search for the flights in home page 
        BasePageFragments.close_login_model(self)
        Homepage_mmt.flight_search(self)

        #verfiy mmt logo is visable and navigates to home page on clicking 
        flights_MMT.logo_visability_and_navigation_in_pages(self)
        
        # agian click on search in home to navigate to flight page 
        self.click_element(Homepage_mmt.search)

        # close the popups appeared 
        flights_MMT.close_popups(self)

        # verify that search bar is displayed 
        flights_MMT.verify_search_bar_flightPage(self)

        # verify the filter filter type bar is present 

        flights_MMT.verify_fareType_bar(self)

        #verify the avilable filters in the filghts page

        Avilable_Filters=flights_MMT.avilableFilters(self)
        missing = set(FD.FILTERS) - set(Avilable_Filters)  # Elements in FD.Filters but not in Avilable_Flights
        extra = set(Avilable_Filters) - set(FD.FILTERS)  # Elements in Avilable_Flights but not in FD.Filters

        assert sorted(Avilable_Filters) == sorted(FD.FILTERS), f"Missing: {missing}, Extra: {extra}"

        #verify the avilable icons in the filghts page sticky header

        Avilable_icons=flights_MMT.avilable_icons_sticky_Header(self)
        missing = set(HD.NAVIGATION_BAR_ELEMENTS) - set(Avilable_icons)  # Elements in FD.Filters but not in Avilable_Flights
        extra = set(Avilable_icons) - set(HD.NAVIGATION_BAR_ELEMENTS)  # Elements in Avilable_Flights but not in FD.Filters

        assert sorted(Avilable_icons) == sorted(HD.NAVIGATION_BAR_ELEMENTS), f"Missing: {missing}, Extra: {extra}"




    @pytest.mark.flightpage
    def test_flight_search_valid_data(self):

        BasePageFragments.close_login_model(self)
        #search for flight with valid data in home page 
        Homepage_mmt.flight_search(self)

        #verfiy search button is disabled initally
        assert not flights_MMT.verfiy_search_button_status(self) , "search button in disabled intially"

        #select trip type
        flights_MMT.select_trip_type(self,FD.Trip_types[1])

        # enter to and from city 

        flights_MMT.enter_to_and_from_city(self)

        # verify search button is enabled 
        assert  flights_MMT.verfiy_search_button_status(self) , "search button in enabled"

        #enter date 

        flights_MMT.select_date(self)

        #click search button 
        flights_MMT.click_search_button(self)