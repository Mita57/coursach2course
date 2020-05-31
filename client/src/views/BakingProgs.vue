<template>
    <div class="mt-4 ml-2">
        <div id="table">
            <v-data-table fixed-header hide-default-footer disable-pagination :height="tableHeight" :headers="headers"
                          :items="items"
                          class="elevation-2">
                <template v-slot:item.image="{ item }">
                    <div class="p-2">
                        <v-avatar class="profile" color="grey" size="100" tile>
                            <v-img :src="item.image" he></v-img>
                        </v-avatar>
                    </div>
                </template>
                <template v-slot:top>
                    <v-toolbar flat color="white">
                        <v-text-field v-model="search" @input="searchFieldChanged()" class="mb-2"
                                      append-icon="mdi-magnify" dense outlined label="Поиск"
                                      hide-details></v-text-field>
                        <v-spacer></v-spacer>
                        <v-select dense :items="ovens" class="mt-4 mr-4" v-model="editedItem.type" label="Выберите печку" solo/>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ on }">
                                <v-btn tile color="primary" dark class="mb-2" v-on="on">Добавить</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="headline">Предмет</span>
                                </v-card-title>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.name" ref="editName" label="Название"/>
                                        </v-row>
                                        <v-row>

                                            <v-text-field dense v-model="editedItem.amount"
                                                          label="Количество"></v-text-field>
                                        </v-row>
                                        <v-row>
                                            <v-file-input dense accept="image/png, image/jpeg, image/bmp"
                                                          placeholder="Добавьте изображение" prepend-icon="mdi-camera"
                                                          label="Изображение"/>
                                        </v-row>
                                        </v-row>
                                    </v-container>
                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="primary" text @click="close">Отменить</v-btn>
                                    <v-btn color="primary" text @click="save">Сохранить</v-btn>
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
            <v-btn large id="cancelButton" tile color="accent" style="color: #7e3179" class="mt-3 bts elevation-3"
                   @click="cancelClick()">Отмена
            </v-btn>
            <v-btn large id="saveButton" tile color="primary" class="mt-3 bts elevation-3" @click="saveInventory()">
                Сохранить
            </v-btn>
        </div>
    </div>
</template>

<script>
    export default {
        name: "BakingProgs",
        data() {
            return {
                search: '',
                dialog: false,
                tableHeight: 0,
                headers: [
                    {text: '', align: 'start', value: 'image'}, //img
                    {text: 'Название', align: 'start', value: 'name'},
                    {text: 'Количество', align: 'start', value: 'amount'},
                    {text: 'Действия', align: 'start', value: 'actions', sortable: false},
                ],
                globalItems: [
                    {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    },
                    {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    },
                    {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    },
                    {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'cock',
                        amount: 3,
                    },
                ],
                items: [],
                ovens: ['Печка адын', 'Печка дыва'],
                editedIndex: -1,
                editedItem: {
                    name: '',
                    amount: 0,
                    image: '',
                },
                defaultItem: {
                    name: '',
                    amount: 0,
                    image: '',
                },
                date: new Date().toISOString().substr(0, 10),
                arrayEvents: [`${new Date().getFullYear()}-12-31`,
                    `${new Date().getFullYear()}-02-14`,
                    `${new Date().getFullYear()}-02-23`,
                    `${new Date().getFullYear()}-03-08`,
                    `${new Date().getFullYear()}-05-09`,
                    `${new Date().getFullYear()}-09-01`,
                    `${new Date().getFullYear()}-04-04`, // easter
                ]
            }
        },
        methods: {
            editItem(item) {
                this.editedIndex = this.items.indexOf(item)
                this.editedItem = Object.assign({}, item)

                this.globalItems[this.globalItems.indexOf(item)] = Object.assign({}, item);
                this.searchFieldChanged();
                this.dialog = true
            },

            deleteItem(item) {
                const index = this.items.indexOf(item)
                const globalIndex = this.gloalItems.indexOf(item)
                confirm('Удалить ' + this.items[index].name + '?') && this.items.splice(index, 1) && this.globaiItems.splice(globalIndex, 1)
            },
            save() {
                if (this.$refs.editName.value != '') {
                    this.$refs.editName.error = false;
                    if (this.editedIndex > -1) {
                        Object.assign(this.items[this.editedIndex], this.editedItem)
                    } else {
                        this.items.push(this.editedItem)
                    }
                    this.close()
                }
                else {
                    this.$refs.editName.error = true;
                }
            },
            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },
            saveInventory() {
                throw 'not implemented';
            },
            getTableHeight() {
                if (window.innerHeight <= 600) {
                    this.tableHeight = window.innerHeight * 0.65;
                } else if (window.innerHeight < 800) {
                    this.tableHeight = window.innerHeight * 0.7;
                } else {
                    this.tableHeight = window.innerHeight * 0.75;
                }
            },
            cancelClick() {
                if (confirm('Отменить изменения?')) {
                    location.reload();
                }
            },
            searchFieldChanged() {
                this.items = (this.globalItems.filter(obj => {
                    return obj.name.includes(this.search);
                }))
            }
        },
        created() {
            document.title = 'Инвентарь';
            window.addEventListener("resize", this.getTableHeight);
            this.getTableHeight();
        },
        destroyed() {
            window.removeEventListener("resize", this.getTableHeight);
        },
        mounted() {
            this.items = this.globalItems;
        }
    }
</script>


<style scoped>
    #table {
        width: 80%;
        margin: auto;
        height: 10%;
    }

    #buttons {
        display: flex;
        width: 80%;
        margin: auto;
        justify-content: space-around;
    }

    .bts {
        width: 150px;
    }
</style>