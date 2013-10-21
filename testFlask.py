from requests import put, get ,delete ,head

#testing...
result3 = put('http://localhost:5001/flask/dannysaban4', data={'data':'666 only my milk'}).json()
print result3