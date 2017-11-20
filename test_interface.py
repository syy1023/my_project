#coding=utf-8
import requests
import json
import unittest
import unittest,time,re,os
import HTMLTestRunner

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.url="http://192.168.0.48:8332"
        self.header = {"Authorization": "Basic UlBDdXNlcjoxMjM0NTY="}
        self.auth = ("xxx", "xxx")        
        self.verificationErrors=[]
        self.accept_next_alert=True
        
    def tearDown(self):
        self.assertEqual([],self.verificationErrors)

    
    def test_decode_the_transaction(self):
        url="http://192.168.0.121:9332"
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "decoderawtransaction", "params": ["02000000010000000344434e010000000000000000000000000000000000000000000000000000000000000000ffffffff045702ea00ffffffff020040075af0750700232103985b3037efca7d91a2ac6983774dda2a45ac678d71f90aa5f50350581a2266b3ac0000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf900000000"]}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_all_the_outputtransaction(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettxoutsetinfo", "params": [] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_info_of_thenodes(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getinfo", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_outputtransactionin(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettxout", "params": ["c2fa86c41b17d7d8e69ac47f2233ce99a8d16cdc14116bb8fa8096179d337d2e", 1] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_the_remained_amountofmoney(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getbalance", "params": ["1GLZUzNXpww1N8K1CmifGJueCynjFSqqS8"]}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_the_templates_of_blocks(self):
        url="http://192.168.0.121:9332"
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getblocktemplate", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_the_remained_amountofmoney(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "getmempoolentry", "params": ["c2fa86c41b17d7d8e69ac47f2233ce99a8d16cdc14116bb8fa8096179d337d2e"] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_get_unconfirmed_remianed_cash(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getunconfirmedbalance", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_list_the_currency_inalladdresses(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "listaddressgroupings", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_list_therecieved_money_inaddresses(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "listreceivedbyaddress", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_search_a_transaction(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "gettransaction", "params": [" 0a19ecdf40b396308a6a53dc3055d7d6e8c35b68a0b5ea7af04a89733525425f"] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_search_details_of_thewallet(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "getwalletinfo", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_show_remianedmoney_onaccounts(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"jsonrpc", "method": "listaccounts", "params": []}
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code
    def test_transfer_money_from_one_account(self):
        url=self.url
        header=self.header
        auth=self.auth
        data={"jsonrpc": "1.0", "id":"curltest", "method": "sendfrom", "params": ["hello", "1GwbxAGmEAohyYYLcgB4s3PPdGEhMigi18", 1, "DCN"] }
        r=requests.post(url=url,json=data, auth=auth)
        print r.text
        print r.status_code



if __name__=="__main__":  
    testunit=unittest.TestSuite()
    testunit.addTest(TestInterface("test_decode_the_transaction"))
    testunit.addTest(TestInterface("test_get_all_the_outputtransaction"))
    testunit.addTest(TestInterface("test_get_info_of_thenodes"))
    testunit.addTest(TestInterface("test_get_outputtransactionin"))
    testunit.addTest(TestInterface("test_get_the_remained_amountofmoney"))
    testunit.addTest(TestInterface("test_get_the_templates_of_blocks"))
    testunit.addTest(TestInterface("test_get_the_remained_amountofmoney"))
    testunit.addTest(TestInterface("test_get_unconfirmed_remianed_cash"))
    testunit.addTest(TestInterface("test_list_the_currency_inalladdresses"))
    testunit.addTest(TestInterface("test_list_therecieved_money_inaddresses"))
    testunit.addTest(TestInterface("test_search_a_transaction"))
    testunit.addTest(TestInterface("test_search_details_of_thewallet"))
    testunit.addTest(TestInterface("test_show_remianedmoney_onaccounts"))
    testunit.addTest(TestInterface("test_transfer_money_from_one_account"))
    filename="C:\\Users\\test\\Desktop\\test_interface\\result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'otc_interface测试结果报告',description='by anryan')
    runner.run(testunit)
    fp.close()

    
