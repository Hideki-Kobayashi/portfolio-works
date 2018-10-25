// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false
import firebase from 'firebase'

// Initialize Firebase
var config = {
  apiKey: "AIzaSyCcAmPdkWVJRr6iy0NP1Fl_wUtfhE7Rygs",
  authDomain: "vue-chat-14d11.firebaseapp.com",
  databaseURL: "https://vue-chat-14d11.firebaseio.com",
  projectId: "vue-chat-14d11",
  storageBucket: "vue-chat-14d11.appspot.com",
  messagingSenderId: "362297633002"
};
firebase.initializeApp(config);

new Vue({
  el: "#app",
  components: { App },
  template: '<App/>'
})