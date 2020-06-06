import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        username: 'cocksucker',
        type:'admin',
        loggedIn:true
    },
    mutations: {
        login (state, name, type) {
            state.username = name;
            state.type = type;
            state.loggedIn = true;
        },

        logout(state) {
            state.username = '';
            state.type = '';
            state.loggedIn = false;
        }
    }
})

export default store;
