# My-contacts API

## Basic Auth 
 ``` 
  username: renan
  password: 1234
 ```
 ---
 ## Endpoints
 ### Person
  ``` 
     METHOD

     GET -> http://127.0.0.1:8000/contacts/person/

     GET -> http://127.0.0.1:8000/contacts/person/{id}/

    POST -> http://127.0.0.1:8000/contacts/person/
             _____________________________
             | Data Params               |
             |---------------------------|
             | name: "Luke Skywalker"    |
             | favorite: boolean         |    
             |___________________________|

   PATCH -> http://127.0.0.1:8000/contacts/person/{id}/
             _____________________________
             | Data Params               |
             |---------------------------|
             | name: "Luke Skywalker"    |
             | favorite: true|false      |    
             |___________________________|

  DELETE -> http://127.0.0.1:8000/contacts/person/{id}/
 ```
 ### Phone
  ``` 
 
 ```