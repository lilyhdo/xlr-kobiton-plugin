from com.mashape.unirest.http import Unirest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
import unittest
import time
import base64
# import sys
# sys.path.append('..')
import configs

# java libraries
import io.appium.java_client.android.AndroidDriver
import java.util.concurrent.TimeUnit
import org.openqa.selenium.WebElement
import org.openqa.selenium.remote.DesiredCapabilities
import org.testng.Assert
import org.testng.annotations.AfterTest
import org.testng.annotations.BeforeTest
import org.testng.annotations.Test

from io.appium.java_client.android import AndroidDriver
from java.util.concurrent import TimeUnit
from org.openqa.selenium import WebElement
from org.openqa.selenium.remote import DesiredCapabilities
from org.testng import Assert
from org.testng.annotations import AfterTest
from org.testng.annotations import BeforeTest
from org.testng.annotations import Test

class AndroidAppTest(unittest.TestCase):

    def setUp(self):
        self._command_executor = RemoteConnection(configs.kobitonServerUrl, resolve_ip=False)
        self._command_executor.set_timeout(configs.session_timeout)
        self.driver = webdriver.Remote(self._command_executor, configs.desired_caps)

    def setUpJavaway(self):
        driver = AndroidDriver(getAutomationUrl(), configs.desired_caps)
        driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS)

    def tearDown(self):
        self.driver.quit()

    def test_android_app(self):
        print('should do things in the app')
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='SKIP FOR NOW']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='DAY 2']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='REGISTRATION - 2 HOURS']").click()
        time.sleep(3)

        sessionId = self.driver.desired_capabilities.get('kobitonSessionId')

        userapi = username + ":" + apiKey
        base64EncodedBasicAuth = base64.b64encode(userapi.encode())
        basicAuth = 'Basic ' + base64EncodedBasicAuth.decode()
        print(sessionId)

        def updateSessionInfo(sessionId, basicAuth):
        #     headers = {
        #     'Authorization': 'Basic ' + base64EncodedBasicAuth.decode(),
        #     'Content-Type': 'application/json'
        #     }
        #     r = requests.put('https://api.kobiton.com/v1/sessions/' + str(sessionId), params={

        #     }, headers = headers)
        #     body = r.json()
        #     print(r)
        #     print(body)
            response = Unirest.put('https://api.kobiton.com/v1/sessions/' + str(sessionId))\
                .header('Authorization', basicAuth)\
                .header('Content-Type', 'application/json')\
                .asString().getStatus()
            print(response)
        updateSessionInfo(sessionId, basicAuth)

        # def getSession(base64EncodedBasicAuth, sessionId):
        #     headers = {
        #     'Authorization': base64EncodedBasicAuth,
        #     'Accept': 'application/json'
        #     }
        #     r = requests.get('https://api.kobiton.com/v1/sessions' + str(sessionId), params={

        #     }, headers = headers)
        #     print r.json()

        # def getCommands(base64EncodedBasicAuth, sessionId):
        #     headers = {
        #     'Authorization': base64EncodedBasicAuth,
        #     'Accept': 'application/json'
        #     }
        #     r = requests.get('https://api.kobiton.com/v1/sessions/' + str(sessionId) + '/commands', params={

        #     }, headers = headers)
        #     print r.json()

        # getSession(base64EncodedBasicAuth, sessionId)
        # getCommands(base64EncodedBasicAuth, sessionId)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidAppTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


