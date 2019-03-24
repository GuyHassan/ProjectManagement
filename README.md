### Sport Data Project

In this project we're working in TDD & CICD approaches.  
our features in the project are : 
	1.give us the champion team for each leagues (premier league,La liga,primeria liga,Eredivisie,champion league,bundesliga,ligue1).  
	2.give us the best scorer for each league and sort it by amount of goals.  

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python interperter
* pip
* IDE - Development envenvironment (like PyCharm)

### How to install

__Section A__
* Clone this repo to your computer :  `https://github.com/GuyHassan/ProjectManagement`

__Section B__
* Open command line . 

__Section C__
* Enter the following sentences in the CL:
```
1.  pip install re 
2.  pip install mock
3.  pip install pycodestyle
```
__Section D__
* Open the project in your IDE

## API's used

The application uses [Soccer Data- API](https://www.football-data.org/) in order to get the facts.  

The project is synchronized with:
* SemaphoreCi - An API used to implement CI/CD (Continuous Integration & Continuous Deployment)
* Heroku - A virtual production environment

## Running the tests

In order to run the test, use command line to enter the following command:
(open command line in project's directory)
```
python TestDrivenDevelopment.py
```
If all tests passed, you should see this output:
![image](https://github.com/GuyHassan/ProjectManagement/blob/master/pass%20test.jpeg)


## Using the application
Run the program with the command (you can on  CL inside the directed file) 
```
python Feature_Sport_Data.py
```
and the following output will be : 

![image](https://github.com/GuyHassan/ProjectManagement/blob/master/output1.JPG )
![image](https://github.com/GuyHassan/ProjectManagement/blob/master/output2.JPG )
