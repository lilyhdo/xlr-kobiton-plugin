from com.mashape.unirest.http import Unirest
import base64

# username = kobitonServer['username']
# apiKey = kobitonServer['password']
# model = kobitonServer['model']

userapi = username + ":" + apiKey
base64EncodedBasicAuth = base64.b64encode(userapi.encode())
basicAuth = 'Basic ' + base64EncodedBasicAuth.decode()

jsonListDevice = Unirest.get('https://api.kobiton.com/v1/devices')\
    .header('Authorization', basicAuth)\
    .header('Accept', 'application/json').asJson().getBody().getObject()

devices = {}
deviceTemplate = "{deviceName} | {platformName} | {platformVersion}"


if model == '':
    for cloudDevice in jsonListDevice.get('cloudDevices'):
        if not cloudDevice.get('isBooked'):
            devices[cloudDevice.get('udid')[:10]] = deviceTemplate.format(
                deviceName=cloudDevice.get('deviceName'),
                platformName=cloudDevice.get('platformName'),
                platformVersion=cloudDevice.get('platformVersion'))

else:
    for cloudDevice in jsonListDevice.get('cloudDevices'):
        if not cloudDevice.get('isBooked'):
            if cloudDevice.get('deviceName') == model:
                devices[cloudDevice.get('udid')[:10]] = deviceTemplate.format(
                    deviceName=cloudDevice.get('deviceName'),
                    platformName=cloudDevice.get('platformName'),
                    platformVersion=cloudDevice.get('platformVersion'))

if devices == {}:
    print("No devices matching your desired model were available.")

print(devices)
