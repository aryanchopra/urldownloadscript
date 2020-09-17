import os
import requests
import shutil


def download(url,directory,fname=None):      
    if fname=None:
        fname= os.path.basename(url)
    new_dl_path=os.path.join(directory,fname)

    #all kinds
    with requests.get(url, stream=True) as r:
        with open(new_dl_path,'wb') as f:
            shutil.copyfileobj(r.raw,f)

