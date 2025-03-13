import pytest
from Pages.Base_page import BasePageFragments
from Pages.Home_page import Homepage_mmt

class Test_mmt_homepage(BasePageFragments):

    @pytest.mark.Homepage
    @pytest.mark.smoke
    def test_homepage_elements(self):
        #close the login window after opening the webpage
        BasePageFragments.close_login_model(self)

        #verify that make my trip logo is visable and on clicking it will navigate to home page
        Homepage_mmt.logo_visibility_and_navigation(self)

        #verify that list your property hyper link is visable and avigates to new web page in another tab
        Homepage_mmt.list_your_property_hyperlink(self)

        #verify that on hovering to introduction to mybiz it should display a switch to boz popup
        Homepage_mmt.introducing_mybiz(self)

        #verify that login or create account is visable and clicking it should prompt the user to login
        Homepage_mmt.login_or_createaccount(self)

        # verify the elemtents in home page navigation bar

        # assert_equal(Homepage_mmt.get_elements_navigation_bar(self),self.homepagedata.elements_navigation_bar
