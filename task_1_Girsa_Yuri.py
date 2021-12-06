import os

path = os.getcwd()
dir_name = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

def create_folder(path):
   if not os.path.exists(path):
      os.mkdir(path)

full_path = os.path.join(path, dir_name)
create_folder(full_path)


for f in folders:
   folder = os.path.join(full_path, f)
   create_folder(folder)
