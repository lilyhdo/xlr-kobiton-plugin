from com.mashape.unirest.http import Unirest
import base64


# username = kobitonServer['username']
# apiKey = kobitonServer['password']


userapi = username + ":" + apiKey
base64EncodedBasicAuth = base64.b64encode(userapi.encode())
basicAuth = 'Basic ' + base64EncodedBasicAuth.decode()

def generateUrl():
    response = Unirest.post('https://api.kobiton.com/v1/apps/uploadUrl') \
        .header('Authorization', basicAuth) \
        .header('Content-Type', 'application/json') \
        .header('Accept', 'application/json') \
        .body("{\"filename\":" + "\"" + filename + "\"" + "}") \
        .asJson().getBody().getObject()

    print(response)
    return (response.get('url'), response.get('appPath'))


def uploadToS3(presignedUrl, filepath):
    with open(filepath) as file:
        fileContent = file.read()
        response = Unirest.put(presignedUrl) \
            .header('Content-Type', 'application/octet-stream') \
            .header('x-amz-tagging', 'unsaved=true') \
            .body(fileContent) \
            .asJson().getStatus()
    print(response)
# .body("{\"filename\":" + "\"" + filename + "\"" + "}") \
def createApp(appPath):
    response = Unirest.post('https://api.kobiton.com/v1/apps') \
        .header('Authorization', basicAuth) \
        .header('Content-Type', 'application/json') \
        .body("{\"appPath\":" + "\"" + appPath + "\"" + "}") \
        .asString().getStatus()
    print(response)


tupleStuff = generateUrl()
uploadToS3(tupleStuff[0], filepath)
createApp(tupleStuff[1])
