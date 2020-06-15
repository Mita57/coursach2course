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
                        <v-select dense :items="ovens" class="mt-4 mr-4" v-model="oven" item-text="name" item-value="id"
                                  @change="ovenSelected" label="Выберите печку" solo>
                            <template slot="no-data">
                                <div tabindex="-1" class="v-list-item theme--light">
                                    <div class="v-list-item__content">Нет данных</div>
                                </div>
                            </template>
                        </v-select>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ on }">
                                <v-btn tile color="primary" class="mb-2" v-on="on" :disabled="addButtonDisabled">
                                    Добавить
                                </v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="headline">Программа</span>
                                </v-card-title>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.name"
                                                          :error="nameError" label="Название"/>
                                        </v-row>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.temp" :error="tempError"
                                                          label="Температура℃" type="number"></v-text-field>
                                        </v-row>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.time" :error="timeError"
                                                          label="Время(мин)" type="number"></v-text-field>
                                        </v-row>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.steam"
                                                          @input="validatePercent('steam')" :error="steamError"
                                                          label="Пар(%)" type="number"></v-text-field>
                                        </v-row>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.dryness"
                                                          @input="validatePercent('dryness')" :error="drynessError"
                                                          label="Dry(%)" type="number"></v-text-field>
                                        </v-row>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.fan"
                                                          label="Скорость вентиляторов" type="number"></v-text-field>
                                            <v-checkbox color="primary" v-model="editedItem.isP" label="P"></v-checkbox>
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

    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "BakingProgs",
        data() {
            return {
                search: '',
                dialog: false,
                addButtonDisabled: true,
                tableHeight: 0,
                headers: [
                    {text: 'Название', align: 'start', value: 'name'},
                    {text: 'T℃', align: 'start', value: 'temp'},
                    {text: 'Время(мин)', align: 'start', value: 'time'},
                    {text: 'Пар(%)', align: 'start', value: 'steam'},
                    {text: 'Dry(%)', align: 'start', value: 'dryness'},
                    {text: 'Вентилятор', align: 'start', value: 'fan', sortable: false},
                    {text: 'Действия', align: 'start', value: 'actions', sortable: false},
                ],
                globalItems: [],
                items: [],
                ovens: [],
                oven: {},
                nameError: false,
                timeError: false,
                tempError: false,
                steamError: false,
                drynessError: false,
                editedIndex: -1,
                editedItem: {
                    id: 0,
                    name: '',
                    temp: 1,
                    time: 1,
                    steam: 0,
                    dryness: 0,
                    fan: '',
                    isP: false
                },
                defaultItem: {
                    name: '',
                    temp: 1,
                    time: 1,
                    steam: 0,
                    dryness: 0,
                    fan: 0,
                    isP: false
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

            validatePercent(type) {
                if (type == "steam") {
                    if (parseInt(this.editedItem.steam) < 0 || parseInt(this.editedItem.steam) > 100 || this.editedItem.steam == '') {
                        this.steamError = false;
                        setTimeout(() => {
                            this.steamError = true
                        }, 1);
                    } else {
                        this.steamError = false;
                    }

                } else {
                    if (parseInt(this.editedItem.dryness) < 0 || parseInt(this.editedItem.dryness) > 100 || this.editedItem.dryness == '') {
                        this.drynessError = false;
                        setTimeout(() => {
                            this.drynessError = true
                        }, 1);
                    } else {
                        this.drynessError = false;
                    }

                }

            },
            deleteItem(item) {
                const globalIndex = this.globalItems.indexOf(item)
                const id = this.globalItems[globalIndex].id;
                const rw = this;

                confirm('Удалить ' + this.globalItems[globalIndex].name + '?') && this.globalItems.splice(globalIndex, 1)
                axios.get('http://127.0.0.1:5000/removeProg?id=' + id).then(() => {
                    rw.searchFieldChanged();
                }).catch((err) => {
                    console.log(err);
                })
            },
            save() {
                if (this.editedItem.name != '' && !this.steamError && !this.drynessError && this.editedItem.time != '' && this.editedItem.temp != '') {
                    this.nameError = false;
                    this.tempError = false;
                    this.timeError = false;

                    if (this.editedIndex > -1) {
                        Object.assign(this.items[this.editedIndex], this.editedItem);

                        let self = this;
                        let finalFan = this.editedItem.fan;
                        if (this.editedItem.isP) {
                            finalFan += "p";
                        }

                        axios.get('http://127.0.0.1:5000/editProg', {
                            params: {
                                id: self.editedItem.id,
                                name: self.editedItem.name,
                                temp: self.editedItem.temp,
                                time: self.editedItem.time,
                                steam: self.editedItem.steam,
                                dryness: self.editedItem.dryness,
                                fan: finalFan
                            }
                        }).catch((err) => {
                            console.log(err);
                        })
                    } else {
                        this.items.push(this.editedItem)

                        let self = this;
                        let finalFan = this.editedItem.fan;
                        if (this.editedItem.isP) {
                            finalFan += "p";
                        }

                        axios.get('http://127.0.0.1:5000/addProg', {
                            params: {
                                ovenId: self.oven,
                                name: self.editedItem.name,
                                temp: self.editedItem.temp,
                                time: self.editedItem.time,
                                steam: self.editedItem.steam,
                                dryness: self.editedItem.dryness,
                                fan: finalFan
                            }
                        }).catch((err) => {
                            console.log(err);
                        })
                    }
                    this.close()
                } else {
                    if (this.editedItem.name == "") {
                        this.nameError = false;
                        setTimeout(() => {
                            this.nameError = true
                        }, 1);
                    } else {
                        this.nameError = false;
                    }

                    if (this.editedItem.time == "") {
                        this.timeError = false;
                        setTimeout(() => {
                            this.timeError = true
                        }, 1);
                    } else {
                        this.timeError = false;
                    }

                    if (this.editedItem.temp == "") {
                        this.tempError = false;
                        setTimeout(() => {
                            this.tempError = true
                        }, 1);
                    } else {
                        this.tempError = false;
                    }
                }
            },
            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
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
            getOvens() {
                const rw = this;
                axios.get('http://127.0.0.1:5000/getEquipment').then((res) => {
                    let resp = [];
                    for (let i = 0; i < res.data.length; i++) {
                        let elem = {
                            name: res.data[i][1],
                            id: res.data[i][0],
                        };
                        resp.push(elem);
                    }
                    rw.ovens = resp;
                }).catch((res) => {
                    console.log(res);
                })
            },
            ovenSelected() {
                const rw = this;
                axios.get('http://127.0.0.1:5000/getProgs', {
                    params: {
                        id: rw.oven
                    }
                }).then((res) => {
                    let resp = [];
                    for (let i = 0; i < res.data.length; i++) {
                        let elem = {
                            temp: res.data[i][1],
                            id: res.data[i][0],
                            time: res.data[i][2],
                            steam: res.data[i][3],
                            dryness: res.data[i][4],
                            name: res.data[i][7],
                        };
                        let fan = "";
                        let isP = false;
                        let respFan = res.data[i][5];

                        if (respFan.includes('p')) {
                            fan = respFan.substring(0, respFan.length - 1);
                            isP = true;
                        } else {
                            fan = respFan;
                        }
                        elem.isP = isP;
                        elem.fan = fan;
                        resp.push(elem);
                    }
                    rw.globalItems = resp;
                    rw.syncStuff();
                    rw.addButtonDisabled = false;
                }).catch((res) => {
                    console.log(res);
                })
            },
            syncStuff() {
                this.items = this.globalItems;
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
            document.title = 'Программы выпечки';
            window.addEventListener("resize", this.getTableHeight);
            this.getTableHeight();
        },
        destroyed() {
            window.removeEventListener("resize", this.getTableHeight);
        },
        mounted() {
            this.items = this.globalItems;
            this.getOvens();
        }
    }
</script>


<style scoped>
    #table {
        width: 80%;
        margin: auto;
        height: 10%;
    }
</style>
