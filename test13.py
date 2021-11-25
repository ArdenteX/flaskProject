import requests
from proxyPool.conf import HEADERS

Cookie = 'acw_tc=2760779316377755700792009e9bd70b2fe68956098c6041b1a872a6c49523; TY_SESSION_ID=16bb2cbe-9882-438d-a152-6ea835a661b5; PHPSESSID=an05n4ptlb3id2jun8p5g8hud6; shoppingCartSessionId=1f40e6e51fc0112c6bd4956b972d71af; reciever_area=1006000000; utm_source=101002001000; kfz_uuid=cac3a3fa-c4c2-498c-a9be-0ad5e6b8bfb5; kfz_trace=cac3a3fa-c4c2-498c-a9be-0ad5e6b8bfb5|0|f6fbcdf193607f22|101002001000'
for i in range(0, 50):
    res = requests.get('https://www.liepin.com/', headers=HEADERS)
    print(i, ": status = ", res.status_code)
    print(res.url)