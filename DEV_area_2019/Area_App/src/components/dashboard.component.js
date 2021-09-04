import React, { Component } from 'react';
import { ScrollView , Button } from 'react-native';
import { Switch, StyleSheet, Text, View, TextInput, TouchableOpacity} from 'react-native';
import { authorize } from 'react-native-app-auth'
import Service from "./service.component";
import OpenWeather from "./openweather.component";
import IntraTek from "./intratek.component";
import News from "./news.component";
import Hour from "./hour.component";
import Movie from "./movie.component";
import Foot from "./foot.component";
import axios from 'axios';


class Dashboard extends Component {

  constructor(props) {
    super(props);
  }

  /*async _onLoginDiscord() {
  
    const config = {
      clientId: '680149220270800904',
      clientSecret: 'CjkbKfUU6MBj3VR33-2V5OrUWLMm-mBV',
      redirectUrl: 'http://localhost:8081/oauth2',
      scopes: ['email', 'identify'],
      serviceConfiguration: {
        authorizationEndpoint: 'https://discordapp.com/api/oauth2/authorize',
        tokenEndpoint: 'https://discordapp.com/api/oauth2/token',
        revocationEndpoint: 'https://discordapp.com/api/oauth2/token/revoke'
      }
    }

    try {
      const authResult = await authorize(config)
    } catch (error) {
      console.log(error)
    }
  }*/

  render() {
    const { navigate } = this.props.navigation;
    return(
      <ScrollView>
        <OpenWeather />
        <IntraTek />
        <News />
        <Hour />
        <Movie />
        <Foot />
      </ScrollView>
    )
  }
}

/*<Button
          title="AuthDiscord"
          onPress={ () => { this._onLoginDiscord() }}
        />*/
//<Service service='Github' />
//<Service service='Dropbox' />

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

export default Dashboard;