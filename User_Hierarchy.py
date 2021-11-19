
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

def setRoles(roles):
    return roles
    
    
def setUsers(users):
    return users
    


def getSubOrdinates(values):
    RolesValues = setRoles(roles)
    required_values = []
    print(required_values)
    for i in range(len(RolesValues)):
        values_id = RolesValues[i].get('Id')
        if values_id == values:
            required_values.append(RolesValues[i])
    print (required_values)
    required_parent = []
    LenOfValues = len(required_values)
    values_Parent = required_values[0].get('Parent')
    print(values_Parent)
    for j in range(len(RolesValues)):
        #print(required_values[i])
        values_id = RolesValues[j].get('Id')
        if (values_id) > (int(values_Parent) + 1) :
            required_parent.append(RolesValues[j])
    print(required_parent)
    res = [ sub['Id'] for sub in required_parent ]
    print(res)

    required_users = []
    UserValues = setUsers(users)
    for k in range(len(UserValues)):
        values_user_id = UserValues[k].get('Role')
        if values_user_id in res:
            required_users.append(UserValues[k])

    print(required_users)
            

setRoles(roles);

setUsers(users);
getSubOrdinates(1); # should return [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]
getSubOrdinates(1); # should return [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 3,"Name": "Sam Supervisor","Role": 3},{"Id": 4,"Name": "Mary Manager","Role": 2}, {"Id": 5, "Name": "SteveTrainer","Role": 5}]
