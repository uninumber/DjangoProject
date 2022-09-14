# DjangoProject
## Actually just making empty html page was not really cool, so i did this more readable.
### This project has:
* Login/Logout/Register functional (for making reviews on products)
* GET /item/{id}
* GET /buy/{id}
* Docker build(just build(/snap/bin/docker build . -t docker-django)
* Model Order with Discount
* Admin Panel for discussions
*remote connecting

## I'm not actually sure what explain here, cause everything was on website:)
## The most important files to check are: 
* **views.py (implementation of actions)**, 
* **productRoom(page of products)**,
* **admin.py (for reviews, it actually can be implemented for making simple review of products)**, 
* **home.html**, 
* **success.html(after success purchase)**,
* **room.html(My own initiative for reviews)**

## About docker
* **I build this by**
* > /snap/bin/docker build . -t docker-django
*  **with input in file Dockerfile, and then stuck(sorry about that).

## Remote connecting
* It seems not secure website, but anyway (ALLOWED_HOSTS = ['0.0.0.0']/python3 manane.py runserver 0.0.0.0:8000), if it was mented to get access something like Heroku (double apologize)

## About functional

* **Left side consists of rooms where people can discuss about products.**
* **Also you have a search to find needed room.**
* **Available products is actually available products to buy.**
* **On the middle you have live available rooms, where you can create your own or click on it and start discuss.**
* **On the right sight you have a live comments**
* **If you want to create room or to discuss you need to create account.**

### To run on Linux/Windows.

> **python3 manage.py runserver/ python manage.py runserver.**





