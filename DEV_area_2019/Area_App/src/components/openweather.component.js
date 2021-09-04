import React, { Component } from 'react';
import { Switch, StyleSheet, Text, View, TextInput, TouchableOpacity} from 'react-native';
import { Button } from 'react-native';
import axios from 'axios';

class OpenWeather extends Component {

  constructor(props) {
    super(props);
    this.state={
      city: '',
      mail: '',
      temp_max:null,
      temp_min:null,
      switchValue:false
    }
    this.submitOpenWeather = this.submitOpenWeather.bind(this);
  }

  submitOpenWeather() {

    const user = {
        city: this.state.city,
        mail: this.state.mail,
        temp_max: this.state.temp_max,
        temp_min: this.state.temp_min
    }

    console.log(this.state.city);

    if (user.temp_max == "" || user.temp_min == "" || user.city == "" || user.mail == "") {
        return;
    }

    if (this.state.switchValue == false) {
        axios.post('http://10.0.2.2:8080/weather/temp', user)
        .then(function(res) {
            console.log(res.data);
        })
        .catch(error => {
            console.log(error)
        });
        axios.get('http://10.0.2.2:8080/weather/temp', user)
        .then(function(res) {
            console.log(res.data);
        })
        .catch(error => {
            console.log(error)
        });
    }
    else {
        axios.post('http://10.0.2.2:8080/weather/temp', user)
        .then(function(res) {
            console.log(res.data);
        })
        .catch(error => {
            console.log(error)
        });
        axios.get('http://10.0.2.2:8080/weather/temp', user)
        .then(function(res) {
            console.log(res.data);
        })
        .catch(error => {
            console.log(error)
        });
        axios.post('http://10.0.2.2:8080/weather/fluctuation', user)
        .then(function(res) {
            console.log(res.data);
        })
        .catch(error => {
            console.log(error)
        });
        axios.get('http://10.0.2.2:8080/weather/fluctuation', user)
        .then(function(res) {
            console.log(res.data);
        })
        .catch(error => {
            console.log(error)
        });
    }
  }

    toggleSwitch = (value) => {
        this.setState({switchValue: value})
    }

  render() {
    //const { navigate } = this.props.navigation;
    return(
        <View style={styles.container}>
            <Text>OpenWeather</Text>
            <TextInput ref={input => { this.textInputcity = input }}
            style={styles.inputBox}
            onChangeText={(city) => this.setState({city})}
            underlineColorAndroid='rgba(0,0,0,0)' 
            placeholder="City"
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
            keyboardType="username-address"
            onSubmitEditing={()=> this.textInputmax.focus()}/>
            
            <TextInput ref={input => { this.textInputmax = input }}
            style={styles.inputBox}
            onChangeText={(temp_max) => this.setState({temp_max})} 
            underlineColorAndroid='rgba(0,0,0,0)' 
            placeholder="Max_temp"
            placeholderTextColor = "#002f6c"
            selectionColor="#fff"
            keyboardType="username-address"
            onSubmitEditing={()=> this.textInputmin.focus()}/>

            <TextInput ref={input => { this.textInputmin = input }}
            style={styles.inputBox}
            onChangeText={(temp_min) => this.setState({temp_min})} 
            underlineColorAndroid='rgba(0,0,0,0)' 
            placeholder="Min_temp"
            placeholderTextColor = "#002f6c"
            selectionColor="#fff"
            keyboardType="username-address"/>
            <Text>Fluctuation</Text>
            <Switch
                onValueChange = {this.toggleSwitch}
                value = {this.state.switchValue}/>

            <TouchableOpacity style={styles.button}> 
                <Text style={styles.buttonText} onPress={ () => { this.submitOpenWeather() }}>Submit</Text>
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

export default OpenWeather;