import asyncio
import dc_api
import random
import requests
from faker import Faker
from python_random_strings import random_strings
import time

i=0
jj=0
z=0
b=0

res = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
res2 = requests.get("https://raw.githubusercontent.com/HeoNaeEon/AutoDcWriting/refs/heads/main/ip.txt")

txt = res.text.split("\n")
txt2 = res2.text.split("\n")

pp = []
zz = []

fake = Faker('ko_KR')

while i < len(txt)-1:
 nk = txt[i].split(".")
 if str(nk[0])+"."+str(nk[1]) in txt2:
  kk = ".".join(nk)
  pp.append(kk)
 i=i+1

random.shuffle(pp)

while z < len(pp):
 nk2 = pp[z].split(":")
 if nk2[1] == "80":
  kk2 = ":".join(nk2)
  zz.append(kk2)
 z=z+1

print("auto writing... result in page..")

while jj < len(zz):
 print(str(jj)+"/"+str(len(zz))+" "+"("+str(zz[jj])+")")
 try:
  async def run():
   global b
   name = fake.name()
   password  = fake.password()  
   gel = "loan_new1"
   minor = False
   title = "‼️당 일 100-500 / 인 증 업 체 / ㅂl 대 면 폰 테 크‼️"+random_strings.random_letters(3)
   content = "✅상담문의: ㅌㄹbest0666 ㅋㅌkorea1599"+"\n"+"\n"+random_strings.random_letters(3)
   proxy = "http://"+zz[jj]
   #time.sleep(random.randrange(2,10))
   api = dc_api.API()
   doc_id = await api.write_document(board_id=gel, title=title, contents=content, name=name, password=password,pr=proxy,is_minor=minor)
   await api.close()
   if doc_id.headers["Set-Cookie"] != "":
    print("success")
    b+=1
  asyncio.run(run())
  jj=jj+1
 except:
  jj=jj+1
print("success : "+str(b))
f=open("b.txt","w")
f.write(str(b))
f.close()
