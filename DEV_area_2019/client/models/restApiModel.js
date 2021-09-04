'use strict';

var mongoose = require('mongoose');
var Schema = mongoose.Schema;


var TaskSchema = new Schema({
    username: {
        type: String,
        required: 'Kindly enter the name of the task'
    },
    password: {
        type: String,
        required: 'Entrer a minimum 6 caractere password'
    },
    Created_date: {
        type: Date,
        default: Date.now
    }
    // status: {
    //     type: [{
    //         type: String,
    //         enum: ['pending', 'ongoing', 'completed']
    //     }],
    //     default: ['pending']
    // }
});

module.exports = mongoose.model('Tasks', TaskSchema);