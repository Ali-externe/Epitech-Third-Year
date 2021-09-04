FROM node:10.13-alpine
# ENV NODE_ENV production
# COPY ../app-release.apk .
WORKDIR /usr/src/app
# COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
COPY ["package*.json", "./"]
# RUN npm install --production --silent && mv node_modules ../
RUN npm install --global nodemon
RUN npm i -f
RUN npm cache clean -f
RUN npm install -gn
RUN npm install nodemailer -S
RUN npm install dotenv -S
COPY . .
EXPOSE 8081
CMD ["nodemon", "server.js"]