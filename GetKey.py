def genToken(appid):
    import json
    import datetime
    import time
    import calendar
    import requests
    from jwt import (
    JWT,
    jwk_from_pem,
)
    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    exp = calendar.timegm(exp.timetuple())
    message = {
        'iat': int(time.time()),
        'exp': exp,
        'iss': 39888,
    }
    with open('now-deploy.pem', 'rb') as fh:
        signing_key = jwk_from_pem(fh.read())
    jwt = JWT()
    compact_jws = jwt.encode(message, signing_key, 'RS256')
    data = {'Authorization': f'Bearer {compact_jws}',
            'Accept': 'application/vnd.github.machine-man-preview+json'}
    r = requests.post(url = f"https://api.github.com/app/installations/{appid}/access_tokens", headers = data) 
    data = r.json()
    token = data["token"]
    return token