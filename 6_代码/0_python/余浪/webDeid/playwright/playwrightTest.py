from playwright.sync_api import sync_playwright

i = 0 # 0-chromium,1-webkit,2-firefox
#url = "https://www.baidu.com"
url = "https://firewallsecuritytest.58corp.com/webfp/index"
i = int(input("[0-chromium, 1-webkit, 2-firefox]\ninput i: "))

def testChromium(url):
    with sync_playwright() as playwright:
        browser_type = playwright.chromium
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        print(page.title())
        while input("input `e` to exit: ") != "e":
            pass
        browser.close()
        return browser

def testWebkit(url):
    with sync_playwright() as playwright:
        browser_type = playwright.webkit
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        print(page.title())
        while input("input `e` to exit: ") != "e":
            pass
        browser.close()
        return browser

def testFirefox(url):
    with sync_playwright() as playwright:
        browser_type = playwright.firefox
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        print(page.title())
        while input("input `e` to exit: ") != "e":
            pass
        browser.close()
        return browser

browser = [testChromium, testWebkit, testFirefox][i](url)
