from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import contextlib
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Initiate the Edge browser
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver = webdriver.Edge("msedgedriver.exe")

#Maximize the window
driver.maximize_window()

#Open the google webpage
driver.get("https://www.google.com")

#Find-Element by ID
#element=driver.find_element(By.ID,"APjFqb")

#Find-Element by XPath
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")

#Enter the search value, RTS Labs in our case
value='RTS Labs'
element.send_keys(value)
element.send_keys(Keys.ENTER)
time.sleep(1)

#Search for 1st link with company name
element1=driver.find_element(By.PARTIAL_LINK_TEXT,value)
#Open the company webpage
element1.click()

time.sleep(10)

#open the Chip AI chat box
element2=driver.find_element(By.XPATH,"//*[@id=\"chatbase-bubble-button\"]/div/img")
element2.click()

time.sleep(5)

#Switch to chat box frame
#iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
driver.switch_to.frame('chatbase-bubble-window')

#Ask a question to the AI
element4 = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/form/div[2]/div[1]/textarea")
question="Where are you located?"
element4.send_keys(question)
element4.send_keys(Keys.ENTER)
#Wait added for a quick verification
time.sleep(3)


#Record the answer
element3 = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div/div[3]/div/div/div/p")
addressValue=element3.text.lower()
#print(addressValue)

#verify the answer
expectedaddressValue="4951 lake brook dr #225, glen allen, virginia 23060"
if expectedaddressValue in addressValue:
    print("Address is correct")

if expectedaddressValue not in addressValue:
    print("Address is incorrect")
