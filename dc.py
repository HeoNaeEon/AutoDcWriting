import asyncio
import dc_api
import requests
import random
from faker import Faker


i=0
jj=0
res = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
res2 = requests.get("https://raw.githubusercontent.com/HeoNaeEon/AutoDcWriting/refs/heads/main/ip.txt")
txt = res.text.split("\n")
txt2 = res2.text.split("\n")
pp = []

fake = Faker('ko_KR')

while i < len(txt)-1:
 nk = txt[i].split(".")
 if str(nk[0])+"."+str(nk[1]) in txt2:
  kk = ".".join(nk)
  pp.append(kk)
 i=i+1

random.shuffle(pp)

gel2 = input("ID : ")
minor2 = input("MINOR : ").lower().strip()
title2 = input("TITLE : ")
content2 = input("CONTENT : ")

print("auto writing... result in page..")

while jj < len(pp):
 print(str(jj)+"/"+str(len(pp))+" "+"("+str(pp[jj])+")")
 try:
  async def run():
   name = "ㅇㅇ"
   password  = fake.password()
   gel = gel2
   minor = minor2
   title = title2
   content = content2
   proxy = "http://"+pp[jj]
   api = dc_api.API()
   doc_id = await api.write_document(board_id=gel, title=title, contents=content, name=name, password=password,pr=proxy,is_minor=minor)
   await api.close()
  asyncio.run(run())
  jj=jj+1
 except:
  jj=jj+1
