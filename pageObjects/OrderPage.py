from selenium.webdriver.common.by import By


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    # find_element_by_id("country")
    country = (By.ID, "country")

    # find_element_by_link_text("India")
    India = (By.LINK_TEXT, "India")

    # find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    # find_element_by_css_selector("input[class*='btn-success']")
    purchasebtn = (By.CSS_SELECTOR, "input[class*='btn-success']")

    # find_element_by_css_selector("[class*='alert-success']")
    msgSuccess =  (By.CSS_SELECTOR, "[class*='alert-success']")

    def selectCountry(self):
        return self.driver.find_element(*OrderPage.country)

    def selectIndia(self):
        return self.driver.find_element(*OrderPage.India)

    def selectCheckbox(self):
        return self.driver.find_element(*OrderPage.checkBox)

    def clickPurchase(self):
        return self.driver.find_element(*OrderPage.purchasebtn)

    def successMessage(self):
        return self.driver.find_element(*OrderPage.msgSuccess)



