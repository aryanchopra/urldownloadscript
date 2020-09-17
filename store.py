import os
filepath= os.path.abspath(__file__)
BASE_DIR=os.path.dirname(filepath)
files_dir= os.path.join(BASE_DIR,'images')

# if not os.path.exists(files_dir):
#     print('Invalid Path')

os.makedirs(files_dir,exist_ok=True)

my_images=range(0,12)

for i in my_images:
    fname=f'{i}.text'
    file_path=os.path.join(files_dir,fname)
    if os.path.exists(file_path):
        print(f'{fname} Already exists')
        continue
    with open(file_path,'w') as f:
        f.write(f'{i}th file')
