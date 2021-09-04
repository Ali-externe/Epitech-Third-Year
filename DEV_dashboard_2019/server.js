'use strict';

const express = require('express');
const PORT = 8080;
const HOST = '0.0.0.0';
const app = express();
var path = require('path');
var scriptjs = require('./script.js');
var qs = require('querystring');
var url = "mongodb://mongo:27017/";
var MongoClient = require("mongodb").MongoClient;
var mongoose = require("mongoose");

mongoose.connect('mongodb://mongo:27017/dashboard', {
    useNewUrlParser: true
})
    .catch((err) => {
	console.error("FUCK\n")
	mongoose.connect('mongodb://localhost:27017/dashboard', {
            useNewUrlParser: true
	})
            .catch((err) => {
		console.error("JE SUCE PL\n" + err.stack)
		process.exit(1)
            })
    });

app.use(express.static(__dirname));

app.post('/login', (req, res) => {
    var body = "";
    req.on("data", function (data) {
	body+=data;
    });
    req.on("end",function(){
	var obj = qs.parse(body);
	var mail = obj.mail;
	var pwd = obj.pwd;
	MongoClient.connect(url, function(err, db) {
	    if (err) throw err;
	    var dbo = db.db("dashboard");
	    dbo.collection("members").find({mail: mail, password: pwd}).toArray(function(err, result) {
		if (err) throw err;
		console.log(result);
		if (result.length != 0) {
		    res.sendFile(path.join(__dirname + '/pages/home.html'));
		    console.log("SUCCES");
		}
		else {
		    app.use(express.static(__dirname + '/'));
		    res.sendFile(path.join(__dirname + '/pages/log.html'));
		    console.log("FAILURE");
		}
		db.close();
	    });
	});
    });
});

app.post('/sub', (req, res) => {
    var body = "";
    req.on("data", function (data) {
	body+=data;
    });
    req.on("end",function(){
	var obj = qs.parse(body);
	var mail = obj.mail;
	var pwd = obj.pwd;
	console.log(mail);
	console.log(pwd);

	MongoClient.connect(url, function(err, db) {
	    if (err) throw err;
	    var dbo = db.db("dashboard");
	    dbo.collection("members").find({mail: mail, password: pwd}).toArray(function(err, result) {
		if (err) throw err;
		console.log(result);
		if (result.length != 0) {
		    app.use(express.static(__dirname + '/'));
		    res.sendFile(path.join(__dirname + '/pages/log.html'));
		    console.log("ALREADY EXIST");
		    db.close();
		}
		else {
		    app.use(express.static(__dirname + '/'));
		    res.sendFile(path.join(__dirname + '/pages/log.html'));
		    var myobj = { mail: mail, password: pwd };
		    dbo.collection("members").insertOne(myobj, function(err, res) {
			if (err) throw err;
			console.log("NEW ACCOUNT");
			db.close();
		    });
		}
	    });
	});
    });
});

app.post('/checkClicked', (req, res) => {
    console.log("COUCOUUUUUUUUUUU");
});

app.get('/', (req, res) => {
    app.use(express.static(__dirname));
    res.sendFile(path.join(__dirname + '/pages/log.html'));
});

app.get('/signUp', (req, res) => {
    app.use('/', express.static(__dirname));
    res.sendFile(path.join(__dirname + '/pages/signup.html'));
});

app.get('/home', function(req, res) {
    app.use('/', express.static(__dirname));
    res.sendFile(path.join(__dirname + '/pages/home.html'));
});

app.get('/services', function(req, res) {
    app.use('/', express.static(__dirname));
    res.sendFile(path.join(__dirname + '/pages/widget.html'));
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
