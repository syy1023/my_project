#coding=utf-8
from appium import webdriver
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
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'VGVGBEAMEAS4PFNZ' #手机型号，使用adb devices可以查看
        desired_caps['appPackage'] = 'com.bullockchain.android.xxx'#app包名 打开app程序 使用adb shell dumpsys window w |findstr \/ |findstr name=
        desired_caps['appActivity'] = 'com.bullockchain.android.xxx.MainActivity'
        desired_caps["unicodeKeyboard"] = True
        desired_caps['resetKeyboard'] = True
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
       
        self.verificationErrors=[]
        self.accept_next_alert=True

    def test_transaction(self):
      
            
        u"按地址转账"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)


        
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入钱包地址\"]").send_keys(u'1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('//android.view.View/android.view.View[2]/android.view.View[1]').send_keys("1")                                                                               
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u"在app上给对方转账")
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"验证码\"]").send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"确认转出 \"]").click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_transaction.png")               
        driver.reset()
    
    def test_transaction2(self):
        u"按账户转账"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)
        
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.view.View[@content-desc=\"转账到账户\"]").click()
        time.sleep(4)
        driver.find_element_by_name(u'收款人账户').send_keys('1882647xxxx')
        time.sleep(3)
        driver.find_element_by_name(u'收款人姓名').send_keys('sunday')
        time.sleep(3)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"转账\"]/android.view.View[1]/android.view.View[2]/android.view.View[1]').send_keys('1')
                                     
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u'在app上转账到对方账户')
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"验证码\"]").send_keys("1234")
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_transaction2.png")
        driver.reset()

    def test_my_wallet_copyaddr(self):
        u"复制钱包地址"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)

        
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"我的钱包\"]').click() 
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"已复制\"]').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_my_wallet_copyaddr.png")
        driver.reset()
      
    def test_complain_feedback(self):
        u"申诉反馈-查看"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)
       
        
        driver.find_element_by_xpath('//android.view.View/android.view.View[6]/android.view.View[4]').click()                                      
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_complain_feedback.png")
        time.sleep(3)
        driver.reset()

    def test_to_cash(self):
        u"提现"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)

     
        driver.tap([(54,1734)],100)
        time.sleep(2)
        driver.find_element_by_name(u'请输入钱包地址').send_keys('1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"提现\"]/android.view.View[1]/android.view.View[1]/android.view.View[2]').send_keys('1')
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认提现 \"]').click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"验证码\"]").send_keys("1234")
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认提现 \"]').click()
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_to_cash.png")
        time.sleep(3)
        driver.reset()
        
    def test_logout(self):
        u"退出"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)

        driver.tap([(1020,309)],100)
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\logou.png")
        driver.reset() 

    def test_to_complain(self):
        u"转账记录——投诉"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(3)
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账记录\"]').click()
       
        
        time.sleep(2)
        def getSize():
            x=driver.get_window_size()['width']
            y=driver.get_window_size()['height']
            return(x,y)
        def swipeUp(t):
            l=getSize()
            x1=int(l[0]*0.5)
            y1=int(l[1]*0.9999)
            y2=int(l[1]*0.01)
            driver.swipe(x1,y1,x1,y2,t)
        swipeUp(150)
        time.sleep(3)
        driver.tap([(1000,1000)],100)
        time.sleep(2)
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"对订单有问题,订单申述\"]').click()
        time.sleep(2)
        driver.find_element_by_name(u'请输入申述内容').send_keys(u"通过app进行投诉2017110617：48：50")
        time.sleep(1)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"提交申述 \"]').click()
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_to_complain.png")
        driver.reset()

    def test_wrong_transaction_address(self):
        u"按照地址转账，输入错误转账地址"
        driver=self.driver
        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)


        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入钱包地址\"]").send_keys(u'1FotmWf89WcmanDTHtoWpW8ViVobBriFFF')
        time.sleep(2)
        driver.find_element_by_xpath('//android.view.View/android.view.View[2]/android.view.View[1]').send_keys("1")
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u"在app上给对方转账")
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"验证码\"]").send_keys("1234")
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"确认转出 \"]").click()
        time.sleep(1)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_wrong_transaction_address.png")
        driver.reset()

    def test_exceed_transaction_amount_byaddress(self):
         
        u"按照地址转账，转账数量超过余额"
        driver=self.driver
        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)


        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入钱包地址\"]").send_keys(u'1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('//android.view.View/android.view.View[2]/android.view.View[1]').send_keys("1000")
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u"在app上给对方转账")
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_exceed_transaction_amount_byaddress.png")
        driver.reset()

    def test_illegal_transaction_amount_byaddress(self):
        u"按照地址转账，转账数量不合法"
        driver=self.driver
        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)


        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入钱包地址\"]").send_keys(u'1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('//android.view.View/android.view.View[2]/android.view.View[1]').send_keys("-10")
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u"在app上给对方转账")
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_illegal_transaction_amount_byaddress.png")
        driver.reset()


    def test_phoneum_account_not_match(self):
        u"按账户转账,姓名和账户不匹配"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)
        
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.view.View[@content-desc=\"转账到账户\"]").click()
        time.sleep(4)
        driver.find_element_by_name(u'收款人账户').send_keys('1882647xxxx')
        time.sleep(3)
        driver.find_element_by_name(u'收款人姓名').send_keys('sun')
        time.sleep(3)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"转账\"]/android.view.View[1]/android.view.View[2]/android.view.View[1]').send_keys('1')                                     
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u'在app上转账到对方账户')
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_phoneum_account_not_match.png")
        driver.reset()
    def test_exceed_transaction_amount_byaccount(self):
        u"按账户转账,转账数量超过账户余额"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)
        
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.view.View[@content-desc=\"转账到账户\"]").click()
        time.sleep(4)
        driver.find_element_by_name(u'收款人账户').send_keys('1882647xxxx')
        time.sleep(3)
        driver.find_element_by_name(u'收款人姓名').send_keys('sunday')
        time.sleep(3)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"转账\"]/android.view.View[1]/android.view.View[2]/android.view.View[1]').send_keys('1000')                                     
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u'在app上转账到对方账户')
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_exceed_transaction_amount_byaccount.png")
        driver.reset()

    def test_illegal_transaction_amount_byaccount(self):
        u"按账户转账,转账数量不合法"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)
        
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.view.View[@content-desc=\"转账到账户\"]").click()
        time.sleep(4)
        driver.find_element_by_name(u'收款人账户').send_keys('1882647xxxx')
        time.sleep(3)
        driver.find_element_by_name(u'收款人姓名').send_keys('sunday')
        time.sleep(3)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"转账\"]/android.view.View[1]/android.view.View[2]/android.view.View[1]').send_keys('-10')                                     
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u'在app上转账到对方账户')
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_illegal_transaction_amount_byaccount.png")
        driver.reset()
        
    def test_transaction_tomyself_byaddress(self):
      
            
        u"按地址给自己转账"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)


        
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入钱包地址\"]").send_keys(u'1AYJMXfBbmM22C1Yf9CzBdGCp3JNTvrYqT')
        time.sleep(2)
        driver.find_element_by_xpath('//android.view.View/android.view.View[2]/android.view.View[1]').send_keys("1")                                                                               
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u"在app上给对方转账")
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_transaction_tomyself_byaddress.png")               
        driver.reset()
    
    def test_transaction2_tomyself_byaccount(self):
        u"按账户给自己转账"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)
        
        driver.find_element_by_xpath('//android.view.View[@content-desc=\"转账\"]').click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.view.View[@content-desc=\"转账到账户\"]").click()
        time.sleep(4)
        driver.find_element_by_name(u'收款人账户').send_keys('xxxxx')
        time.sleep(3)
        driver.find_element_by_name(u'收款人姓名').send_keys('anryan')
        time.sleep(3)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"转账\"]/android.view.View[1]/android.view.View[2]/android.view.View[1]').send_keys('1')
                                     
        time.sleep(3)
        driver.find_element_by_name(u'备注信息可以作为申述依据').send_keys(u'在app上转账到对方账户')
        time.sleep(3)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认转出 \"]').click()
        time.sleep(2)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_transaction2_tomyself_byaccount.png")
        driver.reset()
    def test_to_cash_from_myownaddress(self):
        u"从自己地址提现"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)

     
        driver.tap([(54,1734)],100)
        driver.tap([(54,1734)],100)
        time.sleep(2)
        driver.find_element_by_name(u'请输入钱包地址').send_keys('1AYJMXfBbmM22C1Yf9CzBdGCp3JNTvrYqT')
        time.sleep(2)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"提现\"]/android.view.View[1]/android.view.View[1]/android.view.View[2]').send_keys('1')
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认提现 \"]').click()
        time.sleep(3)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_to_cash_from_myownaddress.png")
        driver.reset()

    def test_to_cash_from_exceed_transactionamount(self):
        u"提现,数额超出最大值"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)

     
        driver.tap([(54,1734)],100)
        driver.tap([(54,1734)],100)
        time.sleep(2)
        driver.find_element_by_name(u'请输入钱包地址').send_keys('1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"提现\"]/android.view.View[1]/android.view.View[1]/android.view.View[2]').send_keys('1000')
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认提现 \"]').click()
        time.sleep(3)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_to_cash_from_exceed_transactionamount.png")
        driver.reset()

    def test_to_cash_from_illegal_amount(self):
        u"提现，数字非法"
        driver = self.driver

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.EditText[@text=\"请输入手机号码\"]").send_keys("xxxxx")

        time.sleep(3)

        driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys("1234")

        time.sleep(3)

        driver.find_element_by_xpath("//android.widget.Button[@content-desc=\"登    录 \"]").click()

        time.sleep(2)

     
        driver.tap([(54,1734)],100)
        driver.tap([(54,1734)],100)
        time.sleep(2)
        driver.find_element_by_name(u'请输入钱包地址').send_keys('1FotmWf89WcmanDTHtoWpW8ViVobBrivPF')
        time.sleep(2)
        driver.find_element_by_xpath('//android.webkit.WebView[@content-desc=\"提现\"]/android.view.View[1]/android.view.View[1]/android.view.View[2]').send_keys('1')
        time.sleep(2)
        driver.find_element_by_xpath('//android.widget.Button[@content-desc=\"确认提现 \"]').click()
        time.sleep(3)
        driver.save_screenshot("C:\\Users\\test\\Desktop\\test_app\\test_to_cash_from_illegal_amount.png")
        driver.reset()
        
               
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__=="__main__":  
    testunit=unittest.TestSuite()
    
    print 'main init finish'
    testunit.addTest(Test("test_to_complain"))
    testunit.addTest(Test("test_transaction"))
    testunit.addTest(Test("test_transaction2"))
    testunit.addTest(Test("test_my_wallet_copyaddr"))
    testunit.addTest(Test("test_complain_feedback"))
    testunit.addTest(Test("test_to_cash"))
    testunit.addTest(Test("test_logout"))
    testunit.addTest(Test("test_wrong_transaction_address"))
    testunit.addTest(Test("test_exceed_transaction_amount_byaddress"))
    testunit.addTest(Test("test_illegal_transaction_amount_byaddress"))
    testunit.addTest(Test("test_phoneum_account_not_match"))
    testunit.addTest(Test("test_exceed_transaction_amount_byaccount"))
    testunit.addTest(Test("test_illegal_transaction_amount_byaccount"))
    testunit.addTest(Test("test_transaction_tomyself_byaddress"))
    testunit.addTest(Test("test_transaction2_tomyself_byaccount"))
    testunit.addTest(Test("test_to_cash_from_myownaddress"))
    testunit.addTest(Test("test_to_cash_from_exceed_transactionamount"))
    testunit.addTest(Test("test_to_cash_from_illegal_amount"))
    
    
    filename="C:\\Users\\test\\Desktop\\test_app\\result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'otc_app测试结果报告',description='by anryan')
    runner.run(testunit)
    fp.close()
    
