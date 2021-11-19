<h1 align="center">Coding Challenge - Users Hierarchy</h1>
<p>
</p>

<!-- TABLE OF CONTENTS -->

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>  
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>  
    <li><a href="#structure">Structure</a></li>
    <li><a href="#test-cases">Test Cases</a></li>
    <li><a href="#Progress">Progress</a></li>
    <li><a href="#Alternative-methods">Alternative Methods</a></li>
    <li><a href="#Author">Author</a></li>
   <li><a href="# Disclaimers">Disclaimers</a></li>
  </ol>
</details>

### About The Project

A function, for an arbitrary collection of roles and users, given a user Id returns a
list of ALL their subordinates

### Prerequisites

* Python - v3.9.9  
* Packages- N/A 

### Installation

Option 1:

Installation can be done by Cloning the repository into your loacl system and accessing through Pycharm. You can use any of the follwing methods to run this application

> Git Clone Https

	https://github.com/nedu96/CodingChallenge-UsersHierarchy.git
  
> Git Clone ssh

	git@github.com:nedu96/CodingChallenge-UsersHierarchy.git
  
> Git Clone CLI

	gh repo clone nedu96/CodingChallenge-UsersHierarchy
  
> After Cloning the repository you can import the file through Pycharm and follow the following steps

1. Import file into Pycharm
2. Click on the Debug and then Run 'application' Option

Option 2:

1. Download the zip file from git home
2. Extract file 
3. Open User_Hierarchy.py via Python IDLE 3.9.9

### Test Cases


> Test Case 1: 

* Input :
roles = [
{
"Id": 1,
"Name": "System Administrator",
"Parent": 0
},
{
"Id": 2,
"Name": "Location Manager",
"Parent": 1
},
{
"Id": 3,
"Name": "Supervisor",
"Parent": 2
},
{
"Id": 4,
"Name": "Employee",
"Parent": 3
},
{
"Id": 5,
"Name": "Trainer",
"Parent": 3
}
];
users = [
{
"Id": 1,
"Name": "Adam Admin",
"Role": 1
},
{
"Id": 2,
"Name": "Emily Employee",
"Role": 4
},
{
"Id": 3,
"Name": "Sam Supervisor",
"Role": 3
},
{
"Id": 4,
"Name": "Mary Manager",
"Role": 2
},
{
"Id": 5,
"Name": "Steve Trainer",
"Role": 5
}
];

getSubOrdinates(3)

* Output: [{"Id": 2,"Name": "Emily
Employee","Role": 4}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]

* Test Case: Passed

> Test Case 2 : 

* Input: getSubOrdinates(1)

* Output : [{"Id": 2,"Name": "Emily
Employee","Role": 4}, {"Id": 3,"Name": "Sam Supervisor","Role": 3},
{"Id": 4,"Name": "Mary Manager","Role": 2}, {"Id": 5, "Name": "Steve
Trainer","Role": 5}]

* Test Case: Passed


> Test Case 3 : 

* Input : getSubOrdinates(a)

* Output : invalid 

* Test Case: Failed

* Reason : Exception! invalid data type

* solution: Throw back Exception, Providing with valid data type.


### Progress

Iteration 1: 

* Create SetRoles and setUsers to recieve data from the Roles
* Run a loop to verify 'ID'
* Store the Object role that matches ID

Iteration 2:

* Run loop to verify the 'Parent' value to compare with the Users
* Store the Object role that matches Parent

Iteration 3:

* Cross verification with the Id that matches the one form the User.

Time taken: 1 day (17/11/2021)


### Alternative Methods

> Current Method


Code Efficiency : 0.00003(time)
* Code Efficiecy can vary based on Size of input.
* Perks of this method: Cost efficient
* Disadvantage  of this method: Time inefficient 
* Space Complexity : O(1)


> Alternative methods
* Using Hash Map
* Perks of this method: Time efficient
* Disadvantage  of this method: Cost inefficient 


### Author

* Name: Nedunchezia Pandia Rajan
* Mail: nedu1996@gmail.com
* github: https://github.com/nedu96
* linkedin: https://www.linkedin.com/in/nedunchezia-pandia-rajan/

### Disclaimers

N/A
