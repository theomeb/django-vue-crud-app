# Base application template
## Dockerized Django REST back - VueJS front

You often need to have a init template to launch a basic application which uses a front UI displaying data fetched from a back framework. Looking for this kind of template on Google, I didn't find what I needed, so I created it.

In the following lines, I'll explain how you can launch my app and how it is structured. 

## Getting Started
![](app-gif.gif)

### Installing

Pull this repo 
```
mkdir test && cd test
git init
git remote add origin git@github.com:theomeb/django-vue-crud-app.git
git pull origin master
```

Build and launch server and database dockers
```
cd server
docker-compose up --build
```

Install front app
```
cd ../client/emoeth-client
npm install
```

Launch front application
```
npm run serve
```

Back API is available at `localhost:8080/apiemoeth` and front app is running on `localhost:8000`

### Architecture
The front UI consumes API routes of a dockerized Django REST back using PostGreSQL as database.
The database consists in three tables that gather data on document type, on language and on confidentiality.

#### Back

- I've created models to store the provided json files into tables. The route `apiemoeth/init/` initialize the tables with the JSON data files. 
- CORS is enabled.
- I've created routes to retrieve data from the three databases and routes to make actions on these databases, here is a sum-up of exposed API endpoints `apiemoeth/<route>`: 

| Routes                | Role                          | Parameters                                             | Response              |
|-----------------------|-------------------------------|--------------------------------------------------------|-----------------------|
| `GET /language`       | Retrieve LANGUAGE data        |                                                        | Data                  |
| `GET /confidentiality`| Retrieve CONFIDENTIALITY data |                                                        | Data                  |
| `GET /doctype`        | Retrieve DOCTYPE data         |                                                        | Data                  |
| `GET /edit`           | Edit one row in a table       | table, name_to_changed, name, total_docs (,short_name) | Success/Error message |
| `GET /create`         | Create one row in a table     | table, name, total_docs (,short_name)                  | Success/Error message |
| `GET /delete`         | Delete one row in a table     | table, name                                            | Success/Error message |
| `GET /`               | Entry API                     | name=YourName                                          | Welcome page          |

- If you want to manage the data directly with Django REST, exec `python manage.py createsuperuser --email admin@example.com --username admin` in the docker, set your password and get on `/apiemoeth/admin` with your credentials. 

#### Front 

- I've created one component `Board.vue` in which all the code for displaying data is made. 
- I used vuetify table component to display data easily.
- In `<script>` part, you can see all the javascript logic to get data or trigger the API. 

### Possible improvements
- **Ultime goal** : create DOCUMENTS table with fields related to other tables as the language, the document type or the confidentiality and make joints between them to retrieve data. 
- I only used GET requests because API is simple, it's better to use PUT, especially if data becomes more complex. 
- Security : the requests should be secured. 
    - Either with authentication or with token between front and back, because today everybody can init the database for example.
    - Make a restricted CORS policy could also improve the security.

**Any ideas, suggestions, improvements ? Feel free to open a PR !**

## Authors

* **Théomé Borck** - *Technical test* - [Github Repo](https://github.com/theomeb/technical-test)
