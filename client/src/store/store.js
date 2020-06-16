import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        username: 'dungeonMaster',
        type:'baker',
        loggedIn:true
    },
    actions: {
        login ({commit}, name, type) {
            commit('login', name, type);
        },

        logout({commit}) {
            commit('logout');
        }
    },

    mutations: {
        login(state, user, type) {
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
