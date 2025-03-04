
import random
from selenium.webdriver.common.by import By
from _Data.data import FlightPageData as FD
from Locators.Base_locators import Baselocators


class flightPage_locators(Baselocators):

        SEARCH_BAR=(By.ID,'widgetHeader')
        FARETYPE_BAR=(By.XPATH,"//div[@class='fareTypeWrapper']")
        FARE_TYPE=(By.XPATH,f"//span[@class='appendLeft7' and contains(text(),'{random.choice(FD.FARE_TYPES[1:])}')]")
        FILTERS_FLIGHTS=(By.XPATH,"//p[@class='filtersHeading appendBottom15']")
        JOURNEY_TITLE = (By.XPATH, "//p[contains(@class,'journey-title')]//span")
        PROMOTION_BANNER = (By.ID, "carouselBanner")
        WEEKLY_FARE_BANNER = (By.ID, 'weeklyFare')
        SORT_BY_TAB = (By.ID, "//div[@class='sortTabsWrapper appendTop20']")
        AVAILABLE_FLIGHTS = (By.XPATH, "//div[@class=' ']")
        SEARCH_BUTTON_DISABLED=(By.XPATH,"//span[@class='disable-btn-txt']")
        SEARCH_BUTTON_ENABLED=(By.ID,"search-button")
        CURRENT_TRIP_TYPE=(By.XPATH,"//div[@class='multiDropDownVal']")
        TRIP_TYPE_DROPDOWN=(By.XPATH,"//div[@class='dropDownList']")
        


