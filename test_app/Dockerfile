FROM node:alpine

RUN apk add --no-cache git

RUN apk add --no-cache openssh

WORKDIR /data

RUN git clone https://github.com/rifkyalikiki/example-api-app /data/app

WORKDIR /data/app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm instal

COPY . .

CMD [ "node", "server.js" ]

EXPOSE 3000