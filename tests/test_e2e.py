import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from pageObjects.OrderPage import OrderPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        #self.driver.find_element_by_link_text("Shop").click()

        products = checkoutPage.getCardTitles()
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

        log = self.getLogger()
        log.info("getting all the card titles")
        i = -1
        for product in products:
            i = i+1
            productName = product.text
            log.info(productName)
            if productName == "Blackberry":
                checkoutPage.getCardButton()[i].click()
        checkoutPage.checkoutButton().click()

        name = checkoutPage.assertOne().text
        assert name == "Blackberry"

        self.driver.get_screenshot_as_file("screen1.png")

        orderPage = checkoutPage.checkoutItems()

        orderPage.selectCountry().send_keys("ind")

        log.info("Entering country name as ind")
        #self.driver.find_element_by_id("country").send_keys("ind")

        self.verifyLinkPresence("India")
        orderPage.selectIndia().click()
        #self.driver.find_element_by_link_text("India").click()

        # assert driver.find_element_by_id("country").get_attribute("value") == "India"
        assert orderPage.selectCountry().get_attribute("value") == "India"

        #self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        orderPage.selectCheckbox().click()

        #self.driver.find_element_by_css_selector("input[class*='btn-success']").click()
        orderPage.clickPurchase().click()
        result = orderPage.successMessage().text
        log.info("Text received from application is"+result)

        assert "Success! Thank you!" in result

        self.driver.get_screenshot_as_file("screen.png")
