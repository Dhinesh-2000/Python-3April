import json

emp={
    'id':101,
    'name':'Rahul',
    'avail':True,
    'location':None
    
}
emp_json = json.dumps(emp)
print(emp_json)
print(type(emp_json))