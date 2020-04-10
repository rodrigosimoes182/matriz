from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://mobileapps.saude.gov.br/esus-vepi/files/unAFkcaNDeXajurGB7LChj8SgQYS2ptm/b7d2591790c7eee6abf3842983a46d92_Download_COVID19_20200404.csv")
#assert "ok" in driver.find_element_by_class_name
#elem = driver.find_element_by_xpath('//html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[6]/div[1]/img')[0]
#elem.click()
time.sleep(2)
#print(elem)
#elem.clear()
#elem.send_keys("Brazil")
#elem.send_keys(Keys.RETURN)
#assert "No results found." in driver.page_source
driver.close()