from Pages.Home_page import Homepage_mmt
from Locators.Buspage_locators import busespage_locators
from _Data.data import HomePageData
from _Wrapper.Webelements import Webelement

class Buses_mmt(Homepage_mmt):

       searchBar=busespage_locators.BUSES_SEARCH_BAR
       source_city=busespage_locators.FORM_CITY
       destination_city=busespage_locators.TO_CITY
       otherdate=busespage_locators.OTHER_DATE
       searchbutton=busespage_locators.SEARCH_BUTTON
       options_sortby=busespage_locators.SORT_BY
       avilableFilters=busespage_locators.AVILABLE_FILTERS
       dateslider=busespage_locators.DATE_SLIDER
       dealsbanner=busespage_locators.DEALS_BANNER
       view_statebuses=busespage_locators.VIEW_STATEBUSES
       busesFound=busespage_locators.BUSES_FOUND
       buseslist=busespage_locators.BUSES_LIST

       def verify_searchbar_busespage(self):
           assert self.findElement(Buses_mmt.searchBar), "search bar is not dispalyed in buses page "

       def enter_to_and_from_city(self):
           self.click_element(Buses_mmt.source_city)
           self.send_text(Homepage_mmt.input_field,self.homepagedata.Domestic_cities[2])
           self.click_element(Buses_mmt.destination_city)
           self.send_text(Homepage_mmt.input_field,self.homepagedata.International_cities[2])
       
       def select_date(self):
           Webelement.click_element(Buses_mmt.otherdate)
           Webelement.set_date(HomePageData.travel_date)

       def click_search_button(self):
            Webelement.click_element(Buses_mmt.searchbutton)

       def avilable_sort_options(self):
            
            elements=Webelement.findElements(Buses_mmt.options_sortby)

            return [element.text for element in elements]
       
       def avilable_filters(self):
           elements=Webelement.findElements(Buses_mmt.avilableFilters)
           filters=[element.text for element in elements]
           return filters
       
       
       
       def verify_date_slider(self):
              
            assert Webelement.findElement(Buses_mmt.dateslider), "date slider is not displayed in buses page"

       def verify_dealsBanner_is_dispalyed(self):
            
            assert Webelement.findElement(Buses_mmt.dealsbanner), "deals banners is not dispalyed in buses page "

       def click_veiw_stateebuses(self):
            
            Webelement.click_element(Buses_mmt.view_statebuses)

       def verify_buses_found(self):
            
           busesfound = int(Webelement.findElement(Buses_mmt.busesFound).text.split(' ')[0])

           actualbuses = Webelement.findElements(Buses_mmt.buseslist)

           assert len(actualbuses) == busesfound, f"The count shown ({busesfound}) and buses found ({len(actualbuses)}) do not match."
