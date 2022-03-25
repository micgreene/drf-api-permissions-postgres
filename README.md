# Django REST Framework Permissions & Postgresql Database

+ *In this app I move my site closer to production grade by adding Permissions and Postgresql Database to my DRF/Docker API.*

## Feature Tasks and Requirements

+ In this project I merge the functionality of:
  + how to restrict access to portions of API data
  + how to switch over to using postgres vs sqlite

### Features - Django REST Framework

+ permissions so that only authenticated user’s have access to API.
+ custom permission so that only author of post can update or delete it.
+ ability to switch user’s directly from browsable API.

### Features - Docker

+ create Dockerfile based off python:3.8-slim
+ create docker-compose.yml to run Django app as a web service.
+ add postgres 11 as a service

### Deployed URLs

+ **Running Server:** N/A
+ **Running Clients:** N/A

### Pull Request

+ [permissions-postgres/pull/1](URL 'https://github.com/micgreene/drf-api-permissions-postgres/pull/1')

### README

+ [README.md](URL 'https://github.com/micgreene/drf-api-permissions-postgres/blob/master/README.md')
