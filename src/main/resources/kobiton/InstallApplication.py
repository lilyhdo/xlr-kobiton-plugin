from com.mashape.unirest.http import Unirest
import base64
from java.io import File
from java.io import FileInputStream
import jarray

# username = kobitonServer['username']
# apiKey = kobitonServer['password']
# filepath = ""
# filename = ""

whichApi = 'api'
userapi = username + ":" + apiKey
base64EncodedBasicAuth = base64.b64encode(userapi.encode())
basicAuth = 'Basic ' + base64EncodedBasicAuth.decode()

def generateUrl():
    response = Unirest.post('https://' + whichApi + '.kobiton.com/v1/apps/uploadUrl') \
        .header('Authorization', basicAuth) \
        .header('Content-Type', 'application/json') \
        .header('Accept', 'application/json') \
        .body("{\"filename\":" + "\"" + filename + "\"" + "}") \
        .asJson().getBody().getObject()

    print(response)
    return (response.get('url'), response.get('appPath'))

def uploadToS3(presignedUrl, filepath):
    stream = FileInputStream(File(filepath))
    fileBytes = jarray.zeros(stream.available(), "b")
    stream.read(fileBytes)
    file = File(filepath)
    if (file):
        print('I got it?')
        print(file)
    jsonResponse = Unirest.put(presignedUrl) \
        .header('Content-Type', 'application/octet-stream') \
        .header('x-amz-tagging', 'unsaved=true') \
        .body(fileBytes) \
        .asJson()
    print('final json ', jsonResponse)
    stream.close()

def createApp(appPath):
    response = Unirest.post('https://' + whichApi + '.kobiton.com/v1/apps') \
        .header('Authorization', basicAuth) \
        .header('Content-Type', 'application/json') \
        .body("{\"filename\":" + "\"" + filename + "\"" + "}") \
        .body("{\"appPath\":" + "\"" + appPath + "\"" + "}") \
        .asJson().getStatus()
    print(response)


urlAppPath = generateUrl()
uploadToS3(urlAppPath[0], filepath)
createApp(urlAppPath[1])



