<template>
    <v-app>
        <!-- Header -->
        <v-app-bar app class="primary white--text" absolute short fixed>
            </v-btn>
            <v-toolbar-items class="ml-n8">
                <v-btn to="/info" text class="font-weight-bold" style="background-color: #f5e2a7; color: #7e3179">
                    <img class="mr-3 mt-1" :src="require('./assets/bready.jpg')" height="50"/> bReady
                </v-btn>
                <!--Admin(mom <3)-->
                <v-btn v-if="$store.state.type=='admin'" to="/dayPlanAdmin" text class=" white--text">План на день
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/inventory" text class=" white--text">Инвентарь
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/equipment" text class=" white--text">Оборудование
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/bakingProgs" text class=" white--text">Программы выпечки
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/semiFinished" text class=" white--text">Полуфабрикаты
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/recipes" text class=" white--text">Рецепты и ТТК
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/employees" text class=" white--text">Сотрудники</v-btn>

                <!--cashier-->
                <v-btn v-if="$store.state.type=='cashier'" to="/onlineOrders" text class=" white--text">Заказы онлайн
                </v-btn>
                <v-btn v-if="$store.state.type=='cashier'" to="/kitchenSituation" text class=" white--text">Кухня
                </v-btn>
                <v-btn v-if="$store.state.type=='cashier'" to="/dayPlanBaker" text class=" white--text">План на день
                </v-btn>

                <!--baker-->
                <v-btn v-if="$store.state.type=='baker'" to="/dayPlanBaker" text class=" white--text">План на день
                </v-btn>
                <v-btn v-if="$store.state.type=='baker'" to="/recipesBaker" text class=" white--text">Рецепты и ТТК
                </v-btn>
                <v-btn v-if="$store.state.type=='baker'" to="/checklist" text class=" white--text">Чек-лист</v-btn>

            </v-toolbar-items>
            <v-spacer></v-spacer>

            <v-toolbar-items>
                <v-btn v-if="!$store.state.loggedIn" text class=" white--text" to="/login">Войти</v-btn>
                <v-menu offset-y v-else transition="slide-y-transition" bottom>
                    <template v-slot:activator="{ on }">
                        <v-btn text class=" white--text" v-on="on">
                            <v-avatar v-if="$store.state.loggedIn" class="mr-2" style="margin-top: -3px" color="grey">
                                <v-img :src="require('./assets/bready.jpg')"></v-img>
                            </v-avatar>
                            {{$store.state.username}}
                        </v-btn>
                    </template>
                    <v-list>
                        <v-list-item to="/profile">
                            <v-list-item-title>Профиль</v-list-item-title>
                        </v-list-item>
                        <v-list-item @click="logout()">
                            <v-list-item-title>Выйти</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>

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
            return {}
        },
        methods: {
            logout() {
                this.$store.dispatch('logout');
                router.push('/info');
            }
        }

    };
</script>

<style>
    ::-webkit-scrollbar {
        width: 6px;
    }

    ::-webkit-scrollbar-thumb {
        box-shadow: inset 0 0 5px grey;
        width: 6px;
        background: #7e3179;
    }

</style>
