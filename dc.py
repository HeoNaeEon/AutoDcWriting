import dc_api
import requests
import random
import asyncio
from faker import Faker
import time
import string

gel = input("id : ")
minor = input("is minor? : ")
sendtxt = input("message : ")

print("auto writing... result in page..")

i=0
res = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
txt = res.text.split("\n")
fake = Faker('ko_KR')
random.shuffle(txt)

while i < len(txt):
 print(str(i)+"/"+str(len(txt)))
 try:
  async def run():
   rand_str = ""
   a = ""
   j=0
   for k in range(len(sendtxt)):
    rand_str += str(random.choice(string.ascii_uppercase + string.digits))
   lst = list(rand_str)
   finaltxt = list(sendtxt)
   while j < len(lst):
    a += finaltxt[j] + lst[j]
    j=j+1
   name = fake.name()
   password  = fake.password()
   title = a
   content = fake.company()+fake.job()
   proxy = "http://"+txt[i]
   api = dc_api.API()
   doc_id = await api.write_document(board_id=gel, title=title, contents=content, name=name, password=password,pr=proxy,is_minor=minor)
   await api.close()
  asyncio.run(run())
  i=i+1
 except:
  i=i+1

