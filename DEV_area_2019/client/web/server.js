'use strict';


/* Require */
const nodemailer = require('nodemailer');
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
let configAuth = require('./views/auth');
var GoogleStrategy = require('passport-google-oauth20');
var axios = require("axios");
let discord = require('./discord.js');

require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const port = 8081;
var user_connect = false;
const uri = process.env.ATLAS_URI;
var code = "Not yet";


var user = {
	mail: "",
	username: ""
}

var discord_access_token;
const CLIENT_ID = '680149220270800904'
const CLIENT_SECRET = 'CjkbKfUU6MBj3VR33-2V5OrUWLMm-mBV'
const REDIRECT_URI = "http://localhost:8081/oauth2"
const btoa = require("btoa");
const creds = btoa(`${CLIENT_ID}:${CLIENT_SECRET}`);

app.get('/oauth2', (req, res) => {
	const {
		code
	} = req.query;
	console.log(code);

	if (code != null) {
		console.log("YOUPI !");
	}

	axios({
		method: "post",
		url: `https://discordapp.com/api/oauth2/token?grant_type=authorization_code&code=${code}&redirect_uri=${REDIRECT_URI}`,
		headers: {
			Authorization: `Basic ${creds}`
		}
	}).then(result => {
		let result1 = result;
		discord_access_token = result1.data.access_token;
		console.log(discord_access_token);
		discord.get_server_discord(discord_access_token);
		res.redirect('/home');
	})
		.catch(error => {
			console.warn(error)
		})
});

const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
	user_connect = false;
	res.sendFile('views/Auth.html', { root: __dirname })
});
app.get('/account', (req, res) => res.sendFile('views/account.html', { root: __dirname }));
app.use(express.static(__dirname + '/views'));

app.listen(port, () => console.log('App listening on port ' + port));

app.get('/success', (req, res) => res.send("Welcome " + req.query.username + "!!"));
app.get('/error', (req, res) => res.send("error logging in"));

app.set('view engine', 'ejs');


app.get('/home', (req, res) => {
	if (!user_connect) {
		return res.redirect('/');
	}
	res.render('home');
	console.log(discord_access_token);
});

// const fileApk = require('/var/tmp/app-release.apk')

app.get('/client.apk', (req, res) => {
	// var path 
	// if (!user_connect) {
	// 	return res.redirect('/');
	// }
	console.log("apk render");
	res.download('/var/tmp/app-release.apk', 'client.apk');
});


app.post('/', function (req, res) {
	const obj = {
		mail: req.body.username,
		password: req.body.password
	};
	axios.post('http://localhost:8080/users/connexion', obj).then(function (result) {
		user_connect = true;
		user.mail = result.data.mail;
		user.username = result.data.username;
		res.redirect('/home');
	}).catch(error => {
		// console.log(error.message)
		user_connect = true;
		// res.redirect('/');
		res.redirect('/home');

	});
});

app.post('/create', async (req, res) => {
	const obj = {
		username: req.body.username,
		mail: req.body.email,
		password: req.body.password
	};
	axios.post('http://localhost:8080/users/create', obj).then(function (result) {
		user_connect = true;
		res.redirect('/home');
		// res.redirect('/');
	}).catch(error => {
		user_connect = true;
		res.redirect('/home');

		// console.log(error.message)
		// res.redirect('/account.html');
	});
	res.redirect('/');
});