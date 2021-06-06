# My Contacts API

#### My Contacts App: [My Contacts](https://github.com/cardosorrenan/my_contacts)

## Setup

###### Python: 3.6.9v
###### Pip: 20.2.4v
 
 ##### 1. Get repo
 ``` 
 git clone https://github.com/cardosorrenan/my_contacts_api
 ```
 
 ##### 2. Go to folder project
 ``` 
 cd ./my_contacts_api
 ```
 
 ##### 3. Install dependencies
 ``` 
 pip install -r requirements.txt
 ```
 
 ##### 4. Instantiate sqlite3 database and run migrations
 ``` 
 python manage.py migrate 
 ```
 
 ##### 5. Dump fake data 
 ```
 python manage.py loaddata my_contacts/fixtures/*.json
 ```
 
 ##### 6. Create superuser (command for development purposes)
 ```
 ./manage.py createsuperuser2 --username renan --password 1234 --noinput --email 'renan@teste.com'
 ```
 
 ##### 7. Run server
 ```
 python manage.py runserver
 ```

 ##### 8. [http://localhost:8000/api/?format=json](http://localhost:8000/api/?format=json)
 
 ## API
 
 ##### [Insomnia File](https://github.com/cardosorrenan/my_contacts_api/blob/master/my_contacts/static/MyContact_Insomnia.json) - Download and import :rocket:
 
 ### Person
 
 #### Model response
 
 ```
 Person {
    id: number
    name: string
    favorite: boolean
    phones: Phone[]
    created_at: date
    updated_at: date
 }
 ```
 
 #### Endpoints

 | | URL | METHOD | REQUEST BODY | RESPONSE |
 | :-: | :-: | :-: | :-: | :-: |
 | INDEX | /contacts/persons | GET | - | Person[ ] |
 | GET ONE | /contacts/persons/{id} | GET | - | Person |
 | SAVE | /contacts/persons | POST | name,<br /> favorite | Person |
 | EDIT | /contacts/persons/{id} | PATCH | name,<br /> favorite | Person |
 | DELETE | /contacts/persons/{id} | DELETE | - | - |
 
 ### Phone
 
 #### Model response
 
 ```
 Phone {
    id: number
    number: string
    person: number
    created_at: date
    updated_at: date
 }
 ```
 
 #### Endpoints

 | | URL | METHOD | REQUEST BODY | RESPONSE |
 | :-: | :-: | :-: | :-: | :-: |
 | INDEX | /contacts/phones | GET | - | Phone[ ] |
 | GET ONE | /contacts/phones/{id} | GET | - | Phone |
 | SAVE | /contacts/phones | POST | number,<br /> person | Phone |
 | EDIT | /contacts/phones/{id} | PATCH | number,<br /> person | Phone |
 | DELETE | /contacts/phones/{id} | DELETE | - | - |
 
