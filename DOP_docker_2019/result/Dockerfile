FROM node:10.13-alpine

EXPOSE 80
WORKDIR /usr/src/app
COPY package.json .
RUN npm install
COPY . .

CMD [ "npm", "start"]
