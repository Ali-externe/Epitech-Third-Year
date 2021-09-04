'use strict';
module.exports = function (app) {
    var object = require('../controllers/usersController');

    app.route('/users/:Id').get(object.find_user_by_id);

    app.route('/users/connexion').post(object.find_user_by_mail_and_password);

    app.route('/users/create').post(object.create_user);

    app.route('/users/logout').post(object.logout);

    app.route('/users/auth2/create').post(object.create_user_auth2);

    app.route('/users/auth2/connexion').post(object.find_user_by_email);
};
