from Locators.Base_locators import BaseLocators
from selenium.webdriver.common.by import By

class BusesPageLocators(BaseLocators):
        BUSES_SEARCH_BAR=(By.ID, 'busModifySearch')
        FILTERS_CONTAINER=(By.XPATH, "//div[@class='filterContainer']")
        AVAILABLE_FILTERS=(By.XPATH,"//li[@class='containerHorizontal']")   #####
        DATE_SLIDER=(By.XPATH,"//div[@class='date-slider-container noSelection pointer']")
        DEALS_BANNER=(By.XPATH,"//div[contains(class(),'slick-slide slick-active')]")
        SORT_BY=(By.XPATH,"//li[@class='activeItem' or @class='']")
        VIEW_STATEBUSES=(By.XPATH,"div[@class='stateTransWrap makeFlex pointer blackText hrtlCenter ']")
        BUSES_LIST=(By.XPATH,"//div[@class='busCardContainer ']")
        BUSES_FOUND=(By.XPATH,"//p[@class='latoBold secondaryTxt font14']")
        FROM_CITY=(By.ID, "from")  #####
        TO_CITY=(By.ID, "to")
        DEPART=(By.XPATH,"//span[@class='appendBottom8 font12 capText deepskyBlueText']")
        OTHER_DATE=(By.ID,'other_date')
        SEARCH_BUTTON=(By.XPATH,"//button[contains(text(),'Search')]")
        
