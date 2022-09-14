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
* I build this by /snap/bin/docker build . -t docker-django with input in file **Dockerfile**, and then stuck(sorry about that).

## Remote connecting
* It seems not secure website, but anyway (ALLOWED_HOSTS = ['0.0.0.0']/python3 manane.py runserver 0.0.0.0:8000), if it was mented to get access something like Heroku (double apologize)





