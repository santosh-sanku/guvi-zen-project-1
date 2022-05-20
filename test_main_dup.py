from lib2to3.pgen2 import driver
from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pytest
from main import santosh

def test_open_login():
    driver = webdriver.Firefox()
    driver.get('https://www.zenclass.in/login')
    driver.find_element(by=By.NAME, value="email").send_keys("sankusantoshkuamr@gmail.com")
    driver.find_element(by=By.NAME, value="password").send_keys("Santosh@123")
    driver.find_element(by=By.NAME, value="login").click()
    driver.close()
    assert TRUE
    

