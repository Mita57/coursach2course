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
                        <v-btn tile color="accent" style="color: #7e3179" dark class="mb-2 mr-2" @click="cancelClick()">
                            Отменить
                        </v-btn>
                        <v-btn tile color="primary" dark class="mb-2 mr-2" @click="emptyList()">Отчистить</v-btn>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ on }">
                                <v-btn tile color="primary" dark class="mb-2" v-on="on">Добавить</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="headline">Продукт</span>
                                </v-card-title>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-col>
                                                <v-text-field dense v-model="editedItem.name" ref="editName" :error="nameError" label="Название"/>
                                            </v-col>
                                        </v-row>
                                        <v-row>
                                            <v-col>
                                                <v-text-field dense v-model="editedItem.amount" ref="editAmount" :error="amountError"  @input="validateAmount()" :label="changeAmountLabel"/>
                                            </v-col>
                                        </v-row>
                                        <v-row>
                                            <v-file-input accept="image/png, image/jpeg, image/bmp"
                                                          placeholder="Добавьте изображение" prepend-icon="mdi-camera"
                                                          label="Изображение"/>
                                        </v-row>
                                    </v-container>
                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer/>
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

        <div id="sidebar" class="mr-3">
            <div>
                <v-date-picker class="elevation-4" full-width id="date" v-model="date" :events="arrayEvents"
                               event-color="#7e3179" locale="ru-RU" :first-day-of-week="1"></v-date-picker>
            </div>
            <template>
                <div class="text-center">
                    <v-menu top :offset-y="true">
                        <template v-slot:activator="{ on }">
                            <v-btn large id="standard" color="primary" class="mt-4 elevation-3" dark v-on="on">
                                Стандартный
                            </v-btn>
                        </template>
                        <v-list id="v-list">
                            <v-list-item @click="uploadDefault()">
                                <v-list-item-title>Выгрузить</v-list-item-title>
                            </v-list-item>
                            <v-list-item to="/dayPlanAdmin/changeDayPlan">
                                <v-list-item-title>Изменить</v-list-item-title>
                            </v-list-item>
                        </v-list>
                    </v-menu>
                </div>
            </template>
            <v-btn tile large id="saveButton" color="primary" class="mt-3 elevation-3" @click="savePlan()">Сохранить
            </v-btn>
        </div>
    </div>

</template>

<script>
    export default {
        name: "DayPlanAdmin",
        data() {
            return {
                search: '',
                changeAmountLabel: 'Количество',
                amountError: false,
                nameError: false,
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
                        name: 'owo',
                        amount: 3,
                    },
                    {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    },
                    {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    },
                    {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    }, {
                        image: require('../assets/bready_intro.jpg'),
                        name: 'lol',
                        amount: 3,
                    },
                ],
                items: [],
                editedIndex: -1,
                editedItem: {
                    name: '',
                    amount: 1,
                    image: '',
                },
                defaultItem: {
                    name: '',
                    amount: 1,
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
        computed: {

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
                if (this.$refs.editName.value != '' && !this.amountError) {
                    this.nameError = false;
                    if (this.editedIndex > -1) {
                        Object.assign(this.items[this.editedIndex], this.editedItem)
                    } else {
                        this.items.push(this.editedItem)
                    }
                    this.close()
                }
                else {
                    this.nameError = false;
                    setTimeout(() => {this.nameError = true}, 1);
                }
            },
            validateAmount() {
                if(isNaN(this.editedItem.amount) || this.editedItem.amount <= 0) {
                    this.amountError = false;
                    setTimeout(() => {this.amountError = true;}, 1);
                    this.changeAmountLabel = 'Количество должно быть числом';
                }
                else {
                    this.amountError = false;
                    this.changeAmountLabel = 'Количество';
                }
            },
            close() {
                this.dialog = false;
                this.editedItem.amount = 0;
                this.editedItem.name = '';
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },
            uploadDefault() {
                throw 'not Implemented';
            },
            savePlan() {
                throw 'not implemented';
            },
            getTableHeight() {
                if (window.innerHeight <= 600) {
                    this.tableHeight = window.innerHeight * 0.75;
                } else if (window.innerHeight < 800) {
                    this.tableHeight = window.innerHeight * 0.8;
                } else {
                    this.tableHeight = window.innerHeight * 0.85;
                }
            },
            emptyList() {
                if (confirm('Отчистить список?')) {
                    this.items = [];
                }
            },
            searchFieldChanged() {
                this.items = (this.globalItems.filter(obj => {
                    return obj.name.includes(this.search);
                }))
            },
            cancelClick() {
                if (confirm('Отменить изменения?')) {
                    location.reload();
                }
            }

        },
        created() {
            document.title = 'Планы на день';
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
        height: 90%;
        width: 68%;
        float: left;
    }

    #sidebar {
        width: 30%;
        height: 90%;
        float: right;
    }

    #date {
        width: 100%;
    }

    #standard {
        width: 100%;
    }

    #saveButton {
        width: 100%;
    }

    #v-list {
        background-color: #f5e2a7;
    }


</style>
