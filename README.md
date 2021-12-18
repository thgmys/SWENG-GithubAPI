# SWENG-GithubAPI
Repository for Github API project for CSU33012- Software Engineering module

# How to Run
You will need access to a valid Github OAuth token to use these programs

Download zip of this project: https://github.com/marklysaght/SWENG-GithubAPI.git

Make sure that Python 3.9.7 or later is installed

Install pip with the following command

```
python get_pip.py
```

Install dependencies with the following command 

```
pip install -r req.txt
```

Navigate to the root folder of the project and from there you can run any of the following.

```
python toJSON.py
```

```
python toMongo.py
```

```
python emptyMongo.py
```

```
python visualise.py
```
There is an explanation below of what each script does.

### toJSON.py 
Fetches information from the Github API about a specified user and writes it to a JSON file in the root directory

<img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/marklysaght-json.png?raw=true" alt="mongodb" width="300"/> <img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/torvalds-json.png?raw=true" alt="mongodb" width="300"/>

### toMongo.py 
Fetches information from the Github API about a specified user and writes it to a MongoDB database

<img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/mongodb%20database.png?raw=true" alt="mongodb" width="500"/>

### emptyMongo.db 
Clears the MongoDB database of all entries

### visualise.py 
Fetches information from the Github API about a specified user and visualises this data in the form of a pie chart, bar chart and gauge chart using the pygal library

### user/torvalds
<img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/pie-torvalds.png?raw=true" alt="pie" width="300"/> <img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/bar-torvalds.png?raw=true" alt="bar" width="300"/> <img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/gauge-torvalds.png?raw=true" alt="gauge" width="300"/>

### user/marklysaght
<img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/pie-marklysaght.png?raw=true" alt="pie" width="300"/> <img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/bar-marklysaght.png?raw=true" alt="pie" width="300"/> <img src="https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/gauge-marklysaght.png?raw=true" alt="pie" width="300"/>
