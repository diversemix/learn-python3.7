 # Code

 ## Running

 This can be simply done via docker using:
 ```
 docker-compose build
 docker-compose up
```

Or if you want to develop locally you can always create yourself a virtualenv and run:
`python3.7 app.py`

 ## Instructions

 Once the app is running you can get back widgets by using curl, e.g.
```
curl http://localhost:5000/v1/widgets
```

Or you can create a new widget by POSTing:

```
curl -d '{"name":"fred"}' -H "Content-Type: application/json" -X POST http://localhost:5000/v1/widgets
```

