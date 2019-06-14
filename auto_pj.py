from selenium import webdriver
import time

class auto_pj:
    def __init__(self,username,password):
        self.username = username
        self.password = password  

    def baocun(self,browser):
        time.sleep(2)
        all_handles = browser.window_handles
        browser.switch_to.window(all_handles[2])
        browser.find_element_by_id('pj0601id_3_1').click()
        browser.find_element_by_id('pj0601id_2_1').click()
        browser.find_element_by_id('pj0601id_5_1').click()
        browser.find_element_by_id('pj0601id_8_1').click()
        browser.find_element_by_id('pj0601id_4_1').click()
        browser.find_element_by_id('pj0601id_6_1').click()
        browser.find_element_by_id('pj0601id_7_1').click()
        browser.find_element_by_id('pj0601id_1_2').click()
        browser.find_element_by_id('pjbfb').clear()
        browser.find_element_by_id('pjbfb').send_keys('99')
        browser.find_element_by_id('bc').click()
        alert = browser.switch_to.alert
        time.sleep(1)
        alert.accept()
        browser.switch_to.window(all_handles[0])

    def pingjiao(self,browser):    
        time.sleep(2)
        all_handles = browser.window_handles
        browser.switch_to.window(all_handles[2])
        browser.find_element_by_id('tj').click()
        alert = browser.switch_to.alert
        time.sleep(1)
        alert.accept()
        alert = browser.switch_to.alert
        time.sleep(1)
        alert.accept()
        browser.switch_to.window(all_handles[0])


    def login(self):
        browser = webdriver.Chrome()
        browser.get("http://jwxt.upc.edu.cn/jsxsd/")
        handle1 = browser.current_window_handle
        browser.implicitly_wait(10)
        elem = browser.find_element_by_id('userAccount')
        elem.send_keys(self.username)
        elem = browser.find_element_by_id('userPassword')
        elem.send_keys(self.password)
        code = input("请手动输入验证码：")
        elem = browser.find_element_by_id('RANDOMCODE')
        elem.send_keys(code.strip())
        return browser


    def enter_pingjiao(self,browser):
        browser.find_element_by_id('btnSubmit').click()
        browser.find_element_by_class_name('block6').click()
        browser.find_element_by_xpath("//*[@id='Form1']/table/tbody/tr[2]/td[7]/a").click()
        a = input("您的评教课程总数【请输入该页面左侧最后一个序号】：")
        print("\n【模式0：完成打分并保存，可后续更改提交！】\n【模式1：已完成打分与更改，将数据提交！】")
        print("建议第一次运行使用模式0初步打分，检查后再次运行模式1进行提交！")
        mode = input("请输入您的模式：")
        # 模式0 只保存不提交
        if int(mode) == 0:
            for index in range(2,int(a)+2): 
                yiping = browser.find_element_by_xpath("//*[@id='dataList']/tbody/tr["+str(index)+"]/td[7]").text
                yitijiao = browser.find_element_by_xpath("//*[@id='dataList']/tbody/tr["+str(index)+"]/td[8]").text
                classname = browser.find_element_by_xpath("//*[@id='dataList']/tbody/tr["+str(index)+"]/td[3]").text
                print(index-1)
                if  yiping == '否' :
                    print( classname + ' 未评教！现在开始评教！')
                    browser.find_element_by_xpath("//*[@id='dataList']/tbody/tr["+str(index)+"]/td[9]/a").click()
                    self.baocun(browser)
                    print( classname + ' 已保存评教!')
                    # pingjiao()
                elif  (yitijiao == '否') and (yiping == '是'):
                    print( classname + ' 已保存未提交!\n【请注意提交！】') 
                elif  yitijiao == '是':
                    print( classname + ' 已完成评教!')
                print('-'*35)
            print('评教已完成！浏览器将在5秒后关闭！\n【请注意提交未提交的科目!如有未提交，请重新运行并选择模式1进行提交！】')
            time.sleep(5)
            browser.quit()
        # 模式1 提交
        elif int(mode) == 1:
            for index in range(2,int(a)+2): 
                yiping = browser.find_element_by_xpath("//*[@id='dataList']/tbody/tr["+str(index)+"]/td[7]").text
                yitijiao = browser.find_element_by_xpath("//*[@id='dataList']/tbody/tr["+str(index)+"]/td[8]").text
                classname = browser.find_element_by_xpath("//*[@id='dataList']/tbody/tr["+str(index)+"]/td[3]").text
                print(index-1)
                if  (yitijiao == '否') and (yiping == '是') :
                    print( classname + ' 未提交！\n【现在进行提交！】')
                    browser.find_element_by_xpath("//*[@id='dataList']/tbody/tr["+str(index)+"]/td[9]/a").click()
                    self.pingjiao(browser)
                    print( classname + ' 已提交评教!')
                    print('-'*35)
                elif yitijiao == '是':
                    print( classname + ' 已完成评教!')
                else:
                    print('出错了！请关闭浏览器！')
            print('评教已完成！浏览器将在5秒后关闭！\n【所有科目均已提交！祝您好运！】')
            time.sleep(5)
            browser.quit()

    def main(self):
        browser = self.login()
        self.enter_pingjiao(browser)




if __name__ == "__main__":
    my_pj = auto_pj('1607040212','abc123456')
    my_pj.main()