# base image
FROM node:12.2.0-alpine

# set working directory
WORKDIR /app

RUN npm install
RUN npm install -g @vue/cli

COPY ./client-app /app

# COMMAND TO CREATE THE APP - WILL COPY ON LOCAL 
#docker-compose run client-quora vue create vue-app --default
