from requests import put, get ,delete ,head

#testing...
#result3 = put('http://localhost:5001/flask/dannysaban', data={'data': 'Remember only my milk'}).json()
#print result3
# token = 'CAAB6QDBLXTcBACpf4tCm93ViG9ItEkQWf3VCls6rDJWd3w4fSxS2LfbICe6SW9ZAu2K8c6bqft5xBm4vCdKraikc88fAZClDHc2yRP7OHV9SD5ZB39EpQNKvg310ZA54fwsnYA4rjWJBa2Kqp9MruVxz0PStAofslocJMwCL9lZBi7PPDsHrVkEmuKc3FzTxX8NboF70fOQZDZD'

try:
    resultGet = get('http://localhost:8188/websocket').json()
except:
    resultGet = 'problem responding to get request'
    
 
# try:
#     resultPut = put('http://localhost:8888/login/'+token, 
#                     data = {'fb_update': 'Married'}).json()
# except:
#     resultPut = 'problem responding to put request'   
 
 
  
print resultGet
# print resultPut