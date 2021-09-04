// module.exports = function (app) {

//     	const passport = require('passport');
// 	app.use(passport.initialize());
// 	app.use(passport.session());


//     app.get('/', (req, res) => {
// 		user_connect = false;
// 		res.sendFile('views/Auth.html', { root: __dirname })
// 	});

//     // app.get('/home', (req, res) => {
// 	// 	if (!user_connect) {
// 	// 		return res.redirect('/');
// 	// 	}
// 	// 	res.render('home');
// 	// });

//     app.post('/',
//         passport.authenticate('local', { failureRedirect: '/error' }),
//         function (req, res) {
//             user_connect = true;
//             res.redirect('/home');
//     });
// }