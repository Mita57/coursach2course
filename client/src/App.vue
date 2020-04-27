<template>
    <v-app>
        <!-- Header -->
        <v-app-bar app class="primary white--text" absolute short fixed clipped-right>
            <router-link to="/">
                <img class="mr-3 mt-1" :src="require('./assets/bready.jpg')" height="50"/>
            </router-link>
            <v-toolbar-title class="headline" dark>
                <router-link style="color: white; text-decoration: none" to="/"><span>bReady</span></router-link>
            </v-toolbar-title>
            <v-toolbar-items class="ml-4">
            </v-toolbar-items>
            <v-spacer></v-spacer>

            <v-toolbar-items>
                <v-btn text class=" white--text" to="/account">Войти</v-btn>
            </v-toolbar-items>
        </v-app-bar>

        <!-- Sidebar -->
        <v-content>
            <router-view/>
        </v-content>
    </v-app>
</template>

<script>
    import axios from 'axios';
    import router from "./router";

    export default {
        name: 'App',
        data() {
            return {
                user: 'Войти',
                channels: [],
                auth_result: ''
            }
        },
        methods: {
        }
    };
</script>

<style>

</style>
