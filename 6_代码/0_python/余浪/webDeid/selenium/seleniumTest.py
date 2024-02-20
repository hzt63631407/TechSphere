from selenium import webdriver

i = 0 # 0-ie,1-chrome,2-firefox

#url = "https://www.baidu.com"
url = "https://firewallsecuritytest.58corp.com/webfp/index"
i = int(input("[0-ie(win), 1-chrome, 2-firefox, 3-safari(mac)]\ninput i: "))

def testIe(url):
    options = webdriver.IeOptions()
    options.set_capability('ie.ensureCleanSession', True)
    browser = webdriver.Ie(options=options)
    browser.get(url)
    return browser

def testChrome(url):
    browser = webdriver.Chrome()
    browser.get(url)
    return browser

def testFirefox(url):
    browser = webdriver.Firefox()
    browser.get(url)
    return browser

def testSafari(url):
    browser = webdriver.Safari()
    browser.get(url)
    return browser

browser = [testIe, testChrome, testFirefox, testSafari][i](url)
try:
    print(browser.get_log("browser"))
except:
    pass
while input("input `e` to exit: ") != "e":
    pass
browser.close()