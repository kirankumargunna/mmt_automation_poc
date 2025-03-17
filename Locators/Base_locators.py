from selenium.webdriver.common.by import By

class BaseLocators:
    MMT_LOGO_STICKY_HEADER=(By.XPATH,"//a[@class='chMmtLogo']")
    ICON_IN_STICKY_HEADER=(By.XPATH,"//span[@class='headerIconTextAlignment chNavText darkGreyText']")
    POPUPS=(By.CSS_SELECTOR,"button.button")

    