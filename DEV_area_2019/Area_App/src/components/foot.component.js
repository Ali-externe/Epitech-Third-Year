import React, { Component } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity } from 'react-native';
import { Button } from 'react-native';
import axios from 'axios';


class Foot extends Component {

  constructor(props) {
    super(props);
    this.state={
      mail: '',
      team: ''
    }
    this.submitFoot = this.submitFoot.bind(this);
  }

  submitFoot() {
    const user = {
        equipe_a_suivre: this.state.team,
        mail: this.state.mail
    }

    console.log(this.state.team);

    if (user.team == "" || user.mail == "") {
        return;
    }

    axios.post('http://10.0.2.2:8080/foot', user)
    .then(function(res) {
        console.log(res.data);
    })
    .catch(error => {
        console.log(error)
    });
    axios.get('http://10.0.2.2:8080/foot', user)
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
            <Text>Foot</Text>

            <TextInput ref={input => { this.textInputmail = input }}
            style={styles.inputBox}
            onChangeText={(mail) => this.setState({mail})}
            underlineColorAndroid='rgba(0,0,0,0)' 
            placeholder="Mail"
            placeholderTextColor = "#002f6c"
            selectionColor="#fff"
            keyboardType="username-address"
            onSubmitEditing={()=> this.textInputteam.focus()}/>

            <TextInput ref={input => { this.textInputteam = input }}
            style={styles.inputBox}
            onChangeText={(team) => this.setState({team})} 
            underlineColorAndroid='rgba(0,0,0,0)' 
            placeholder="Foot"
            placeholderTextColor = "#002f6c"
            selectionColor="#fff"
            keyboardType="username-address"/>

            <TouchableOpacity style={styles.button}> 
                <Text style={styles.buttonText} onPress={ () => { this.submitFoot() }}>Submit</Text>
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

export default Foot;