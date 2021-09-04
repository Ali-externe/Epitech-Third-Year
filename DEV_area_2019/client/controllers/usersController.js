'use strict';

var mongoose = require('mongoose'),
    User = mongoose.model('user');

exports.create_user = function (req, res) {
    var new_user = new User(req.body);
    new_user.save(function (err, user) {
        if (err)
            res.send(err);
        res.json(user);
    });
};

exports.find_user_by_id = function (req, res) {
    User.findById(req.params.Id, function (err, task) {
        if (err)
            res.send(err);
        res.json(User);
    });
};

exports.find_user = function (req, res) {
    User.findByMail(req.body.mail, function (err, task) {
        if (err)
            res.send(err);
        res.json(User);
    });
};