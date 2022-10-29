from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import openpyxl


PATH = r"hakaton\driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://jusan.kz/exchange-rates")
sleep(3)


table = driver.find_elements(
    By.XPATH, '//*[@id="root"]/div/section/div[2]/div/div[3]/div/table/tbody')

data_table = []
for _ in table:
    rows = driver.find_elements(By.TAG_NAME, 'tr')
    dt = [i.text.strip().split('\n') for i in rows[1:]]
    for j in dt[0:19]:
        data_table.append(j)

df = pd.DataFrame(data_table)
df.columns = ["Currency", "Date ", "Buy", "Sell"]
print(df)

jusan_data = 'Jusan_data.xlsx'
df.to_excel(jusan_data)
print('DataFrame is written to Excel File successfully.')
