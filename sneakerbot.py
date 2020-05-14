import time
import requests
from selenium import webdriver


r = requests.get('https://www.nike.com/tw/launch/?s=in-stock')

url = 'https://www.nike.com/tw/launch/t/air-max-90-lahar-escape-light-cream/'

#accountINFO
uid = 'xxxxx@gmail.com'
pwd = 'xxxx'
gid = 'idnumber'

#boost browser
driver = webdriver.Chrome(executable_path = '/Users/Sugarliou/Documents/chromedriver')
driver.get(url)

memberLogin = driver.find_element_by_xpath("//button[@data-qa='top-nav-join-or-login-button']")
memberLogin.click()
time.sleep(1)

#Login
elem = driver.find_element_by_xpath("//input[@type='email']")
elem.send_keys(uid)

elem = driver.find_element_by_xpath("//input[@type='password']")
elem.send_keys(pwd)

login_submit = driver.find_element_by_xpath("//input[@value='登入']")
login_submit.click()
time.sleep(3)
#sizeshose
size_choose = driver.find_element_by_xpath("//button[contains(text(),'CM 27')]")
size_choose.click()
time.sleep(1)

size_comfirm = driver.find_element_by_css_selector("button[data-qa='add-to-cart'")
size_comfirm.click()

time.sleep(2)

#gocheckcart
cart_url = 'https://www.nike.com/tw/cart'
driver.get(cart_url)

driver.find_element_by_xpath("//button[contains(text(),'會員結帳')]").click()
driver.find_element_by_xpath("//input[@id='governmentid']").send_keys(gid)
#已閱讀聲明
driver.find_element_by_xpath("//span[@class='checkbox-checkmark']").click()
time.sleep(1)


#checkout信用卡資訊
driver.find_element_by_xpath("//button[contains(text(),'繼續至帳單')]").click()
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'繼續至付款')]").click()



