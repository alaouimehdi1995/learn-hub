FROM node:8.10.0-alpine

# Preparing working directory
WORKDIR /usr/src/app/
COPY package.json ./

# Installing dependencies
RUN npm install

# Exposing the application default port
EXPOSE 3000
