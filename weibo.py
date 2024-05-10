#!/home/sk/anaconda3/envs/myenv/bin/python
import requests
import json
def get_auth_url(client_id, redirect_uri):
    encode_params=r'client_id='+client_id+r'&redirect_uri='+redirect_uri+r'&response_type=code'
    print(encode_params)
    return '%s%s?%s' % ('https://api.weibo.com/oauth2/', 'authorize',encode_params)

#https://weibo.com/?code=e272e90013044c4397f29666a7f189bd

def get_access_token(app_key, app_secret, redirect_url):
    #通过url_auth输入weibo账号进行登录
    #从登录成功后的回调url获得code
    url_auth = get_auth_url(app_key, redirect_url)
    print('[get_access_token]' + url_auth)
   
    code = input('Input code:')
    url_get_token = "https://api.weibo.com/oauth2/access_token"
 
    payload = {
    "client_id":app_key,
    "client_secret":app_secret,
    "grant_type":"authorization_code",
    "code":code,
    "redirect_uri":redirect_url
    }
    
    #获取access_token
    res = requests.post(url_get_token, data=payload)
    print(res.text)
    resj = json.loads(res.text)
    return resj['access_token']

#{"access_token":"2.00vZLWzBZmUZ3Ed69ce6ffacAh3jME","remind_in":"157679999","expires_in":157679999,"uid":"1825160335","isRealName":"true"}
def share_weibo(access_tk,text,rip):
    access_token = access_tk
    #安全域名，sina限制文本内容必须有此字段
    safe_domain = 'https://weibo.com/5296864682/profile?topnav=1&wvr=6'
    url_share = 'https://api.weibo.com/2/statuses/share.json'
    
    payload = {
        'access_token':access_token,
        'status':text + ' ' + safe_domain,
        'rip':rip
    }
    

    res = requests.post(url_share, data = payload)
    print(res.text)

#]https://api.weibo.com/oauth2/authorize?client_id=3998070531&redirect_uri=http://weibo.com&response_type=code
if __name__=='__main__':
    client_id='3998070531'
    app_secret='945625e4ea1f3fc4a70c0512f2de9ad1'
    redirect_uri='http://weibo.com'
    rip='222.90.59.186'
    #get_auth_url(client_id,redirect_uri)
    access_token=get_access_token(client_id,app_secret,redirect_uri)
    
    text = input('Input text:')
    res = share_weibo(access_token,text,rip)