from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
# Menjalankan Web Browser

browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://kuisioner-ng.unud.ac.id/dashboard")
browser.implicitly_wait(15)
browser.find_element_by_css_selector("input[id='username']").send_keys("INSERT_USERNAME")
browser.find_element_by_css_selector("input[id='password']").send_keys("INSERT_PASSWORD")
browser.implicitly_wait(10)
time.sleep(10)
table_pbm=browser.find_element_by_class_name("kuisioner-pbm-table-container")
tabel_pbm_in=table_pbm.find_element_by_css_selector("table tbody")
rows = tabel_pbm_in.find_elements_by_tag_name("tr")
arrayKrs=[]
for row in rows:
    arrayKrs.append(row.find_element_by_css_selector(":last-child a").get_attribute("href"))

for link in arrayKrs:
    browser.get(link);
    browser.implicitly_wait(5)
    time.sleep(5)
    for i in range(41):
        rating=random.randint(0, 2)
        if(i==0):
            continue
        if(i==1):
            x=i*5-rating
        else:
            x=(i+1)*5-rating
        code='jawaban_'+str(i)+"_"+str(x);
        element="label[for='{}']".format(code)
        # print(element)
        browser.find_element_by_css_selector(element).click();
    browser.find_element_by_css_selector("input[name='jawaban[41][jawaban]'").clear();
    browser.find_element_by_css_selector("input[name='jawaban[41][jawaban]'").send_keys("Bagus terus tingkatkan");
    browser.find_element_by_css_selector("button[id='btn-end'").click();
    wait = WebDriverWait(browser, 5)
    alert = wait.until(expected_conditions.alert_is_present())
    alert.accept();
