from Pages.Home_page import Homepage_mmt
from Locators.Buspage_locators import BusesPageLocators
from _Data.data import HomePageData
from _Wrapper.Webelements import Webelement

class Buses_mmt(Homepage_mmt):

       searchBar=BusesPageLocators.BUSES_SEARCH_BAR
       source_city=BusesPageLocators.FROM_CITY
       destination_city=BusesPageLocators.TO_CITY
       otherdate=BusesPageLocators.OTHER_DATE
       searchbutton=BusesPageLocators.SEARCH_BUTTON
       options_sortby=BusesPageLocators.SORT_BY
       avilableFilters=BusesPageLocators.AVAILABLE_FILTERS
       dateslider=BusesPageLocators.DATE_SLIDER
       dealsbanner=BusesPageLocators.DEALS_BANNER
       view_statebuses=BusesPageLocators.VIEW_STATEBUSES
       busesFound=BusesPageLocators.BUSES_FOUND
       buseslist=BusesPageLocators.BUSES_LIST

       def verify_searchbar_busespage(self):
          try:
               if not self.findElement(Buses_mmt.searchBar):
                    self.logger.error("Search bar is not displayed in the buses page")
               if self.findElement(Buses_mmt.searchBar):
                    self.logger.info("Identified search bar in buses page")
          except Exception as e:
               self.logger.error(f"Unexpected error search bar is not visable: {str(e)}")
        

       def enter_to_and_from_city(self):

          self.logger.info("Entering source and destination cities in flight page")
          try:
            self.click_element(Buses_mmt.source_city)
            self.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[1])
            Webelement.click_element(Buses_mmt.destination_city)
            Webelement.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[2])
            self.logger.info(f"Set cities: {self.homepagedata.DOMESTIC_CITIES[1]} to {self.homepagedata.DOMESTIC_CITIES[2]}")
          except Exception as e:
            self.logger.error(f"Unexpected error in entering cities: {str(e)}")
            raise Exception(f"Unexpected error while entering cities: {str(e)}") from e


          #  self.click_element(Buses_mmt.source_city)
          #  self.send_text(Homepage_mmt.input_field,self.homepagedata.DOMESTIC_CITIES[2])
          #  self.click_element(Buses_mmt.destination_city)
          #  self.send_text(Homepage_mmt.input_field,self.homepagedata.INTERNATIONAL_CITIES[2])
       
       def select_date(self):
          self.logger.info("Attempting to select date")
          try:
               self.click_element(Buses_mmt.otherdate)
               self.set_date(HomePageData.TRAVEL_DATE)
               self.logger.info("sucessfully selected date")
          except Exception as e:
               self.logger.error(f"Unexpected error in selecting date: {str(e)}")

       def click_search_button(self):
          try:
               self.click_element(Buses_mmt.searchbutton)
          except Exception as e:
               self.logger.error(f"Error in click_search_button: {e}")
              
              
               # self.click_element(Buses_mmt.searchbutton)

       def avilable_sort_options(self):
          try:
              elements = Webelement.findElements(Buses_mmt.options_sortby)
              return [element.text for element in elements]
          except Exception as e:
               self.logger.error(f"Error in avilable_sort_options: {e}")
               return []  




          #   elements=Webelement.findElements(Buses_mmt.options_sortby)

          #   return [element.text for element in elements]
       
       def avilable_filters(self):
          try:
               elements = Webelement.findElements(Buses_mmt.avilableFilters)
               filters = [element.text for element in elements]
               return filters
          except Exception as e:
               self.logger.error(f"Error in avilable_filters: {e}")
               return []



          #  elements=Webelement.findElements(Buses_mmt.avilableFilters)
          #  filters=[element.text for element in elements]
          #  return filters
       
       
       
       def verify_date_slider(self):
          try:
               assert Webelement.findElement(Buses_mmt.dateslider), "date slider is not displayed in buses page"
          except AssertionError as e:
               self.logger.error(f"Assertion Failed: {e}")
          except Exception as e:
               self.logger.error(f"Error in verify_date_slider: {e}")
              
          #   assert Webelement.findElement(Buses_mmt.dateslider), "date slider is not displayed in buses page"

       def verify_dealsBanner_is_dispalyed(self):
          try:
               assert Webelement.findElement(Buses_mmt.dealsbanner), "deals banners is not dispalyed in buses page"
          except AssertionError as e:
               self.logger.error(f"Assertion Failed: {e}")
          except Exception as e:
               self.logger.error(f"Error in verify_dealsBanner_is_dispalyed: {e}")  
     
     
     # assert Webelement.findElement(Buses_mmt.dealsbanner), "deals banners is not dispalyed in buses page "

       def click_veiw_stateebuses(self):
            
          try:
               Webelement.click_element(Buses_mmt.view_statebuses)
          except Exception as e:
               self.logger.error(f"Error in click_veiw_stateebuses: {e}")
            
          # Webelement.click_element(Buses_mmt.view_statebuses)

       def verify_buses_found(self):
           
          try:
               busesfound = int(Webelement.findElement(Buses_mmt.busesFound).text.split(' ')[0])
               actualbuses = Webelement.findElements(Buses_mmt.buseslist)
               assert len(actualbuses) == busesfound, f"The count shown ({busesfound}) and buses found ({len(actualbuses)}) do not match."
          except AssertionError as e:
               self.logger.error(f"Assertion Failed: {e}")
          except Exception as e:
               self.logger.error(f"Error in verify_buses_found: {e}")


            
          #  busesfound = int(Webelement.findElement(Buses_mmt.busesFound).text.split(' ')[0])

          #  actualbuses = Webelement.findElements(Buses_mmt.buseslist)

          #  assert len(actualbuses) == busesfound, f"The count shown ({busesfound}) and buses found ({len(actualbuses)}) do not match."


