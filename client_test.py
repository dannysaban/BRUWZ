from requests import put, get ,delete ,head

#testing...
#result3 = put('http://localhost:5001/flask/dannysaban', data={'data': 'Remember only my milk'}).json()
#print result3
token = 'CAAB6QDBLXTcBAMuAVXvwrTu7LTdmSg7665cDNeZAomENTEtuIarKdR56M2f3BGwq7EgYnZBTfuBSbnAjegzh4b4eNsMP8mx5NM5Q7bhNVcgCbaOnyWO4OC7QrMtKwmvCZAIz0xv718edTr3Nw77c4fANCDBZCYxwdvoNceJZCJPuyk4ZAQG8SrHTt7nqM2hvPP5ksfgdUgaQZDZD'

try:
    resultGet = get('http://localhost:8008/login/'+token).json()
except:
    resultGet = 'problem responding to get request'
    
print resultGet 
try:
    resultPut = put('http://localhost:8008/login/'+token, 
                    data = {'fb_update': 'Married'}).json()
except:
    resultPut = 'problem responding to put request'   
 
 
  

print resultPut

# result7 =  head('http://localhost:8002/flask/dannysaban')
# print 'the response head is: %s' % result7
# 
# result7 =  get('http://localhost:8002/flask/dannysaban')
# print 'the response get is: %s' % result7.json()
# 
# result7 =  delete('http://localhost:8002/flask/dannysaban')
# print 'the response delete is: %s' % result7.json()

