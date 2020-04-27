import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme:{
    themes: {
      light: {
        primary: '#7e3179',
        secondary: '#b0bec5',
        accent: '#f5e2a7',
        error: '#b71c1c',
      },
    },
  }
});
