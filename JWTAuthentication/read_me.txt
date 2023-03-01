to get access token and refresh hit following command on terminal -

http POST http://127.0.0.1:8000/gettoken/ username='prathamesh' password='prathamesh'
----------------------------------------------------------------------------------------------------------------------

to generate new acess token from refresh token hit following command -

http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcm
VzaCIsImV4cCI6MTY3MjM3ODczMCwiaWF0IjoxNjcyMjkyMzMwLCJqdGkiOiI1ODc4OGE2ZGI3MmU0YjczYjlmYzU4ODBiMzEwYTViMiIsInVzZXJfaWQi
OjF9.IzkABYGii9cQQCYBZPomeEa6y0Hxl3BU6h3936dWeX8"
----------------------------------------------------------------------------------------------------------------------

to check whether token is valid or not -

http POST http://127.0.0.1:8000/verifytoken/ token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzI
iwiZXhwIjoxNjcyMjkyNDUxLCJpYXQiOjE2NzIyOTIxNTEsImp0aSI6Ijc1ZTUxODQ0ZTFiYjQ2NTdhMmUyMjI1MTIwMjdkOTNkIiwidXNlcl9pZCI6MX0
.gS20zuceG-K2gMvfckqwn-8iu-8gTXAxjd6zvh3wD-E"
----------------------------------------------------------------------------------------------------------------------

to list all record using api

http POST http://127.0.0.1:8000/studentAPI/ "Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90e
XBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMjk1NDI4LCJpYXQiOjE2NzIyOTUxMjgsImp0aSI6ImUzYzgwZmFlOWNhNjQ3YTBiYWMyMzZlZmU5NTJmNjk1IiwidXNlcl9pZCI6MX0.Jv5vJD4nbQLjryYadmQdBHNjHdHA
8IUHOLOYd8Qp3WE"
----------------------------------------------------------------------------------------------------------------------

to post data using api
http -f POST http://127.0.0.1:8000/studentAPI/ roll_no=107 name=Shivam city=Ambap "Authorization:Bearer eyJhbGciOiJI
UzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMjk1Nzk3LCJpYXQiOjE2NzIyOTU0OTcsImp0aSI6IjJiZDE1ZTA4NjFhOTRlZjA5M2NmMTczMGFkOTA4YTllIiwidXNlcl
9pZCI6MX0.98ABqY4pt5mUB8WF5IUcQqbQ6qLWg0FcSgZZgXqj1Js"
----------------------------------------------------------------------------------------------------------------------

to put data using api
http PUT http://127.0.0.1:8000/studentAPI/ roll_no=107 name=Shivam city=Ambap-Kolhapur "Authorization:Bearer eyJhbGciOiJI
UzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMjk1Nzk3LCJpYXQiOjE2NzIyOTU0OTcsImp0aSI6IjJiZDE1ZTA4NjFhOTRlZjA5M2NmMTczMGFkOTA4YTllIiwidXNlcl
9pZCI6MX0.98ABqY4pt5mUB8WF5IUcQqbQ6qLWg0FcSgZZgXqj1Js"
----------------------------------------------------------------------------------------------------------------------

to put data using api
http DELETE http://127.0.0.1:8000/studentAPI/7/ "Authorization:Bearer eyJhbGciOiJI
UzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMjk1Nzk3LCJpYXQiOjE2NzIyOTU0OTcsImp0aSI6IjJiZDE1ZTA4NjFhOTRlZjA5M2NmMTczMGFkOTA4YTllIiwidXNlcl
9pZCI6MX0.98ABqY4pt5mUB8WF5IUcQqbQ6qLWg0FcSgZZgXqj1Js"
