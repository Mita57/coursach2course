<template>
    <v-container class="grey lighten-5">
        <v-row no-gutters>
            <v-col cols="12" sm="6" md="8" >
                <v-card class="mx-auto" outlined>
                    <v-list-item three-line>
                        <div class="text-center">
                            <v-img :src="require('../assets/bready.jpg')" max-width="125"/>
                            <v-btn x-small color="success" dark>Поменять аватар</v-btn>
                        </div>
                        <v-list-item-content class="ml-5">
                            <v-list-item-title class="headline mb-1">Username</v-list-item-title>
                            <v-list-item-subtitle>Info</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                    <v-card-actions>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "Profile",
        mounted() {
            document.title = "Профиль";
        }
    }
</script>

<style scoped>

</style>
