from selenium import webdriver
from selenium.common import exceptions
driver = webdriver.Chrome()
driver.get("https://www.fold3.com/search#query=Richard+Farr&ocr=false&t=830")
element = driver.find_elements_by_class_name("record-content")

for i in element:
    try: 
        print("I before",i)
        count = count+1
        print(count)
        i.click()
        print("Here I am")
        driver.back()
        #element = driver.find_elements_by_partial_link_text("Richard") 
        print("I after ",i)       
    except exceptions.StaleElementReferenceException:
        pass