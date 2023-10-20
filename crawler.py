import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


words_source = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt"
response = requests.get(words_source)
words = response.text.split()
driver = webdriver.Safari()
for word in words:
    try:
        if len(word) >= 6:
            url = f'https://www.aptosnames.com/domain-search/{word}'
            driver.get(url)
            time.sleep(1)
            value = driver.find_element(By.CLASS_NAME, 'css-il8357')

            if value.text == 'Available':
                print(word)
    except Exception:
        time.sleep(1)

driver.close()
