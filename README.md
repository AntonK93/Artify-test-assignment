# Artify test assignment

### Technology stack
front-end: Vue 2.6 / bootstrap 4 / SCSS<br>
back-end: tornado 6.1 / sqlaclhemy 0.7 / redis 2.4 (windows-package) / python 3.9

### Installation
Front end:
  - Install nvm if you do not have one (i used v10.16.3)
  - Install node modules with "npm install" from vue folder
  - Copy "app.config.example.js" from "vue/src/config" into the same folder and rename it to app.config.js, specify your api_url with the host that you are using for your server
  - Run "npm run serve" which will actually run "vue-cli-service serve" to serve it as application. Or you can run "npm run build" and use dist folder to locate it somewhere on your web server.

Back end:
  - Install python if you do not have one (i used v3.9)
  - Install pip if you do not have one (i used  v20.2.4)
  - Install pip requirements.txt within tornado folder "pip install -r requirements.txt"
  - Install mysql server (i used MariaDB v10.5.8)
  - Connect to the mysql server and import "dump.sql" which located in root folder
  - Install redis server (i used redis v2.4 windows package)
  - Adjust "config/config.py" in tornado folder, specify data of mysql/redis connection strings
  - Adjust "CLIENT_APP" in "config/config.py" with the host that you are using for your client application, by default it is http://localhost:8080
  - Run application with a command "python main.py" from root folder

### Time spent
Assignment took about 13 hours in total. Some time i spent for researching approach to interact and build tornado routing, it was not the hardest part but took some time, also some part of time took the python syntax to interact between class methods/constructors/imports/inheritances. The most part of time i spent researching sqlalchemy and her interaction with database/tables/schemas. So as far as i figured out it does not provide any possibility to convert data into json just with
sqlalchemy package, so i used marshmallow package with Schemas to convert data from sqlalchemy into json and pass it to the request. Also i used marshmallow validation to check the request client data, and validation took some part of time as well. Also i researched a bit about cookies and sessions, because actually last time that i worked with cookie sessions it was about 5 years ago, lately we used JWT token in rest apis. For the front end it took the less part of time, as i mentioned in estimation plan about 4 hours because I am working with it now constantly.

### About the assignment
Front-end presents only main route "/" with connected component of user-form which we can fill and send
to the server. Server validates the form and responds to  client, client notificates user with a server respond in a popup.
After successfully submiting the request, it creates a session with uuid number name and stores it in redis with key pair sessionId=userInfoId with expiration time that is defined in config. After creating the session it assigns it into response request header as Set-Cookie and after that client keeps the session. I used headers to provide possibility to use cookies in request headers. Under the front end in vue, in a http service i used withCredentials option to enable site cookies in axios headers.
