from pprint import pprint
from jsonrpc_requests import Server
server = Server('http://localhost:37128')

server.getstatus()

server.createwallet("test1","samkorn")

# Throws "Response without a result field"
server.selectwallet("test1")

server.getwalletinfo("test1")


server.listunspentcoins()


server.getnewaddress("test receive")


server.send()
{ "payments":[ 
{"sendto": "tb1qgvnht40a08gumw32kp05hs8mny954hp2snhxcz", "amount": 15000, "label": "David" }, 
{"sendto":"tb1qpyhfrpys6skr2mmnc35p3dp7zlv9ew4k0gn7qm", "amount": 86200, "label": "Michael"} ], 
"coins":[{"transactionid":"ab83d9d0b2a9873b8ab0dc48b618098f3e7fbd807e27a10f789e9bc330ca89f7", "index":0}], 
"feeTarget":2, "password": "UserPassword" }


server.gethistory()

server.listkeys()


server.enqueue()
{ "coins": [{"transactionId": "ba70587b37ba8b4de143929994d3b8ee2810340cef23e8016020687716117a52", "index":"12"}], "password":"UserPassword"}

server.dequeue()
{ "coins": [{"transactionId": "ba70587b37ba8b4de143929994d3b8ee2810340cef23e8016020687716117a52", "index":"12"}]}

server.stop()
