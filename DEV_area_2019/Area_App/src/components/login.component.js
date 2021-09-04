import React, { Component } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Button } from 'react-native';
import axios from 'axios';

class Login extends Component {

  constructor(props){
    super(props);
    this.state={
        username:'',
        mail:'',
        password: ''
    }
    this.saveData = this.saveData.bind(this);
  }

saveData() {

  //if (!this.state.username) {
  //  return;
  //}

  if (!this.state.mail) {
    return;
  }

  if (!this.state.password) {
    return;
  }

  const user = {
      mail: this.state.mail,
      password: this.state.password,
  }

  var self = this;

  console.log(user);

  axios.post('http://10.0.2.2:8080/users/connexion', user)
      .then(function(res) {
        console.log(res.data);
        if (res.data != "error password") {
          self.props.navigation.navigate('Main_Page');
        }
      })
      .catch(error => {
        console.log(error)
      });

  this.textInputmail.clear();
  this.textInputpass.clear();

}

  render() {
    const { navigate } = this.props.navigation;
    return(
      <View style={styles.container}>
          <TextInput ref={input => { this.textInputmail = input }}
          style={styles.inputBox}
          onChangeText={(mail) => this.setState({mail})}
          underlineColorAndroid='rgba(0,0,0,0)' 
          placeholder="Mail"
          placeholderTextColor = "#002f6c"
          selectionColor="#fff"
          keyboardType="username-address"
          onSubmitEditing={()=> this.textInputpass.focus()}/>
          
          <TextInput ref={input => { this.textInputpass = input }}
          style={styles.inputBox}
          onChangeText={(password) => this.setState({password})} 
          underlineColorAndroid='rgba(0,0,0,0)' 
          placeholder="Password"
          secureTextEntry={true}
          placeholderTextColor = "#002f6c"
          />

          <TouchableOpacity style={styles.button}> 
              <Text style={styles.buttonText} onPress={ () => { this.saveData() }}>Login</Text>
          </TouchableOpacity>
          <Button
          title="Create"
          onPress={ () => { this.props.navigation.navigate('Create'); }}
        />
      </View>
      
  )
  }
}


const styles = StyleSheet.create({
  container: {
      justifyContent: 'center',
      alignItems: 'center',
  },
  inputBox: {
      width: 300,
      backgroundColor: '#eeeeee', 
      borderRadius: 25,
      paddingHorizontal: 16,
      fontSize: 16,
      color: '#002f6c',
      marginVertical: 10
  },
  button: {
      width: 300,
      backgroundColor: '#4f83cc',
      borderRadius: 25,
      marginVertical: 10,
      paddingVertical: 12
  },
  buttonText: {
      fontSize: 16,
      fontWeight: '500',
      color: '#ffffff',
      textAlign: 'center'
  }
});

export default Login;