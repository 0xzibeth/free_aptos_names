import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


words_source = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt" # or any other source
response = requests.get(words_source)
words = response.text.split()
driver = webdriver.Safari() # or Chrome()
for word in words:
    try:
        url = f'https://www.aptosnames.com/domain-search/{word}'
        driver.get(url)
        time.sleep(1)
        value = driver.find_element(By.CLASS_NAME, 'css-il8357') # class `css-il8357` might need an additional check in browser Inspector and update

        if value.text == 'Available':
            print(word)
            
    except Exception:
        time.sleep(1)

driver.close()
