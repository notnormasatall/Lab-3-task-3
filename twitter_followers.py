'''
The following module generates a .json file based on the entered user's
nickname in Twitter.
'''

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl
import oauth


def gen_keys():
    '''
    The function saves all my keys into a dictionary for the further usage.
    '''
    return {"consumer_key": 'cqcoZExJODTpj44eoDB4fknrp',
            "consumer_secret": 'dysukoyHa516H1LEuskvjotunKuV58mak7noTDhH2k6sdqx9u4',
            "token_key": '1175713193706098689-KHZUopZ1FYaeaaEagJG8blltrZ96gt',
            "token_secret": 'yJbkeY34tajGaMXPN15uEcNHkQVz5d1Znxm1CNVg5TQyT'}


def gen_followers(nickname):
    '''
    The following function returns .json file based on an entered Twitter
    nickname.
    '''
    twtr_url = 'https://api.twitter.com/1.1/friends/list.json'

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        print('')

        if len(nickname) < 1:
            break
        url = augment(twtr_url, {'screen_name': nickname, 'count': 15})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()

        js_file = json.loads(data)

        return js_file


def augment(url, parameters):
    '''
    The function gets a certain information based on an entered url and
    developer's keys.
    '''
    secrets = gen_keys()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer,
        token=token,
        http_method='GET',
        http_url=url,
        parameters=parameters
    )

    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)

    return oauth_request.to_url()


if __name__ == "__main__":
    pass
