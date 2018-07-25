

username = kobitonServer['username']
apiKey = kobitonServer['password']

kobitonServerUrl = 'https://' + username + ":" + apiKey + "@api.kobiton.com/wd/hub"

session_timeout = 100

desired_caps = {
    'sessionName':        'Automation test session',
    'sessionDescription': '',
    'deviceOrientation':  'portrait',
    'captureScreenshots': True,
    'app':                'kobiton-store:9701',
    'deviceGroup':        'KOBITON',
    'deviceName':         deviceName,
    'platformName':       platformName,
    'platformVersion':    platformVersion
}

execfile()