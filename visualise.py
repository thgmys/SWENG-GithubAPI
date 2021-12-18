from github import Github
import pygal
import itertools 
import collections
import sys

print("Github API Visualisation")
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

# BAR INFO
repo_names=[]
repo_stars=[]
repo_forks=[]
for repo in usr.get_repos():
    repo_stars.append(repo.stargazers_count)
    repo_forks.append(repo.forks)
    repo_names.append(repo.full_name)

# PIE INFO
lang={}
tmp={}
langkey=[]
langval=[]
Cdict = collections.defaultdict(int)
for repo in usr.get_repos():
    tmp = repo.get_languages()
    for key, val in itertools.chain(tmp.items(), lang.items()):
        Cdict[key] += val
langkey=[*dict(Cdict).keys()]
langval=[*dict(Cdict).values()]
# print(langval)
# print(langkey)

# GAUGE INFO
total_stars=0
total_forks=0
for repo in usr.get_repos():
    total_stars=total_stars+repo.stargazers_count
    total_forks=total_forks+repo.forks_count

# BAR CHART SHOWING STARS, FORKS FOR EACH REPO
barconfig = pygal.Config()
barconfig.x_label_rotation=90
barconfig.explicit_size=1000
barconfig.height=1000
barconfig.width=1000
bar_chart = pygal.Bar(barconfig)
bar_chart.title = 'Stars and forks per repository'
bar_chart.x_labels = map(str, repo_names)
bar_chart.add('stars', repo_stars)
bar_chart.add('forks', repo_forks)
bar_chart.render_in_browser()

# PIE CHART SHOWING THE LANGUAGES USED BY THE USER
pieconfig=pygal.Config()
pieconfig.explicit_size=1000
pieconfig.height=1000
pieconfig.width=1000
pie_chart=pygal.Pie(pieconfig)
pie_chart.title = f'Languages used by {usr.login}'
for i in range(0,len(langkey)):
    pie_chart.add(langkey[i],langval[i])
pie_chart.render_in_browser()

# GAUGE SHOWING TOTAL NUMBER OF FOLLOWERS, STARS, FOLLOWING, FORKS
gaugeconfig=pygal.Config()
gaugeconfig.explicit_size=1000
gaugeconfig.height=1000
gaugeconfig.width=1000
gauge_chart = pygal.Gauge(gaugeconfig)
gauge_chart.title = f'Total number of followers, following, stars and forks for {usr.login}'
gauge_chart.range = [0, max(usr.followers,usr.following,total_stars,total_forks)]
gauge_chart.add('Followers', usr.followers)
gauge_chart.add('Following', usr.following)
gauge_chart.add('Stars', total_stars)
gauge_chart.add('Forks', total_forks)
gauge_chart.render_in_browser()