
#git_hub repo: https://github.com/nedu96/CodingChallenge-UsersHierarchy
#The function getSubOrdinates recieves input from user and the
#datas are parsed from roles and users which are provided as input.
#Inorder to get the sub Ordinates the given two sets of data are extracted based on the requirements.
#Retrive the ID based on the input provided. Find parents for roles based on the Id in Roles. Using the Id with parent
#that matches initial Users. using the ID to extract data from Users.


# sample Input Roles
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
]

#sample Input user
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
]


#setRoles to set Values for Roles
def setRoles(roles):
    return roles
    
#setRoles to set Values for Users
def setUsers(users):
    return users
    

#get subordinate values
def getSubOrdinates(values):
    
    RolesValues = setRoles(roles)

    #store objRoles dataset
    IdValues = []

    #Loop to find ID
    for id in range(len(RolesValues)):
        RoleValueId = RolesValues[id].get('Id')

        #store value in Idvalues if the ID's matches
        if RoleValueId == values:
            IdValues.append(RolesValues[id])

    
    ParentData = []
    LenOfValues = len(IdValues)
    #get Parent values from Idvalues
    ParentValues = IdValues[0].get('Parent')

    #search and store values in Parent data based on 'Parent' values
    for parent in range(len(RolesValues)):
        
        RoleValueId = RolesValues[parent].get('Id')
        if (RoleValueId) > (int(ParentValues) + 1) :
            ParentData.append(RolesValues[parent])

    #Get all Id Values from ParentData 
    IdValues = [ sub['Id'] for sub in ParentData ]
    

    RequiredUsers = []

    #get values of users
    UserValues = setUsers(users)

    #loop to run and retrive roles match it with ID
    for UserVal in range(len(UserValues)):
        ValuesUserID = UserValues[UserVal].get('Role')

        #match roles with Id
        if ValuesUserID in IdValues:
            RequiredUsers.append(UserValues[UserVal])

    #print output
    print(RequiredUsers)
            

setRoles(roles);

setUsers(users);
getSubOrdinates(1); # should return [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]
getSubOrdinates(3); # should return [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 3,"Name": "Sam Supervisor","Role": 3},{"Id": 4,"Name": "Mary Manager","Role": 2}, {"Id": 5, "Name": "SteveTrainer","Role": 5}]
