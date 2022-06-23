from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, string, time

# you need to install selenium first "pip install selenium" in cmd
driver_path = "C:\\Users\\YOURUSER\\Desktop\\chromedriver.exe"  # and you need chrome driver https://chromedriver.chromium.org/downloads

link = r"LINK_HERE"  # go to the post int m.facebook.com while logged out, click login, grab that link and put it here

email = "YOUR EMAIL/USERNAME"
password = "YOUR PASSWORD"

sleepbetweencomments = 10
sleepafter10comments = 50


def comment():
	while True:
		for _ in range(10):
			time.sleep(sleepbetweencomments)
			comment = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
			try:
				browser.find_element_by_id('composerInput').send_keys(comment)
			except:
				comment()
			time.sleep(3)
			try:
				browser.find_element_by_xpath('//button[@data-sigil="touchable composer-submit"]').click()
			except:
				comment()
		time.sleep(sleepafter10comments)


browser = webdriver.Chrome(driver_path)
browser.get(link)

browser.find_element_by_id("m_login_email").send_keys(email)
browser.find_element_by_id("m_login_password").send_keys(password)
browser.find_element_by_id("m_login_password").send_keys(Keys.ENTER)

comment()
