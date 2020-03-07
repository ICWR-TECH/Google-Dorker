print("""
#################
# Google Dorker #
# R&D ICWR      #
#################
""")

import re,sys,requests,fake_useragent

class crawling():

    def __init__(self):
        pass

    def get_page(self,dork,page,ua):
        try:
            x=requests.get(url="https://www.google.com/search?q="+dork+"&start="+str(page)+"0",headers={"User-Agent":ua})
            return x.content
        except:
            return "x"

abc=crawling(); buff="";
ua=fake_useragent.UserAgent().chrome
for x in range(int(sys.argv[2])):
    buff+=abc.get_page(sys.argv[1],x,ua)

site=re.findall("href=\"(.+?)\"",buff)
for x in site:
    link=x.split("/")
    if link[0] == "http:" or link[0] == "https:":
        if not re.search(".google.",link[2]):
            print(x)
