from selenium.webdriver.common.by import By

from PythonSelFramework.pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, "email")
    password = (By.XPATH, "//*[@id='exampleInputPassword1']")
    checkbox = (By.ID, "exampleCheck1")
    dropdowns = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPass(self):
        return self.driver.find_element(*HomePage.password)

    def selectCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def gotoDropdown(self):
        return self.driver.find_element(*HomePage.dropdowns)

    def selectSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def msgSucces(self):
        return self.driver.find_element(*HomePage.success)
