<template id="cock">
    <div id="sas" class="mt-4">
        <div id="table">
            <v-data-table :headers="headers" :items="items" class="elevation-1">
                <template v-slot:top>
                    <v-toolbar flat color="white">
                        <v-spacer></v-spacer>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ on }">
                                <v-btn color="primary" dark class="mb-2" v-on="on">Добавить</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="headline">Продукт</span>
                                </v-card-title>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-col cols="12" sm="6" md="4">
                                                <v-text-field v-model="editedItem.name" label="Название"></v-text-field>
                                            </v-col>
                                            <v-col cols="12" sm="6" md="4">
                                                <v-text-field v-model="editedItem.amount"
                                                              label="Количество"></v-text-field>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                                    <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                                </v-card-actions>

                            </v-card>
                        </v-dialog>
                    </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                    <v-icon small class="mr-2" @click="editItem(item)">
                        mdi-pencil
                    </v-icon>
                    <v-icon small @click="deleteItem(item)">
                        mdi-delete
                    </v-icon>
                </template>
                <template slot="no-data">
                    <div>Нет данных</div>
                </template>
            </v-data-table>
        </div>

        <div id="buttons">
            <template >
                <div class="text-center" id="standard">
                    <v-menu top :offset-y="true">
                        <template v-slot:activator="{ on }">
                            <v-btn color="primary" dark v-on="on">
                                Стандартный
                            </v-btn>
                        </template>
                        <v-list>
                            <v-list-item  @click="">
                                <v-list-item-title>Выгрузить</v-list-item-title>
                            </v-list-item>
                            <v-list-item  @click="">
                                <v-list-item-title>Изменить</v-list-item-title>
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </div>
            </template>
        </div>
    </div>
</template>

<script>
    export default {
        name: "DayPlanAdmin",
        data() {
            return {
                dialog: false,
                headers: [
                    {text: 'Название', align: 'start', value: 'name'},
                    {text: 'Количество', align: 'start', value: 'amount'},
                    {text: 'Действия', align: 'start', value: 'actions', sortable: false},
                ],
                items: [],
                editedIndex: -1,
                editedItem: {
                    name: '',
                    amount: 0
                },
                defaultItem: {
                    name: '',
                    amount: 0
                }
            }
        },
        methods: {
            editItem(item) {
                this.editedIndex = this.items.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },

            deleteItem(item) {
                const index = this.items.indexOf(item)
                confirm('Удалить?') && this.items.splice(index, 1)
            },
            save () {
                if (this.editedIndex > -1) {
                    Object.assign(this.items[this.editedIndex], this.editedItem)
                } else {
                    this.items.push(this.editedItem)
                }
                this.close()
            },
            close () {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },
        },
    }
</script>

<style scoped>
    #table {
        margin: auto;
        height: 90%;
        width: 80%;
    }

    #buttons {
        width: 100%;
        height: 5%;
        display: grid;
        grid-template-columns: 10% 20% 10% 20% 10% 20% 10%;
    }

    #standard {
        grid-column: 2;
    }
</style>
