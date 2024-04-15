from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium_stealth import stealth

import pandas as pd
import csv

import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win64",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


driver.get('https://www.nseindia.com/')

driver.implicitly_wait(5)

linkhoverto = driver.find_element(By.ID, "link_2")
hover = ActionChains(driver)\
    .move_to_element(linkhoverto)\
        .perform()

linktoclick = driver\
    .find_element(By.LINK_TEXT, value='Pre-Open Market')\
        .click()

driver.implicitly_wait(5)

tableid = driver.find_element(By.ID, value='livePreTable')

tablesymbol = tableid.find_elements(By.CLASS_NAME, 'symbol-word-break')
tablefinal = tableid.find_elements(By.CSS_SELECTOR, 'td.bold.text-right')

driver.implicitly_wait(5)

table = []

for i in range(len(tablesymbol)):
    coulmn = {'Symbol': tablesymbol[i].text,
              'Final': tablefinal[i].text}
    table.append(coulmn)

tabledata = pd.DataFrame(table)

print(tabledata)
tabledata.to_csv('nsaindia.csv', index=False)


driver.implicitly_wait(5)
time.sleep(5)


linkhoverto1 = driver.find_element(By.ID, 'link_6')
hover1 = ActionChains(driver)\
    .move_to_element(linkhoverto1)\
        .perform()

linkhoverto2 = driver.find_element(By.XPATH, '/html/body/header/nav/div[1]/a/img')
hover2 = ActionChains(driver)\
    .move_to_element(linkhoverto2)\
        .click()\
            .perform()


driver.implicitly_wait(7)
time.sleep(7)

linkhoverto3 = driver.find_element(By.ID, 'tabList_NIFTYBANK')
hover3 = ActionChains(driver)\
    .move_to_element(linkhoverto3)\
        .click()\
            .perform()


time.sleep(8)


driver.execute_script("window.scrollTo(0, 800)")


time.sleep(6)

driver.quit()