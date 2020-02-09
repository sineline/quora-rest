# Simple Quora App (Docker / Frontend JS / Backend Python)

## Architecture

### Frontend Vue.js

- User authentification with token
- Router
- Interaction with backend
- Display data

### Backend Django Rest API

- User authentification with token
- CORS
- Serialization data from DB

## Set-up

From the root folder, execute the following commands.

1. run "docker-compose run api-quora python manage.py migrate"
2. run "docker-compose run client-quora npm install"
3. run "docker-compose up" (-d to run detached from shell)

## Acknowledgements and recognitions

This project is fundamentally based in [AntoLC/quora-rest](https://github.com/AntoLC/quora-rest) project.
