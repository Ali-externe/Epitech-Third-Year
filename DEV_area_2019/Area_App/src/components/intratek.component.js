import React, { Component } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity} from 'react-native';
import { Button } from 'react-native';
import axios from 'axios';


class IntraTek extends Component {

  constructor(props) {
    super(props);
    this.state={
      autolog: '',
      mail: ''
    }
    this.submitIntraTek = this.submitIntraTek.bind(this);
    this.submitIntraTekAlert = this.submitIntraTekAlert.bind(this);
  }

  submitIntraTek() {

    const user = {
        autologin: this.state.autolog,
        mail: this.state.mail
    }

    if (user.autologin== "" || user.mail == "") {
        return;
    }

    console.log(this.state.autolog);
    axios.post('http://10.0.2.2:8080/epitech/msg', user)
      .then(function(res) {
        console.log(res.data);
      })
      .catch(error => {
        console.log(error)
      });
    axios.get('http://10.0.2.2:8080/epitech/msg', user)
      .then(function(res) {
        console.log(res.data);
      })
      .catch(error => {
        console.log(error)
      });
  }

  submitIntraTekAlert() {

    const user = {
        autologin: this.state.autolog,
        mail: this.state.mail
    }

    if (user.autologin== "" || user.mail == "") {
        return;
    }

    console.log(this.state.autolog);
    axios.post('http://10.0.2.2:8080/epitech/alert', user)
      .then(function(res) {
        console.log(res.data);
      })
      .catch(error => {
        console.log(error)
      });
    axios.get('http://10.0.2.2:8080/epitech/alert', user)
      .then(function(res) {
        console.log(res.data);
      })
      .catch(error => {
        console.log(error)
      });
  }

  render() {
    //const { navigate } = this.props.navigation;
    return(
        <View style={styles.container}>
            <Text>IntraTek</Text>
            <TextInput ref={input => { this.textInputautolog = input }}
            style={styles.inputBox}
            onChangeText={(autolog) => this.setState({autolog})}
            underlineColorAndroid='rgba(0,0,0,0)' 
            placeholder="Autologin link"
            placeholderTextColor = "#002f6c"
            selectionColor="#fff"
            keyboardType="username-address"
            onSubmitEditing={()=> this.textInputmail.focus()}/>

            <TextInput ref={input => { this.textInputmail = input }}
            style={styles.inputBox}
            onChangeText={(mail) => this.setState({mail})}
            underlineColorAndroid='rgba(0,0,0,0)' 
            placeholder="Mail"
            placeholderTextColor = "#002f6c"
            selectionColor="#fff"
            keyboardType="username-address"/>

            <TouchableOpacity style={styles.button}> 
                <Text style={styles.buttonText} onPress={ () => { this.submitIntraTek() }}>Submit Msg</Text>
            </TouchableOpacity>
            <TouchableOpacity style={styles.button}> 
                <Text style={styles.buttonText} onPress={ () => { this.submitIntraTekAlert() }}>Submit Alert</Text>
            </TouchableOpacity>
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

export default IntraTek;