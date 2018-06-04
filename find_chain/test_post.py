import urllib
import urllib2
import json


# urllib
protoco = "http"
host = "127.0.0.1"
port = "5002"
path = "/txion"
__header_key = 'content-type'
__header_value = 'application/json'


def get_url():
    return "{}://{}:{}{}".format(protoco,host,port,path)


def PostRequest(jsonP=None, method="POST"):
    if json and isinstance(jsonP, dict):
        body_value = json.JSONEncoder().encode(jsonP)
    else:
        body_value = json.JSONEncoder().encode({})

    print "application/json:", body_value
    request = urllib2.Request(get_url(), body_value)
    request.add_header(__header_key,__header_value)
    print "lib2 start request:{}".format(get_url(), request)

    data = ''
    if method == "POST":
        data = urllib2.urlopen(request).read()
    try:
        json.loads(data)
    except:
        return data
    else:
        return json.loads(data)


if __name__ == '__main__':
    print PostRequest(jsonP={"from":"network", "to":"Jack", "amount": 18881})