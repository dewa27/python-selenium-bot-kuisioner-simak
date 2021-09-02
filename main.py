from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
# Menjalankan Web Browser
arrayKrs=["https://kuisioner-ng.unud.ac.id/respon_kuisioner/isi_respon_kuisioner/139?id_krs_detail=7230232","https://kuisioner-ng.unud.ac.id/respon_kuisioner/isi_respon_kuisioner/139?id_krs_detail=7230233","https://kuisioner-ng.unud.ac.id/respon_kuisioner/isi_respon_kuisioner/139?id_krs_detail=7230234","https://kuisioner-ng.unud.ac.id/respon_kuisioner/isi_respon_kuisioner/139?id_krs_detail=7230235","https://kuisioner-ng.unud.ac.id/respon_kuisioner/isi_respon_kuisioner/139?id_krs_detail=7230236","https://kuisioner-ng.unud.ac.id/respon_kuisioner/isi_respon_kuisioner/139?id_krs_detail=7230237","https://kuisioner-ng.unud.ac.id/respon_kuisioner/isi_respon_kuisioner/139?id_krs_detail=7239809"];
browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://kuisioner-ng.unud.ac.id/respon_kuisioner/isi_respon_kuisioner/139?id_krs_detail=7230230')
browser.implicitly_wait(7)
browser.find_element_by_css_selector("input[id='username']").send_keys("1905511064")
browser.find_element_by_css_selector("input[id='password']").send_keys("dreamer2712")
browser.implicitly_wait(10)
time.sleep(10)
for link in arrayKrs:
    browser.get(link);
    browser.implicitly_wait(5)
    time.sleep(5)
    for i in range(41):
        if(i==0):
            continue
        if(i==1):
            x=i*5
        else:
            x=(i+1)*5
        code='jawaban_'+str(i)+"_"+str(x);
        element="label[for='{}']".format(code)
        # print(element)
        browser.find_element_by_css_selector(element).click();
    browser.find_element_by_css_selector("input[name='jawaban[41][jawaban]'").send_keys("Bagus terus tingkatkan");
    browser.find_element_by_css_selector("button[id='btn-end'").click();
    wait = WebDriverWait(browser, 5)
    alert = wait.until(expected_conditions.alert_is_present())
    alert.accept();
    


# browser.get('www.google.com')