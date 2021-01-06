
#https://gatewayapi.com/app/settings/apikeys/secrets/oauth/0/

from requests_oauthlib import OAuth1Session

def get_sms_token():
    key = 'OCDi8-8qygJI87kPdE5LIb-7'
    secret = 'Z9B3kgiqFcAF4mvbqlWp@XnAYLNhDbkXBO^JtJT3'
    token = '4vPvKsoCSPO5D3ROSyG_u69XcDNXD8fjm7rC1rZs2aPqgyktoxHjVQDuWRXO6mMT'
    return key, secret, token

def send_sms(mobil_no,sender,text):
    key, secret, token = get_sms_token()
    #key = 'Create-an-API-Key'
    #secret = 'GoGenerateAnApiKeyAndSecret'
    gwapi = OAuth1Session(key, client_secret=secret)
    req = {
        'recipients': [{'msisdn': mobil_no}],
        'message': text,
        'sender': sender,
    }
    '''
    req = {
        'recipients': [{'msisdn': 4527285100}],
        'message': 'hello',
        'sender': 'sender',
    }
    '''    
    res = gwapi.post('https://gatewayapi.com/rest/mtsms', json=req)
    res.raise_for_status()

#send_sms(4527285100, 'MAGNUS FAR','skru ned')
