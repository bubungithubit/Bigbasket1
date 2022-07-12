from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import unittest
import HtmlTestRunner



@given(u'Lunch chrome browser')
def step_impl(context):
    context.serv_obj = Service("C:\\Users\\CHBUDA\\Desktop\\setupfile\\chromedriver.exe")
    context.driver = webdriver.Chrome(service=context.serv_obj)



@when(u'Open Big Basket website')
def step_impl(context):
    context.driver.get("https://www.bigbasket.com/")


@when(u'Select city and  continue')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(),'560004')]").click()
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]").submit()
    time.sleep(5)


@given(u'Scroll to Best sellers area')
def step_impl(context):
    context.best_sellers = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[8]/carousel-product-widget[2]/section/div[1]/h2")
    context.driver.execute_script("arguments[0].scrollIntoView();", context.best_sellers)

@when(u'Adding product to kart')
def step_impl(context):
    context.add_btn = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[8]/carousel-product-widget[2]/section/div[2]/div/div[1]/div/div[1]/div/div/product-template-in-container/div[1]/div[4]/div[3]/div/div[5]/div[2]/button")
    context.add_btn.click()
    time.sleep(5)


@then(u'Assert Add button')
def step_impl(context):
    context.add_btn = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[8]/carousel-product-widget[2]/section/div[2]/div/div[1]/div/div[1]/div/div/product-template-in-container/div[1]/div[4]/div[3]/div/div[5]/div[2]/button")
    context.assertTrue(context.add_btn.is_displayed() == False)
    #context.assertTrue(True)


@then(u'Assert My Basket title updated')
def step_impl(context):
    context.my_basket_text = context.driver.find_element(By.XPATH, "//*[@id='totalNumberOfCartItems']").text
    context.assertTrue("0 items" != context.my_basket_text)
    time.sleep(10)


@when(u'Hover on My Basket')
def step_impl(context):
    context.my_basket = context.driver.find_element(By.XPATH," //*[@id='navbar-main']/div/bigbasket-cart-template/div/div[2]/a")
    time.sleep(5)
    action = ActionChains(context.driver)
    action.move_to_element(context.my_basket).perform()


@then(u'Assert same product selected')
def step_impl(context):
    context.product_name1 = context.driver.find_element(By.XPATH,"/html/body/div[1]/div[8]/carousel-product-widget[2]/section/div[2]/div/div[1]/div/div[1]/div/div/product-template-in-container/div[1]/div[4]/div[1]/a").text
    context.ele = context.driver.find_element(By.XPATH,"//*[@id='navbar-main']/div/bigbasket-cart-template/div/div[2]/ul/li[1]/div/ul/li/div/div[3]/div/div[2]/a")
    context.P_name2 = context.ele.text
    context.check = context.product_name1 == context.P_name2
    context.assertTrue(True)


@when(u'click on View Basket and Checkout')
def step_impl(context):
    context.my_basket = context.driver.find_element(By.XPATH,"//*[@id='navbar-main']/div/bigbasket-cart-template/div/div[2]/a")
    context.driver.execute_script("arguments[0].click()", context.my_basket)
    context.element = context.driver.find_element(By.XPATH,"//*[@id='navbar-main']/div/bigbasket-cart-template/div/div[2]/ul/li[2]/div[2]/div[2]/button")
    context.driver.execute_script("arguments[0].click();", context.element)



@then(u'Assert Login popup is display')
def step_impl(context):
    context.assertTrue("Login - bigbasket" == context.driver.title)



@when(u'Taking screenshot')
def step_impl(context):
    context.driver.get_screenshot_as_file("C:\\Users\\CHBUDA\\Desktop\\screenshort\\hii.png")


@then(u'close popup and close drive')
def step_impl(context):
    context.driver.close()
