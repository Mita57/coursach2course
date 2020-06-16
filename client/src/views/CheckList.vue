<template>
    <div>
        <v-snackbar v-model="snackbar" timeout="99999999999">
            {{text}}
            <template v-slot:action="{ attrs }">
                <v-btn color="primary" text v-bind="attrs" @click="snackbar = false">
                </v-btn>
            </template>
        </v-snackbar>

            <v-card class="mx-auto my-12" max-width="374">
                <v-img
                        height="250"
                        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
                ></v-img>

                <v-card-title>Развесьте ингредиенты для: багет французский</v-card-title>

                <v-card-text>

                    <div class="my-4 subtitle-1">
                        10 штук
                    </div>

                    <div>Тесто слоеное 400 гр. <br>
                        Сыр твердый 100 гр.<br>
                        Сосиски 500 гр.

                    </div>
                </v-card-text>

                <v-divider class="mx-4"></v-divider>


                <v-card-text>
                    10 минут
                </v-card-text>
                <v-card-actions>
                    <v-spacer/>
                    <v-btn color="deep-purple lighten-2" text @click="reserve">
                        Готово
                    </v-btn>
                </v-card-actions>
            </v-card>
    </div>
</template>

<script>
    export default {
        name: "CheckList",
        data: () => ({
            snackbar: true,
            text: 'Печь Intel Core i9 занята, осталось 12:36',
        }),
    }
    // TODO: everything
</script>

<style scoped>

</style>
