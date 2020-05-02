<template>
    <div class="login text-center mt-10">
        <h1>Войти</h1>
        <v-text-field class="mt-3" outlined type="text" clearable v-model="username" background-color="white"
                      placeholder="Логин" onchange="checkInputs()"><br></v-text-field>
        <v-text-field outlined type="password" clearable v-model="pwrd" background-color="white"
                      placeholder="Пароль" onchange="checkInputs()"><br></v-text-field>
        <v-btn large class="primary" :disabled="isDisabled" id="button" v-model="loginButton" @click="login">Войти
        </v-btn>
        {{result}}
    </div>
</template>

<script>
    import router from "../router";
    export default {
        name: "Login",
        data() {
            return {
                pwrd: '',
                username: '',
                result: '',
            }
        },
        methods: {
            login() {
                const aw = this;
                axios({
                    headers: {
                        'Access-Control-Allow-Origin': '*',
                        'Content-Type': 'application/json',
                    },
                    method: 'post',
                    url: 'http://localhost:5000/login',
                    data: {
                        login: aw.login,
                        pwrd: aw.pwrd
                    },
                }).then(function (response) {
                    if (response.data.result == 'fail') {
                        aw.result = 'Неправильное имя пользователя или пароль';
                    } else {
                        this.$store.state.username = aw.login;
                        this.$store.state.type = response.data.type;
                        router.push('/');
                    }
                })
                    .catch(function (response) {
                        //handle error
                        console.log(response);
                    })
            }
        }
        ,
        computed: {
            isDisabled() {
                if (this.pwrd.length > 3 && this.username.length > 3) {
                    return false;
                } else {
                    return true;
                }
            }
        },
        created() {
            document.title = 'Вход в систему';
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
