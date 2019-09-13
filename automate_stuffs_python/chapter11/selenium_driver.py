from selenium import webdriver

browser = webdriver.Chrome("/home/mgil/Downloads/chromedriver")
browser.get("https://www.bhdleon.com.do")

try:
    element = browser.find_element_by_link_text("Tasas de Referencia")
    element.click()
except:
    print("Error: Element not found")