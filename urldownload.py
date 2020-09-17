import requests
import os
import shutil
CURR_PATH=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(CURR_PATH)
DOWNLOADS_DIR=os.path.join(BASE_DIR,'downloads')

os.makedirs(DOWNLOADS_DIR,exist_ok=True)

img_path=os.path.join(DOWNLOADS_DIR,'1.png')
url='https://cdn130.picsart.com/245444236016212.png'


#small file
r= requests.get(url,stream=True)
r.raise_for_status()
with open(img_path,'wb') as f:
    f.write(r.content)


dl_filename= os.path.basename(url)
new_dl_path=os.path.join(DOWNLOADS_DIR,dl_filename)

#all kinds
with requests.get(url, stream=True) as r:
    with open(new_dl_path,'wb') as f:
        shutil.copyfileobj(r.raw,f)

