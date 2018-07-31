from com.mashape.unirest.http import Unirest
import base64
from java.io import File
from java.io import FileInputStream
import jarray

# username = kobitonServer['username']
# apiKey = kobitonServer['password']
# filepath = ""
# filename = ""

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

try:
    urlAppPath = generateUrl()
    uploadToS3(urlAppPath[0], filepath)
    createApp(urlAppPath[1])
    print("Your app has successfully been uploaded to the Kobiton Apps Repository. Please go to " +
    "portal.kobiton.com/apps to check your app ID.")
except:
    print("Your app has not been uploaded. Please try again or upload manually on portal.kobiton.com/apps")
