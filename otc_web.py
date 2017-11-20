#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchAttributeException
import unittest,time,re,os
import HTMLTestRunner
import unittest

class Test(unittest.TestCase):
       
    def setUp(self):
        self.driver=webdriver.Firefox()
       
        self.verificationErrors=[]
        self.accept_next_alert=True

    def test_transaction(self):
        u"按地址转账print出来的title应该是转账明细"
        driver=self.driver
        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")

        time.sleep(3)


        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/input').send_keys("1FotmWf89WcmanDTHtoWpW8ViVobBrivPF")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys("1")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys("to xj")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[5]/div[1]/div/div/div[3]/input").send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_transaction.png")
        print driver.title
    
    def test_transaction2(self):
        u"按账户转账print出来的title应该是转账明细"
        driver=self.driver     
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")

        time.sleep(3)


        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_class_name("change").click()
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div[2]/input').send_keys('18826473795')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('sunday')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys('1')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys('to xj2')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[5]/div[1]/div/div/div[3]/input").send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_transaction2.png")
        print driver.title

    def test_my_wallet_copyaddr(self):
        u"复制钱包地址"
        driver=self.driver
        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")

        time.sleep(3)


        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/p/label').click() 
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/button').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_my_wallet_copyaddr.png")
        print driver.title
      
    def test_complain_feedback(self):
        u"申诉反馈-查看"
        driver=self.driver
        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")

        time.sleep(3)


        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[4]/div[2]/p/label').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_complain_feedback.png")
        print driver.title

    def test_to_cash(self):
        u"提现"
        driver=self.driver        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)     
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/a/p').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]/div/input').send_keys('1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('1')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/button').click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/input").send_keys("1234")
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/button').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_to_cash.png")
        print driver.title

    def test_logout(self):
        u"退出"
        driver=self.driver
        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")

        time.sleep(3)


        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[1]/div/span[2]').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_logout.png")
        print driver.title

    def test_tr_record(self):
        u"转账记录——投诉"
        driver=self.driver        
        driver.get('url')
        print 'test tr_record'
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()
        time.sleep(3)       
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[3]/div[2]/p/label').click()
        time.sleep(3)
        target = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[15]/div[3]/div[2]")
        time.sleep(2)
        driver.execute_script("arguments[0].scrollIntoView();",target)
        time.sleep(3)       
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[15]/div[3]/div[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[4]/p").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/textarea").send_keys(u"我要投诉")
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/button').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_tr_record.png")
        print driver.title

    def test_trtomyself(self):
        u"按照地址给自己转账,false为正常"
        driver=self.driver
        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)

        
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()
        time.sleep(3)       
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/input').send_keys("1AYJMXfBbmM22C1Yf9CzBdGCp3JNTvrYqT")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys("1")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys("to myself")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_trtomyself.png")
        time.sleep(2)  
        print  driver.title==u"转账详情"

    def test_account_phone_not_match(self):
        u"账户与号码不匹配，false为正常"        
        driver=self.driver        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_class_name("change").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div[2]/input').send_keys('18826473795')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('sun')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys('1')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys('to xj2')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_account_phone_not_match.png")
        time.sleep(2)
        print driver.title==u"转账详情"

    def test_trtomyself_byaccount(self):
        u"按照账户给自己转账，false为正常"        
        driver=self.driver        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_class_name("change").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div[2]/input').send_keys('phone_number')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('anryan')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys('1')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys('to xj2')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_trtomyself_byaccount.png")
        time.sleep(2)
        print driver.title==u"转账详情"
        
    def test_tr_number_exceed(self):
        u"按照账户转账，交易额超过账户总额,false为正常"
        driver=self.driver      
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_class_name("change").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div[2]/input').send_keys('18826473795')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('sunday')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys('1000')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys('to xj2')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_tr_number_exceed.png")
        time.sleep(2)
        print driver.title==u"转账详情"

    def test_tr_number_lessthan0_byaccount(self):
        u"按照账户转账，交易额小于零,true为正常"
        driver=self.driver      
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_class_name("change").click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div[2]/input').send_keys('18826xxxxx')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('sunday')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys('-100')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys('to xj2')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_tr_number_lessthan0_byaccount.png")
        time.sleep(2)
        print driver.title==u"转账"

    def test_addr_not_exist(self):
        u"按照地址转账，地址不存在，false为正常"
        driver=self.driver
        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")

        time.sleep(3)


        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/input').send_keys("L2zK6whX31DkDvtJbZDyPUZSsH54eydEy5Y2NbKBjAARSSbdu1KK")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys("1")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys("to xj")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_addr_not_exist.png")
        time.sleep(2)
        print driver.title==u'转账详情'

    def test_trnumber_morethanaccount_byaddress(self):
        u"按照地址转账，数量超出额度，false为正常"
        driver=self.driver
        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")

        time.sleep(3)


        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/input').send_keys("1FotmWf89WcmanDTHtoWpW8ViVobBrivPF")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys("1000")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys("to xj")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_trnumber_morethanaccount_byaddress.png")
        time.sleep(2)
        print driver.title==u'转账详情'

    def test_trnumber_lessthan0_byaddr(self):
        u"按照地址转账，数量为负数，false为正常"
        driver=self.driver
        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")

        time.sleep(3)


        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)
        
        driver.find_element_by_xpath('//*[@id="account"]/div[2]/div/div/div[2]/div[2]/p/label').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div/div[3]/div/input').send_keys("1FotmWf89WcmanDTHtoWpW8ViVobBrivPF")
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div[2]/input').send_keys("-80")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/div/div[2]/input').send_keys("to xj")
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[6]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_trnumber_lessthan0_byaddr.png")
        time.sleep(2)
        print driver.title==u'转账详情'

    def test_to_cash_from_ownaccount(self):
        u"从自己账户提现，结果为false为正常"
        driver=self.driver        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)     
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/a/p').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]/div/input').send_keys('1AYJMXfBbmM22C1Yf9CzBdGCp3JNTvrYqT')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('1')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_to_cash_from_ownaccount.png")
        time.sleep(2)
        print driver.title==u"转账明细"

    def test_to_cashexceedamount_from_ownaccount(self):
        u"从账户提现金额超出最大值，结果为false为正常"
        driver=self.driver        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)     
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/a/p').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]/div/input').send_keys('1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('1000')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_to_cashexceedamount_from_ownaccount.png")
        time.sleep(2)
        print driver.title==u"转账明细"
        
    def test_to_cashillegalamount_from_ownaccount(self):
        u"从账户提现金额超出最大值，结果为false为正常"
        driver=self.driver        
        driver.get('url')
        driver.find_element_by_name("phone").send_keys("phone_number")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[2]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[1]/div[3]/input').send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="login"]/div[2]/button').click()

        time.sleep(3)     
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/a/p').click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]/div/input').send_keys('1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/input').send_keys('-100')
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/button').click()
        time.sleep(2)
        print driver.find_element_by_xpath("/html/body/div[3]/div[2]/p").text
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test\\test_to_cashillegalamount_from_ownaccount.png")
        time.sleep(2)
        print driver.title==u"转账明细"



      
               
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__=="__main__":  
    testunit=unittest.TestSuite()
    
    print 'main init finish'  
    testunit.addTest(Test("test_transaction"))
    testunit.addTest(Test("test_transaction2"))
    testunit.addTest(Test("test_my_wallet_copyaddr"))
    testunit.addTest(Test("test_complain_feedback"))
    testunit.addTest(Test("test_to_cash"))
    testunit.addTest(Test("test_logout"))
    testunit.addTest(Test("test_tr_record"))
    testunit.addTest(Test("test_trtomyself"))
    testunit.addTest(Test("test_account_phone_not_match"))
    testunit.addTest(Test("test_trtomyself_byaccount"))
    testunit.addTest(Test("test_tr_number_exceed"))
    testunit.addTest(Test("test_tr_number_lessthan0_byaccount"))
    testunit.addTest(Test("test_addr_not_exist"))
    testunit.addTest(Test("test_trnumber_morethanaccount_byaddress"))
    testunit.addTest(Test("test_trnumber_lessthan0_byaddr"))
    testunit.addTest(Test("test_to_cash_from_ownaccount"))
    testunit.addTest(Test("test_to_cashexceedamount_from_ownaccount"))
    testunit.addTest(Test("test_to_cashillegalamount_from_ownaccount"))
    filename="C:\\Users\\test\\Desktop\\test\\result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'otc_web测试结果报告',description='by anryan')
    runner.run(testunit)
    fp.close()
    











