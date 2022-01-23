import requests
import argparse
import os
from Github_Token import token


parser = argparse.ArgumentParser()
parser.add_argument("--name","-n",type=str,dest="name",required=True)
parser.add_argument("--private","-p",dest="is_private",action="store_true")
args = parser.parse_args()
repo_name = args.name
is_private = args.is_private



api = "https://api.github.com/user/repos"
if is_private:
    data = '{"name": "' + repo_name + '", "private": true}'
else:
    data = '{"name": "' + repo_name + '", "private": false}'

headers={
    "Authorization": "token "+ token,
    "Accept": "application/vnd.github.v3+json"
}

try:
    r = requests.post(api, data=data, headers=headers)
    r.raise_for_status
    print("here")
 

except requests.exceptions.RequestException as err:
    raise SystemExit(err)

try:
    repo_path='D:\\'
    os.chdir(repo_path)
    os.system("mkdir "+ repo_name)
    os.chdir(repo_path + repo_name)
    os.system("git init")
    os.system("git remote add origin git@github.com:dhruvsethi708/" + repo_name + ".git")
    os.system("echo # " + repo_name + " >> README.md")
    os.system("git add .")
    os.system('git commit -m "first commit"')
    os.system("git push -u origin master")

except FileExistsError as err:
    raise SystemExit(err)
