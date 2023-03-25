from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
driver.set_window_position(10, 25)
driver.set_window_size(400, 1000)
driver.get("https://www.saucedemo.com/")


class Test_Souce:

    def empty_login_and_password(self):
        sleep(1)
        userNameinput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        userNameinput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errormessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errormessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU : {testResult}")
        sleep(5)

    def empty_password(self):
        sleep(1)
        userNameinput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        userNameinput.send_keys("user")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errormessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errormessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU : {testResult}")
        sleep(5)

    def locked_out_user_and_secret_sauce(self):
        sleep(1)
        userNameinput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        userNameinput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errormessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errormessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU : {testResult}")
        sleep(5)

    def X(self):
        sleep(1)
        userNameinput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        userNameinput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errormessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errormessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU : {testResult}")
        sleep(5)

    def standard_user_secret_souce(self):
        sleep(1)
        userNameinput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(1)
        userNameinput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errormessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errormessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU : {testResult}")
        sleep(5)


test = Test_Souce()
print("Empty_Login_and_Password calisiyor.")
test.empty_login_and_password()

print("\nEmty Password calisiyor.")
test.empty_password()

print("\nstandard_user_secret_souce calisiyor.")
test.standard_user_secret_souce()

print("\nX calisiyor.")
test.X()
print("\nstandard_user_secret_souce caslisiyor")
test.standard_user_secret_souce()

while True:
    continue
