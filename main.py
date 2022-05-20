from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

class santosh: # created a class 
    url = "https://www.zenclass.in/"
    soup = requests.get(url)
    driver = webdriver.Firefox()

    def open_login(self): # method for login 
        username = "sankusantoshkumar94@gmail.com"
        password = "Santosh@123"
        self.driver.get(self.url)
        time.sleep(5)
        username1 = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input')
        password1 = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input')
        login_button = self.driver.find_element(by=By.XPATH, value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/button')
        username1.send_keys(username)
        password1.send_keys(password)
        time.sleep(3)
        login_button.click() #clicking the login button
        time.sleep(3)

    def open_query(self): # method for opening the query section from the left nav bar 
        query1 = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[1]/nav/ul/div[6]/li/span/div/div[2]')
        query1.click() 
        time.sleep(3)
    
    def create_query(self): # method for create query 
        query2 = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[1]/div[1]/button')
        query2.click() # to click on the create query button
        not_now = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[1]/img')
        time.sleep(3)
        not_now.click() # to click on the close button on the pop up

    def inside_query(self): # method for creating the query 
        self.open_login() # called the login method 
        time.sleep(3)
        self.open_query() # called the query section method 
        time.sleep(3)
        for count in range(5): # used loop to create 5 queries, one after the other 
            self.create_query() # called the method to click on the create query button
            time.sleep(3)
            cat = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select/option[2]')
            cat.click()
            time.sleep(2)
            sub_cat = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select/option[2]')
            sub_cat.click()
            time.sleep(3)
            voice = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select/option[2]')
            voice.click()
            time.sleep(2)
            q_t = "Guvi Python AT - 1 &2 Automation Project"
            q_d = "This is a Project Test Code Running for the Python Automation - 1&2 Project Given by mentor Mr. Suman Gangopadhyay."
            q_t1 = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/input')
            q_d2 = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea')
            q_t1.send_keys(q_t)
            q_d2.send_keys(q_d)
            submit_button2 = self.driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button')
            submit_button2.click()
            time.sleep(3)
            count = count + 1 # iteration for the loop

s = santosh() # created an object for the class 

s.inside_query() # calling the method using the class object 






