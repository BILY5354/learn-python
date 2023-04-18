from selenium import webdriver

wd = webdriver.Chrome()

wd.get("https://www.byhy.net/")

print(wd.title)