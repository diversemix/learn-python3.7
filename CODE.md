# Code

[![Build Status](https://travis-ci.com/diversemix/learn-python3.7.svg?branch=master)](https://travis-ci.com/diversemix/learn-python3.7)

## Running

 This can be simply done via docker using:

```{bash}
 docker-compose build
 docker-compose up
```

Or if you want to develop locally you can always create yourself a virtualenv and run:
`python3.7 app.py`

## Instructions

Once the app is running you can get back widgets by using curl, e.g.

```{bash}
curl http://localhost:5000/v1/widgets
```

Or you can create a new widget by POSTing:

```{bash}
curl -d '{"name":"fred"}' -H "Content-Type: application/json" -X POST http://localhost:5000/v1/widgets
```
