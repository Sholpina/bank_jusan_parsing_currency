from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

PATH = "C:\Windows\System32\drivers\DriverData\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://jusan.kz/exchange-rates")
sleep(2)


table = driver.find_elements(By.XPATH, '//*[@id="root"]/div/section/div[2]/div/div[3]/div/table/tbody')

data_table = []
for _ in table:
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    dt = [i.text.strip().split('\n') for i in rows[1:]]
    [data_table.append(j) for j in dt[0:19]]

df = pd.DataFrame(data_table)
df.columns=["      Currency", "Date ", "Buy", "Sell"]
print(df)
