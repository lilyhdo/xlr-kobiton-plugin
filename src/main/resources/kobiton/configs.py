

kobitonServerUrl = ''
username = ''
apiKey = ''

# 100 seconds
session_timeout = 100

desired_caps_android_app = {
    'sessionName':        'Automation test session',
    'sessionDescription': '',
    'deviceOrientation':  'portrait',
    'noReset':            True,
    'fullReset':          False,
    'captureScreenshots': True,
    'browserName':        'chrome',
    'deviceGroup':        'ORGANIZATION',
    'app':                'app',
    'appPackage':         'com.facebook.f8',
    'appActivity':        'com.facebook.f8.MainActivity',
    'waitAppPackage':     'com.facebook.f8',
    'udid':               'udid'
}