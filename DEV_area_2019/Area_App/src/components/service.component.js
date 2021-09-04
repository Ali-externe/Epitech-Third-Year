import React, { Component } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity} from 'react-native';

class Service extends Component {

  constructor(props) {
    super(props);
    this.state={
    }
  }

  render() {
    return(
        <View style={styles.container}>
        <Text>{this.props.service}</Text>
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
            <Text style={styles.buttonText} onPress={ () => {            }}>Login</Text>
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

export default Service;