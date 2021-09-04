FROM node:6
WORKDIR /app
COPY package*.json ./
RUN npm install
RUN npm i flatmap-stream
COPY . .
EXPOSE 8080
CMD [ "service", "mongod", "start" ]
CMD [ "node", "server.js" ]
