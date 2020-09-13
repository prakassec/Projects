import requests
import hashlib
import re

req=requests.session()
url = "http://docker.hackthebox.eu:32310/"

rget=req.get(url) #requests.session.get(url)
html=rget.content #requests.session.get(url).content

def html_tags(html):
	clean = re.compile('<.*?>')
	return re.sub(clean,'',html)

out1=html_tags(html)
out2=out1.split('string')[1]
out3=out2.rstrip()

mdhash=hashlib.md5(out3).hexdigest()

data=dict(hash=mdhash)
rpost=req.post(url=url, data=data)


print(rpost.text)
