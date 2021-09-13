from selenium.webdriver.common.by import By

from PythonSelFramework.pageObjects.OrderPage import OrderPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_elements_by_css_selector(".card-title a")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    # product.find_element_by_css_selector("button[class='btn btn-info']").click()
    cardButton = (By.CSS_SELECTOR, "button[class='btn btn-info']")

    # driver.find_element_by_css_selector("input[class*='btn-success']")
    addItem = (By.CSS_SELECTOR, "button[class*='btn-success']")

    # find_element_by_css_selector("a[class*=btn-primary]")
    checkOut = (By.CSS_SELECTOR, "a[class*=btn-primary]")

    # find_element_by_xpath("//tbody/tr/td/div/div/h4/a")
    assertionOne = (By.XPATH, "//tbody/tr/td/div/div/h4/a")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardButton(self):
        return self.driver.find_elements(*CheckoutPage.cardButton)

    def checkoutItems(self):
        self.driver.find_element(*CheckoutPage.addItem).click()
        orderPage = OrderPage(self.driver)
        return orderPage

    def checkoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

    def assertOne(self):
        return self.driver.find_element(*CheckoutPage.assertionOne)
