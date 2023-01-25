from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service = Service('C:\\Users\\bsmer\\Downloads\\chromedriver.exe')

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(service=service, options=options)
  driver.get('https://twitter.com/i/flow/login')
  return driver

def main():
  # ? Get user input
  twitter_username = input("What is your twitter username: ")
  twitter_password = input("What is your twitter password: ")
  twitter_tweet = input("What would you like to tweet about: ")

  driver= get_driver()
  time.sleep(6)

  # ? Type in username
  driver.find_element(by="name", value="text").click()
  driver.find_element(by="name", value="text").send_keys(twitter_username + Keys.RETURN)
  time.sleep(2)

  # ? Type in password
  driver.find_element(by="name", value="password").send_keys(twitter_password + Keys.RETURN)
  time.sleep(5)

  # ? Type tweet
  driver.find_element(by=By.CLASS_NAME, value='public-DraftStyleDefault-ltr').send_keys(twitter_tweet)
  time.sleep(2)

  # ? Click post tweet
  driver.find_element(by='xpath', value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

  # ? Go to twitter profile to view tweet
  driver.find_element(by='xpath', value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()
  time.sleep(4)
  driver.execute_script("window.scrollTo(0, 260)")
  time.sleep(4)

  # ? Click on tweet to view
  driver.find_element(by='xpath', value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/div/article/div/div/div/div[2]/div[1]').click()
  time.sleep(10)

  print(f"Successfully Posted! \nAccount: {twitter_username} \nTweet: {twitter_tweet}")

print(main())