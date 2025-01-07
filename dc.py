import asyncio
import dc_api
import random
import requests
from faker import Faker

def request():
 global txt
 global txt2
 res = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
 res2 = requests.get("https://raw.githubusercontent.com/HeoNaeEon/AutoDcWriting/refs/heads/main/ip.txt")
 txt = res.text.split("\n")
 txt2 = res2.text.split("\n")

def faker():
 global fake
 fake = Faker('ko_KR')

def pp_sort():
 global pp
 pp = []
 i=0
 while i < len(txt)-1:
  nk = txt[i].split(".")
  if str(nk[0])+"."+str(nk[1]) in txt2:
   kk = ".".join(nk)
   pp.append(kk)
  i=i+1
  random.shuffle(pp)

def zz_sort():
 global zz
 zz = []
 z=0
 while z < len(pp):
  nk2 = pp[z].split(":")
  if nk2[1] == "80":
   kk2 = ":".join(nk2)
   zz.append(kk2)
  z=z+1

async def write_document(bid,tt,ct,mr):
 jj=0
 bid=bid
 tt=tt
 ct=ct
 mr=mr
 while jj < len(zz):
  try:
   print(str(jj)+"/"+str(len(zz))+" "+"("+str(zz[jj])+")")
   proxy="http://"+zz[jj]
   api = dc_api.API()
   doc_id = await api.write_document(board_id=bid, title=tt, contents=ct, name=fake.name(), password=fake.password(),pr=proxy,is_minor=mr)
   await api.close()
   if doc_id.headers["Set-Cookie"] != "":
    print("success")
   jj=jj+1
  except:
   jj=jj+1
   await api.close()

while True:
 print("AutoDcWriting... result in page")

 request()

 faker()

 pp_sort()

 zz_sort()
 
 asyncio.run(write_document("ID","Title","Content",TrueOrFalse)) #bid,tt,ct,mr
