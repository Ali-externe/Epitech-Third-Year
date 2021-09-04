'use strict';

module.exports = function (app) {
    var object = require('../controllers/restApiController');

    // object Routes
    app.route('/tasks')
        .get(object.list_all_tasks)
        .post(object.create_a_task);


    app.route('/tasks/:taskId')
        .get(object.read_a_task)
        .put(object.update_a_task)
        .delete(object.delete_a_task);
};