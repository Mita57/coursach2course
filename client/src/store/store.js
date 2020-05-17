import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        username: '',
        type:'baker',
        loggedIn:false
    },
    mutations: {
        login (name, type) {
            this.username = name;
            this.type = type;
            this.loggedIn = true;
        },

        logout() {
            this.username = '';
            this.type = '';
            this.loggedIn = false;
        }
    }
})

export default store;
