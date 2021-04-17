from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("Launching Chrome")
#Opening browser
driver = webdriver.Chrome(r"C:\Users\User\PycharmProjects\Github\browsers\chromedriver.exe")
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and give value
driver.find_element_by_name("q").send_keys("https://github.com/")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath("//h3[contains(.,'Where the world builds software')]").click()
time.sleep(3)
#Clicking Sign up
driver.find_element_by_xpath("//a[contains(.,'Sign up')]").click()
#Verifying Join GitHub in Create Your Account page
driver.find_element_by_xpath("//div[contains(@class,'application-main')]/main/div/div/div[contains(.,'Join GitHub')]").click()
#Verifying the title Create your account
driver.find_element_by_xpath("//h1[contains(.,'Create your account')]").click()
#Entering existing email id
driver.find_element_by_id("user_login").send_keys("kmreddys88@gmail.com")
time.sleep(5)
enabled = driver.find_element_by_xpath("//button[contains(.,'Create account')]").is_enabled()
print(enabled)
#Veryfying Create account button is greyed for an existing user
assert enabled == False
#Clicking Sign in
time.sleep(3)
driver.find_element_by_xpath("//a[contains(.,'Sign in')]").click()
#Entering valid email id in Sign in page
time.sleep(3)
driver.find_element_by_id("login_field").send_keys("kmreddys88@gmail.com")
#Entering Incorrect password
driver.find_element_by_id("password").send_keys("Kreddy")
#Trying to sign in with incorrect password
driver.find_element_by_name("commit").click()
actualError = driver.find_element_by_xpath("//div[@class='flash flash-full flash-error ']/div").text
expectedError = "Incorrect username or password."
#Veryfying Error message for an Incorrect username or password
assert actualError == expectedError
#Clicking Forgot password
driver.find_element_by_xpath("//a[contains(.,'Forgot password')]").click()
time.sleep(3)
driver.find_element_by_id("email_field").clear()
#Entering wrong emailid in reset your password page
driver.find_element_by_id("email_field").send_keys("m.ie")
time.sleep(10)
driver.find_element_by_xpath("//a[@id='home_children_button']").click()
time.sleep(3)
#closing the browser
driver.close()


