from org.openqa.selenium.remote import DesiredCapabilities
import WebTest

# inputs
deviceName = ""
platformName = ""
platformVersion = ""
testScript = ""


# username = kobitonServer['username']
# apiKey = kobitonServer['password']

kobitonServerUrl = 'https://' + username + ":" + apiKey + "@api.kobiton.com/wd/hub"

session_timeout = 100

capabilities_web = DesiredCapabilities()
capabilities_web.setCapability("sessionName", "Automation test session")
capabilities_web.setCapability("sessionDescription", "")
capabilities_web.setCapability("deviceOrientation", "portrait")
capabilities_web.setCapability("browserName", "chrome")
capabilities_web.setCapability("deviceGroup", "KOBITON")
capabilities_web.setCapability("deviceName", "Galaxy J2 Prime")
capabilities_web.setCapability("platformVersion", "6.0.1")
capabilities_web.setCapability("platformName", "Android")

execfile('WebTest.py')
# send to server
# wait for server to return output
# show output!