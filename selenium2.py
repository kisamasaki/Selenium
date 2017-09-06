from selenium import webdriver
browser=webdriver.Firefox()
browser.get('http://kisamasaki.com')
link_elem=browser.find_element_by_link_text('GitHubで事故紹介?')
type(link_elem)
<class 'selenium.webdriver.firefox.webelement.FirefoxWebElement'>
link_elem.click()
