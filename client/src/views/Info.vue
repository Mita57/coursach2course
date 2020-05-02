<template>
    <div id="land" class="text-center">
        <v-container>
            <img :src="require('../assets/bready_intro.jpg')" height="250"/>
        </v-container>
        <div v-if="$store.state.username==''">
            <v-container>
                <h1>Добро пожаловать на bReady</h1>
            </v-container>
            <v-container>
                Для продолжения авторизуйтесь в системе
            </v-container>
            <v-container>
                <v-btn large class="primary" to="login">Войти в систему</v-btn>
            </v-container>
        </div>
        <div v-else>
            <v-container>
                <h1>Пожалуйста, выберите одну из вкладок в панели сверху.</h1>
            </v-container>
        </div>
    </div>

</template>

<script>
    export default {
        name: 'App',
        data() {
            return {}
        },
        methods: {},
        created() {
            document.title = 'bReady';
        }

    };
</script>

<style scoped>

</style>
