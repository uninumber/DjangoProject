# DjangoProject
## Actually just making empty html page was not really cool, so i did this more readable.
## Account rustofdeveloper@gmail.com/ElOUn;121s (products was binding by ip).

### This project has:
* Login/Logout/Register functional (for making reviews on products)
* GET /item/{id}
* GET /buy/{id}
* Docker build(just build(/snap/bin/docker build . -t docker-django)
* Model Order with Discount
* Admin Panel for discussions(ligraus/Xz15062004)
* remote connecting

## I'm not actually sure what explain here, cause everything was on website:)
## The most important files to check are: 
:heavy_plus_sign: **views.py (implementation of actions)**, 

:heavy_plus_sign: **productRoom(page of products)**,

:heavy_plus_sign: **admin.py (for reviews, it's actually can be implemented for making simple reviews for products)**, 

:heavy_plus_sign: **home.html**, 

:heavy_plus_sign: **success.html(after success purchase)**,

:heavy_plus_sign: **room.html(My own initiative for reviews)**

## About docker
* **I build this by**
* > /snap/bin/docker build . -t docker-django
*  **with input in file Dockerfile, and then stuck(sorry about that).**



## About functional

* **The left side consists of room themes where people can discuss about products.**
* **Also you have a search to find needed room.**
* **Available products is actually available products to buy.**
* **On the middle you have live available rooms, where you can create your own or click on it and start discuss.**
* **On the right sight you have a live comments**
* **If you want to create room or to discuss you need to create account.**

### To run on Linux/Windows.
```bash
  python3 manage.py runserver/ python manage.py runserver
```

## Feedback

**If you have any feedback, please reach out to me at** rustofdeveloper@gmail.com




