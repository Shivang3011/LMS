from selenium import webdriver
import time
import pytest


@pytest.fixture(scope="session")
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="F:\ENGINEERING\Selenium\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()


def test_launch_application(setup):
    driver.get("https://node-library-service.herokuapp.com/")
    driver.find_element_by_link_text("Sign-In as User").click()
    driver.get_screenshot_as_file('launch_app.png')
    driver.save_screenshot(r'C:\Users\Owner\PycharmProjects\Test1\LMS\Screenshots')


@pytest.mark.skip(reason="will not execute")  # this method will only execute when we remove SKIP
def test_user_register(setup):
    driver.find_element_by_link_text("Register").click()
    driver.find_element_by_id("firstName").send_keys("test")  # firstname
    driver.find_element_by_id("lastName").send_keys("test")
    driver.find_element_by_id("username").send_keys("tester@123")
    driver.find_element_by_id("gender").send_keys("male")
    driver.find_element_by_id("email").send_keys("abc@test.com")
    driver.find_element_by_id("password").send_keys("123")
    driver.find_element_by_xpath("//button[text()='Register']").click()


def test_login_as_user(setup):
    driver.find_element_by_xpath("//input[@placeholder='Enter Username']").send_keys("test")
    driver.find_element_by_xpath("//input[@placeholder='Enter Password']").send_keys("123")
    driver.find_element_by_xpath("//button[text()='Login']").click()
    driver.get_screenshot_as_file('user_login.png')
    driver.save_screenshot(r'C:\Users\Owner\PycharmProjects\Test1\LMS\Screenshots')


def test_browse_books(setup):
    driver.find_element_by_link_text("Browse Books").click()
    driver.get_screenshot_as_file('browse.png')
    driver.save_screenshot(r'C:\Users\Owner\PycharmProjects\Test1\LMS\Screenshots')


def test_issue_book(setup):
    driver.find_element_by_xpath("//div[5]//div[2]//a[1]").click()
    driver.get_screenshot_as_file('book_issue.png')
    driver.save_screenshot(r'C:\Users\Owner\PycharmProjects\Test1\LMS\Screenshots')


def test_book_details(setUp):
    driver.find_element_by_xpath("//body//div[@class='row']//div[@class='row']//div[1]//div[2]//a[2]").click()
    driver.get_screenshot_as_file('book_details.png')
    driver.save_screenshot(r'C:\Users\Owner\PycharmProjects\Test1\LMS\Screenshots')


def test_activities(setUp):
    driver.find_element_by_id("activities_page").click()
    # driver.find_element_by_link_text("Delete all activities").click()
    driver.get_screenshot_as_file('activities.png')
    driver.save_screenshot(r'C:\Users\Owner\PycharmProjects\Test1\LMS\Screenshots')
