from github import Github
import json
import sys
print("Github API: Write to JSON")
token=input("Enter Github token:")
g=Github(token)
try:
    g.get_user("github")
except:
    print("Invalid token!")
    sys.exit()

user=input("Enter a Github username: ")
try:
    usr=g.get_user(user)
except:
    print("User does not exist!")
    sys.exit()
print("###### profile: "+ usr.login +" ######")
print("Information from github profile from url: " + "https://api.github.com/users/" + usr.login)

# write all repositories to dict
dct_repositories={}
dct_languages={}
dct_repo_info={}
i=0
for repo in usr.get_repos():
    dct_languages[i]=repo.get_languages()
    dct_repo_info['languages']=dct_languages[i]
    dct_repo_info['stars']=repo.stargazers_count
    dct_repo_info['forks']=repo.forks
    if repo.language is not None:
        dct_repo_info['main language']=repo.language
    dct_repositories[repo.full_name]=dict(dct_repo_info)
    i+=1

dct_profile={
    'username': usr.login,
    'full name': usr.name,
    'location': usr.location,
    'company': usr.company,
    'repositories': dict(dct_repositories),
    'public repositories': usr.public_repos,
    'followers': usr.followers,
    'following': usr.following
    }

# remove null entries
for k, v in dict(dct_profile).items():
    if v is None:
        del dct_profile[k]

# writes to json file for testing
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(dct_profile, f, ensure_ascii=False, indent=4)