from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()   

browser.get("https://google.com")

head_ele = browser.find_element(By.CLASS_NAME, "LX3sZb")
a_tags = head_ele.find_elements(By.TAG_NAME, "a")
for a_tag in a_tags:
    link = a_tag.get_attribute("href")
    print(link)
    if link == "https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAmgQ":
        print("clicked")
        a_tag.click()
        break

email = browser.find_element(By.ID, "identifierId")
email.send_keys("kannnan@gmail.com")

browser.find_element(By.ID, "identifierNext").find_element(By.TAG_NAME, "button").click()

# browser.close()