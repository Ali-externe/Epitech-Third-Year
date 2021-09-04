
'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var userSchema = new Schema({
    username: {
        type: String,
        required: 'Kindly enter the name of the task'
    },
    mail: {
        type: String,
        required: 'Mail valid'
    },
    password: {
        type: String,
        required: 'Entrer a minimum 6 caractere password'
    },
    created_at: {
        type: Date,
        default: Date.now
    },
    updated_at: {
        type: Date,
        default: Date.now
    }

});

module.exports = mongoose.model('user', userSchema);