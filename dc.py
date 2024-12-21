import asyncio
import dc_api
import requests
import random
from faker import Faker
import time

i=0
jj=0
z=0

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

"""
gel2 = input("ID : ")
minor2 = input("MINOR : ").lower().strip()
title2 = input("TITLE : ")
content2 = input("CONTENT : ")
"""

print("auto writing... result in page..")

while jj < len(zz):
 print(str(jj)+"/"+str(len(zz))+" "+"("+str(zz[jj])+")")
 try:
  async def run():
   name = "ㅇㅇ"
   password  = fake.password()
   gel = "loan_new1"
   minor = False
   title = "‼️당 일 100-500 / 인 증 업 체 / ㅂl 대 면 폰 테 크‼️"
   content = "✅상담문의: ㅌㄹbest0666 ㅋㅌkorea1599"
   proxy = "http://"+zz[jj]
   time.sleep(random.randrange(1,10))
   api = dc_api.API()
   doc_id = await api.write_document(board_id=gel, title=title, contents=content, name=name, password=password,pr=proxy,is_minor=minor)
   await api.close()
  asyncio.run(run())
  jj=jj+1
 except:
  jj=jj+1
