
import schedule
import time
from os import listdir
import requests


global file,  I
file_path = 'D:/Documents/'
file_list = [_ for _ in listdir(file_path) if _.lower().endswith('pdf')]
I = -1
l = len(file_list)

def autoUpload():
    file = file_path+file_list[I]
    print(requests.post("http://127.0.0.1:8000/file/upload/",data={'remark':'fileType'},files={'file': open(file,'rb')}).text)
    

schedule.every(0.1).seconds.do(autoUpload)
while I<l: 
    try:
        schedule.run_pending()
        I += 1
    except Exception as e:
        print(e,I)
        break
    time.sleep(1)
# print(dict(enumerate( file_list)))
