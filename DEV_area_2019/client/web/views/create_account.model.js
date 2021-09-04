const mongoose = require('mongoose');

const schema = mongoose.schema;

const userSchema = new schema({
    username: {
        type: String,
        unique: true,
        required: true,
        trim: true
    },
    password: {
        type: String,
        required: true,
    }
});

const user = mongoose.model("User", userSchema);

module.exports = user;