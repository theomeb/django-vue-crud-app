# Technical test for dathena

This technical test consists in a UI platform which consumes back API to display data.

In the following lines, I'll explain how you can launch my app and what I've done to build this app.

## Getting Started
![](app-gif.gif)

### Installing

Pull this repo 
```
mkdir test && cd test
git init
git remote add origin git@github.com:theomeb/technical-test.git
git pull origin master
```

Build and launch server and database dockers
```
cd server
docker-compose up --build
```

Install front app
```
cd ../client/dathena-client
npm install
```

Launch front application
```
npm run serve
```

Back API is available at `localhost:8080/apidathena` and front app is running on `localhost:8000`

## What I've done

- First, I made a plan of what needed to be done to succeed in building this app. To do so, I used Trello to set up the architecture and the tasks I had to do to implement it. *If you're interested to see it, I can grant you access to it, just ask me !*

    - This plan was made of three big parts : the first one was setting the back part, i.e a **dockerized Django REST app** as required, then I needed to connect it to a database (I've chosen **PostGreSQL**) and ultimately, I had to set up a UI interface (I've taken **VueJS** as front framework, with **Vuetify** as components library).

    - I've then followed the steps I made myself to always be clear on where I was and what I had to do to continue. 

- I used git and Github to make clear commits along the way. 

### Architecture
#### Back

- I've created models to store the provided json files into tables. The route `apidathena/init/` initialize the tables with the JSON data files. 
- CORS is enabled.
- I've created routes to retrieve data from the three databases and routes to make actions on these databases, here is a sum-up of exposed API endpoints `apidathena/<route>`: 

| Routes                | Role                          | Parameters                                             | Response              |
|-----------------------|-------------------------------|--------------------------------------------------------|-----------------------|
| `GET /language`       | Retrieve LANGUAGE data        |                                                        | Data                  |
| `GET /confidentiality`| Retrieve CONFIDENTIALITY data |                                                        | Data                  |
| `GET /doctype`        | Retrieve DOCTYPE data         |                                                        | Data                  |
| `GET /edit`           | Edit one row in a table       | table, name_to_changed, name, total_docs (,short_name) | Success/Error message |
| `GET /create`         | Create one row in a table     | table, name, total_docs (,short_name)                  | Success/Error message |
| `GET /delete`         | Delete one row in a table     | table, name                                            | Success/Error message |
| `GET /`               | Entry API                     | name=YourName                                          | Welcome page          |

- If you want to manage the data directly with Django REST, exec `python manage.py createsuperuser --email admin@example.com --username admin` in the docker, set your password and get on `/apidathena/admin` with your credentials. 

#### Front 

- I've created one component `DathenaBoard.vue` in which all the code for displaying data is made. 
- I used vuetify table component to display data easily.
- In `<script>` part, you can see all the javascript logic to get data or trigger the API. 

### Possible improvements
- **Ultime goal** : create DOCUMENTS table with fields related to other tables as the language, the document type or the confidentiality and make joints between them to retrieve data. 
- I only used GET requests because API is simple, it's better to use PUT, especially if data becomes more complex. 
- Security : the requests should be secured. 
    - Either with authentication or with token between front and back, because today everybody can init the database for example.
    - Make a restricted CORS policy could also improve the security.


## Authors

* **Théomé Borck** - *Technical test* - [Github Repo](https://github.com/theomeb/technical-test)

You can check my trello board that I used to make this project - [Trello Project](https://trello.com/b/3A9mFMes/test-full-stack-dathena)
