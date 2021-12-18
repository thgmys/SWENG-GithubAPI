# SWENG-GithubAPI
Repository for Github API project for CSU33012- Software Engineering module

# How to Run
You will need access to a valid Github OAuth token to use these programs

Make sure that Python 3.9.7 or later is installed

Download zip of this project
Install python library "pygal" with the following command 
```
pip install pygal
```
Navigate to the root folder of the project and run the following commands:

### toJSON.py 
Fetches information from the Github API about a specified user and writes it to a JSON file in the root directory
```
python toJSON.py
```
### toMongo.py 
Fetches information from the Github API about a specified user and writes it to a MongoDB database
```
python toMongo.py
```
### emptyMongo.db 
Clears the MongoDB database of all entries
```
python emptyMongo.py
```
### visualise.py 
Fetches information from the Github API about a specified user and visualises this data in the form of a pie chart, bar chart and gauge chart using the pygal library
```
python visualise.py
```
![pie](https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/pie-torvalds.png?raw=true)
![bar](https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/bar-torvalds.png?raw=true)
![gauge](https://github.com/marklysaght/SWENG-GithubAPI/blob/main/snapshots/gauge-torvalds.png?raw=true)
