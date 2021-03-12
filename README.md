# T4A2-B  

---  

### R11: Link to deployed website  
https://eric-c-t4a2-b.ml/  

---  

### R12: Link to Github Repo  
https://github.com/eric-chew/T4A2-B  

---  

### R1: Project Libraries  
- bcrypt: Used to hash user passwords
- flake8: Used to check Python code styling
- Flask: Python App Framework
- Flask-Bcrypt: Integration for Flask and Bcrypt
- Flask-Marshmallow: Integration for Flask and Marshmallow
- Flask-Login: Used to manage user authorisation or authentication
- Flask-SQLAlchemy: Integration for Flask and SQLAlchemy
- Flask-WTF: Integration for Flask and WTForms
- Jinja2: Used for templating pages
- marshmallow: Used for mapping Python data types and Database Datatypes
- marshmallow-sqlalchemy: Integration for marshmallow and SQLAlchemy
- psycopg2-binary: Postgres Adapter for Python
- python-dotenv: Used to load environment variables
- SQLAlchemy: ORM for mapping database objects
- WTForms: Used for handling forms  

---

### R3 + R4: Project Management and Trello  
Tasks were categorised based on three axes:
- Difficulty
- Time Commitment
- Importance/Criticality

![](./docs/trello_screenshots/legend.png)

As a single person project, all tasks were delegated to myself based to their importance, and dependancies required and how long they would take.  
This resulting in features being descoped from the original specification for the following reasons:
- Tag Feature: Due to relative inexperience with front-end development and templating, it was not feasible to implement the feature without learning javascript.
- OAuth: By using Flask-Login instead of handling tokens with Flask-JWT-Extended, managing OAuth token would have made authorisation needlessly complicated and prone to error.  

Screenshots of the Trello board are taken after major accomplishments:
![](./docs/trello_screenshots/01.png)
![](./docs/trello_screenshots/02.png)
![](./docs/trello_screenshots/03.png)
![](./docs/trello_screenshots/04.png)
![](./docs/trello_screenshots/05.png)
![](./docs/trello_screenshots/06.png)
![](./docs/trello_screenshots/07.png)
![](./docs/trello_screenshots/08.png)
![](./docs/trello_screenshots/09.png)
![](./docs/trello_screenshots/10.png)

---

### R8 + R9: Testing
Manual Testing was done both on the back end (in a development server) and on the front end (on the production server)  

Back end testing:
![](./docs/development_manual_tests/auth_login1.png)
![](./docs/development_manual_tests/auth_login2.png)
![](./docs/development_manual_tests/auth_register1.png)
![](./docs/development_manual_tests/auth_register2.png)
![](./docs/development_manual_tests/auth_register3.png)
![](./docs/development_manual_tests/feedback_create1.png)
![](./docs/development_manual_tests/feedback_create2.png)
![](./docs/development_manual_tests/feedback_create3.png)
![](./docs/development_manual_tests/feedback_delete.png)
![](./docs/development_manual_tests/feedback_show.png)
![](./docs/development_manual_tests/feedback_update.png)
![](./docs/development_manual_tests/project_create.png)
![](./docs/development_manual_tests/project_delete.png)
![](./docs/development_manual_tests/project_index.png)
![](./docs/development_manual_tests/project_show.png)
![](./docs/development_manual_tests/project_show_user.png)
![](./docs/development_manual_tests/project_update.png)  
  
Front end testing:  
![](./docs/production_manual_tests/01.png)
![](./docs/production_manual_tests/02.png)
![](./docs/production_manual_tests/03.png)
![](./docs/production_manual_tests/04.png)
![](./docs/production_manual_tests/05.png)
![](./docs/production_manual_tests/06.png)
![](./docs/production_manual_tests/07.png)
![](./docs/production_manual_tests/08.png)
![](./docs/production_manual_tests/09.png)
![](./docs/production_manual_tests/10.png)
![](./docs/production_manual_tests/11.png)
![](./docs/production_manual_tests/12.png)
![](./docs/production_manual_tests/13.png)
![](./docs/production_manual_tests/14.png)
![](./docs/production_manual_tests/15.png)
![](./docs/production_manual_tests/16.png)
![](./docs/production_manual_tests/17.png)
![](./docs/production_manual_tests/18.png)
![](./docs/production_manual_tests/19.png)
![](./docs/production_manual_tests/20.png)
![](./docs/production_manual_tests/21.png)
![](./docs/production_manual_tests/22.png)
![](./docs/production_manual_tests/23.png)
![](./docs/production_manual_tests/24.png)
![](./docs/production_manual_tests/25.png)
![](./docs/production_manual_tests/26.png)
![](./docs/production_manual_tests/27.png)
![](./docs/production_manual_tests/28.png)
![](./docs/production_manual_tests/29.png)
![](./docs/production_manual_tests/30.png)
![](./docs/production_manual_tests/31.png)
![](./docs/production_manual_tests/32.png)  
  
Automated testing is performed by the CI/CD pipeline run using GitHub Actions.  

---

### R13: Part A

[View Part A Here](./docs/README.md)

