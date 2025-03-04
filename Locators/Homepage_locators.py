from selenium.webdriver.common.by import By

from Locators.Base_locators import Baselocators


class homepage_locators(Baselocators):
    LOGIN_MOBILE_NUMBER_INPUT=(By.XPATH,"//input[@placeholder='Enter Mobile Number']")
    CLOSE_LOGIN_MODAL_BUTTON=(By.XPATH,"//span[@class='commonModal__close']")
    MMT_LOGO_HOMEPAGE=(By.XPATH,"//a[@class='mmtLogo makeFlex']")
    LIST_YOUR_PROPERTY=(By.XPATH,"//li[@class='makeFlex hrtlCenter']")
    INTROUDUCING_MYBIZ=(By.ID, "showBizUpgradePopup" )
    TOOLTIP_INTROUDUCING_MYBIZ=(By.XPATH,"//p[@class='latoBlack whiteText appendBottom2']")
    LOGIN_OR_CREATEACCOUNT=(By.XPATH,"//li[@class='makeFlex hrtlCenter font10 makeRelative lhUser userLoggedOut']")

    FROM_CITY_INPUT=(By.ID,"fromCity")
    TO_CITY_INPUT=(By.ID,"toCity")
    SEARCH_INPUT_FIELD=(By.CSS_SELECTOR, '.react-autosuggest__input.react-autosuggest__input--open')
    DEPATURE=(By.ID,"departure")
    SEARCH_BUTTON=(By.XPATH,"//*[contains(@class,'primaryBtn font24 latoBold widgetSearchBtn')]")

    BUSES_ICON=(By.XPATH,"//span[@class='chNavIcon appendBottom2 chSprite chBuses inactive']")
    TRAVEL_DATE_CALENDAR = (By.ID,'travelDate')
