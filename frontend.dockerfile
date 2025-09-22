FROM node:18
RUN mkdir /code
WORKDIR /code
COPY ./frontend/package*.json /code/
RUN yarn install
COPY . /code/

