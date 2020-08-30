from selenium import webdriver
import time
import pytest


@pytest.fixture(scope="session")
def setUp():
    global driver
    driver = webdriver.Chrome(executable_path="F:\ENGINEERING\Selenium\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()


def test_launch_application(setUp):
    driver.get("https://node-library-service.herokuapp.com/")
    driver.find_element_by_link_text("Sign-In as Admin").click()


def test_admin_login(setUp):
    driver.find_element_by_xpath("//input[@placeholder='Enter Username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@placeholder='Enter Password']").send_keys("123")
    driver.find_element_by_xpath("//button[text()='Login']").click()


def test_manage_books(setUp):
    driver.find_element_by_id("manage_page").click()


def test_add_book(setUp):
    driver.find_element_by_xpath("//span[text()='Add New Book']").click()
    driver.find_element_by_id("title").send_keys("test")
    driver.find_element_by_id("author").send_keys("test")
    driver.find_element_by_id("description").send_keys("test")
    driver.find_element_by_id("stock").send_keys("test")
    driver.find_element_by_xpath("//div[@id='addEmployeeModal']//input[@class='btn btn-success']").click()


@pytest.mark.skip(reason="not execute")
def test_edit_book(setUp):
    driver.find_element_by_xpath("//div[@id='manage']//tr[1]//td[5]//a[1]//i[1]").click()


@pytest.mark.skip(reason="not execute")
def test_delete_book(setUp):
    driver.find_element_by_xpath("//div[@id='manage']//tr[1]//td[5]//a[2]//i[1]").click()


def test_issue_requests(setUp):
    driver.find_element_by_id("requests_page").click()


@pytest.mark.skip(reason="not execute")
def test_approve_requests(setUp):
    driver.find_element_by_xpath("//div[@id='requests']//a[1]//i[1]").click()


def test_reject_requests(setUp):
    driver.find_element_by_xpath("//div[@id='requests']//a[2]//i[1]").click()
