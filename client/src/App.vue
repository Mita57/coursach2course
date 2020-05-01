<template>
    <v-app>
        <!-- Header -->
        <v-app-bar app class="primary white--text" absolute short fixed clipped-right>
            </v-btn>
            <v-toolbar-items class="ml-n8">
                <v-btn to="/info" text class="font-weight-bold" style="background-color: #f5e2a7; color: #7e3179">
                    <img class="mr-3 mt-1" :src="require('./assets/bready.jpg')" height="50"/> bReady</v-btn>
                <!--Admin(mom <3)-->
                <v-btn v-if="$store.state.type=='admin'" to="/dayPlanAdmin" text class=" white--text">План на день
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/minorEquipment" text class=" white--text">Инвентарь
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/majorEquipment" text class=" white--text">Оборудование
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/recipesAdmin" text class=" white--text">Рецепты и ТТК
                </v-btn>
                <v-btn v-if="$store.state.type=='admin'" to="/employees" text class=" white--text">Сотрудники</v-btn>

                <!--cashier-->
                <v-btn v-if="$store.state.type=='cashier'" to="/onlineOrders" text class=" white--text">Заказы онлайн
                </v-btn>
                <v-btn v-if="$store.state.type=='cashier'" to="/kitchenSituation" text class=" white--text">Кухня
                </v-btn>

                <!--baker-->
                <v-btn v-if="$store.state.type=='baker'" to="/dayPlanBaker" text class=" white--text">План на день
                </v-btn>
                <v-btn v-if="$store.state.type=='baker'" to="/recipesBaker" text class=" white--text">Рецепты и ТТК
                </v-btn>
                <v-btn v-if="$store.state.type=='baker'" to="/instructions" text class=" white--text">Чек-лист</v-btn>

            </v-toolbar-items>
            <v-spacer></v-spacer>


            <v-toolbar-items>
                <v-btn v-if="!$store.state.loggedIn" text class=" white--text" to="/login">Войти</v-btn>
                <v-btn v-else text class=" white--text" to="/profile">{{user}}</v-btn>
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
        methods: {},

    };
</script>

<style>

</style>
