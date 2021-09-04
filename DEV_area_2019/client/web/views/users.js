const router = require('express').Router();
let user = require('./create_account.model');

router.route('/').get((req, res) => {
    user.find()
    .then(users => res.json(users))
    .catch(err => res.status(400).json('Error: ' + err));    
});

router.route('/add').post((res, res) => {
    const username = req.body.username;
    const password = req.body.password;

    const newUser = new user({
        username,
        password,
    });

    newUser.save()
    .then(() => res.json('User addes!'))
    .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;