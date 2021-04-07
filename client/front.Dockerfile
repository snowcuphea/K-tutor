FROM node:lts-alpine

MAINTAINER dudrlf1859@naver.com
WORKDIR /client
ADD package.json ./
ADD . ./
CMD npm install && npm run serve
EXPOSE 8080