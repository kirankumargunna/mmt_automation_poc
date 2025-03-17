import pytest
import allure
from Pages.Base_page import BasePageFragments
from Pages.Home_page import Homepage_mmt
from Pages.Buses_page import Buses_mmt

class Test_mmt_busespage(BasePageFragments):




    @allure.title("buses page smoke test")
    @allure.description("To verify all the elements are loaded in the buses search page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.buspage 
    @pytest.mark.smoke

    def test_smoketest_buspage(self):
         # search for buses in homepage
        BasePageFragments.close_login_model(self)
        Homepage_mmt.bus_search(self)

        #verfiy mmt logo is visable and navigates to home page on clicking 
        Buses_mmt.logo_visability_and_navigation_in_pages(self)

