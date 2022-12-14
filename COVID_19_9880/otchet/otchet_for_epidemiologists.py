# -*- coding: utf-8 -*-
import glob
#COV-1010 Не выгружаются адреса в отчет /reports/covid-research-by-institution

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
from openpyxl import load_workbook

class OtchetForEpidemiologists(unittest.TestCase):
    def setUp(self):
        download_dir = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\otchet\\downloads_exel"
        chrome_options = webdriver.ChromeOptions()
        preferences = {"download.default_directory": download_dir,
                       "directory_upgrade": True,
                       "safebrowsing.enabled": True}
        chrome_options.add_experimental_option("prefs", preferences)
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe", options=chrome_options)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

        '''
        options = webdriver.ChromeOptions()
        #options.add_argument()
        pathdow ='C:/Users/user/PycharmProjects/TestsCovid1/COVID_19_9880/Filling_Lab_Tablets/downloads_exel'



        #self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True
        '''

        '''    
        def genlog(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not os.path.exists("Logs"):
            os.mkdir("Logs")
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'lab_planshet_1.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.lab_planshet()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    

    def test_lab_planshet(self):
        self.genlog()
    '''

    def test_otchet_for_epidemiologists(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        # driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("borisova")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt72 > div.nano.layout-tabmenu-nav > ul > li:nth-child(14) > a > div").click()
        driver.find_element_by_id("reportsForm:j_idt80:8:j_idt82").click()

        #фильтры

        driver.find_element_by_id("buildForm:j_idt81_input").click()
        driver.find_element_by_id("buildForm:j_idt81_input").clear()
        driver.find_element_by_id("buildForm:j_idt81_input").send_keys("12082021")
        driver.find_element_by_id("buildForm:j_idt83_input").click()
        driver.find_element_by_id("buildForm:j_idt83_input").clear()
        driver.find_element_by_id("buildForm:j_idt83_input").send_keys("13082021")

        driver.find_element_by_id("buildForm:j_idt84").click()
        time.sleep(2)
        #driver.find_element_by_id("buildForm:j_idt79_label").click()
        driver.find_element_by_css_selector("#buildForm\:j_idt84_panel").click()
        #driver.find_element_by_xpath("//label[@value='Ярославская область']").click()
        driver.find_element_by_css_selector(
            "#buildForm\:j_idt84_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(86) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        #driver.find_element_by_css_selector("#buildForm\:j_idt79_panel").click()
        driver.find_element_by_css_selector(
            "#buildForm\:j_idt84_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(81) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("buildForm:j_idt94:j_idt97").click()
        time.sleep(2)
        driver.find_element_by_id("buildForm:j_idt94:j_idt102:j_idt104:0:filter").click()
        driver.find_element_by_id("buildForm:j_idt94:j_idt102:j_idt104:0:filter").clear()
        driver.find_element_by_id("buildForm:j_idt94:j_idt102:j_idt104:0:filter").send_keys("ГЭ"+Keys.ENTER)
        time.sleep(2)
        #driver.find_element_by_id("buildForm:j_idt89:j_idt96").click()
        driver.find_element_by_xpath("//td[contains(text(), 'ООО \"ГЭК\"')]").click()
        '''
        driver.find_element_by_id("buildForm:j_idt89:j_idt97:j_idt99:0:filter").click()
        driver.find_element_by_id("buildForm:j_idt89:j_idt97:j_idt99:0:filter").clear()
        driver.find_element_by_id("buildForm:j_idt89:j_idt97:j_idt99:0:filter").send_keys("гбдоу детский сад №16")
        driver.find_element_by_xpath("//td[contains(text(), '196608, Санкт-Петербург, г. Пушкин, ул.Ахматовская , д.13, лит.а')]")
        driver.find_element_by_id("buildForm:j_idt89:j_idt97:j_idt98").click()
        '''
        driver.find_element_by_id("buildForm:j_idt94:j_idt107").click()
        driver.find_element_by_id("buildForm:j_idt91").click()
        time.sleep(4)
        driver.find_element_by_id("buildForm:j_idt90").click()
        time.sleep(3)

        rootpath = 'C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\otchet\\downloads_exel'
        filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
        filelist = [f for f in filelist if os.path.isfile(f)]
        newest = max(filelist, key=lambda x: os.stat(x).st_mtime)

        wb = load_workbook(newest)
        sheet_ranges = wb['information_note']
        number1 = sheet_ranges['B12'].value
        number2 = sheet_ranges['B5'].value
        number3 = sheet_ranges['B6'].value

        assert (number1 == "821I3458979")
        assert (number2 == "821I3246398" or number2 == "821I3246416")
        assert (number3 == "821I3246398" or number3 == "821I3246416")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


