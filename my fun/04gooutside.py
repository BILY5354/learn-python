from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
# 如果是 http 代理，注释掉 socks5 代理配置
# 如果是 socks5 代理，注释掉 http 代理配置
# prox.http_proxy = "127.0.0.1:10800"
# prox.ssl_proxy = "127.0.0.1:10800"
prox.socks5_proxy = "127.0.0.1:10800"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)

driver.get('https://youtube.com')

input()