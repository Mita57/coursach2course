<template>
    <div id="land" class="text-center">
        <v-container>
            <img :src="require('../assets/bready_intro.jpg')" height="250"/>
        </v-container>
        <v-container>
            <h1>Добро пожаловать на bReady</h1>
        </v-container>
        <v-container>
            Для продолжения авторизируйтесь в системе
        </v-container>
        <v-container>
            <v-btn large class="primary" to="login">Войти в систему</v-btn>
        </v-container>
    </div>

</template>

<script>
    export default {
        name: 'App',
        data() {
            return {

            }
        },
        methods: {

        },

    };
</script>

<style scoped>

</style>
