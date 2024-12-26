import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

service = Service("C:/Users/Tochio/Desktop/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get('https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&qid=2&pgid=440')

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "row"))
)

content = driver.page_source

soup = BeautifulSoup(content, 'html.parser')

results = []
for element in soup.find_all('div', class_="newsItem"):
    text = element.get_text(strip=True)
    if text not in results:
        results.append(text)

df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')

