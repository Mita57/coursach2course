<template>
    <div class="login text-center mt-10">
        <h1>Войти</h1>
        <v-text-field class="mt-3" outlined type="text" clearable v-model="username" background-color="white"
                      placeholder="Логин" onchange="checkInputs()"><br></v-text-field>
        <v-text-field outlined type="password" clearable v-model="pwrd" background-color="white"
                      placeholder="Пароль" onchange="checkInputs()"><br></v-text-field>
        <v-btn large class="primary" disabled id="button" v-model="loginButton" @click="login">Войти</v-btn>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                pwrd: '',
                username: ''
            }
        },
        methods: {
            checkInputs() {
                if(this.pwrd.length > 3 && this.username.length > 3) {
                    this.loginButton.disabled = false;
                }
                else {
                    this.loginButton.disabled = true;
                }
            }
        }
    }

</script>

<style scoped>
    .login {
        padding: 15px;
        text-align: center;
        width: 700px;
        margin: auto;
        background-color: #f5e2a7;
        box-shadow: 0 0 10px grey;
    }

    input {
        margin: 10px 0;
        width: 100%;
        padding: 15px;
    }

    button {
        margin-top: 20px;
        width: 10%;
        cursor: pointer;
    }

    p {
        margin-top: 40px;
        font-size: 13px;
    }

    p a {
        text-decoration: underline;
        cursor: pointer;
    }

</style>
