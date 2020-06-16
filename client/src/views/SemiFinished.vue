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
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ on }">
                                <v-btn tile color="primary" dark class="mb-2" v-on="on">Добавить</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="headline">Полуфабрикат</span>
                                </v-card-title>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.name" :error="nameError"
                                                           label="Название"/>
                                        </v-row>
                                        <v-row>
                                            <v-col>
                                                <v-select dense :items="doughTypes" v-model="editedItem.type" :error="typeError"
                                                           label="Тип теста" :disabled="!editedItem.isDough" solo/>
                                                <v-checkbox color="primary" v-model="editedItem.isDough" label="Тесто"></v-checkbox>
                                            </v-col>
                                        </v-row>
                                        <v-row>
                                            <v-file-input dense accept="image/png, image/jpeg, image/bmp"
                                                          placeholder="Добавьте изображение" prepend-icon="mdi-camera"
                                                          label="Изображение"/>
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
                <template v-slot:item.isDough="{ item }">
                    <div v-if="item.isDough"> {{item.type}} </div>
                    <div v-else> - </div>
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
        name: "SemiFinished",
        data() {
            return {
                search: '',
                dialog: false,
                nameError: false,
                typeError:false,
                doughTypes:['Дрожжевое', 'Дрожжевое сдобное', 'Песочное', 'Слоеное', 'Заварное', 'Бисквитное', 'Жидкое'],
                sheetsAmountError: false,

                tableHeight: 0,
                headers: [
                    {text: '', align: 'start', value: 'image'}, //img
                    {text: 'Название', align: 'start', value: 'name'},
                    {text: 'Тесто', align: 'start', value: 'isDough'},
                    {text: 'Действия', align: 'start', value: 'actions', sortable: false},
                ],
                globalItems: [],
                items: [],
                editedIndex: -1,
                editedItem: {
                    name: '',
                    image: '',
                    type: '',
                    isDough: false,
                    id: 0
                },
                defaultItem: {
                    name: '',
                    image: '',
                    type: '',
                    isDough: false,
                },
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
                const rw = this;
                const globalIndex = this.globalItems.indexOf(item);
                const id = this.globalItems[globalIndex].id;
                confirm('Удалить ' + this.globalItems[globalIndex].name + '?') &&
                this.globalItems.splice(globalIndex, 1) &&
                axios.get('http://127.0.0.1:5000/removeSemiFinished?id=' + id).then(() => {
                    rw.searchFieldChanged();
                }).catch((err) => {
                    console.log(err);
                })
            },
            save() {
                if(!this.editedItem.isDough) {
                    this.editedItem.type = 'Дрожжевое';
                }
                if (this.editedItem.name != '') {
                    this.nameError = false;
                    if (this.editedIndex > -1) {
                        Object.assign(this.items[this.editedIndex], this.editedItem);
                        let self = this;
                        axios.get('http://127.0.0.1:5000/editSemiFinished', {
                            params: {
                                name: self.editedItem.name,
                                type: self.editedItem.type,
                                id: self.editedItem.id,
                                isDough:self.editedItem.isDough,
                            }
                        }).catch((err) => {
                            console.log(err);
                        })
                    } else {
                        this.items.push(this.editedItem)
                        let self = this;
                        axios.get('http://127.0.0.1:5000/addSemiFinished', {
                            params: {
                                name: self.editedItem.name,
                                type: self.editedItem.type,
                                isDough: self.editedItem.isDough
                            }
                        }).then().catch((err) => {
                            console.log(err);
                        })
                    }
                    this.close()
                } else {
                    if(this.editedItem.name == '') {
                        this.nameError = false;
                        setTimeout(() => {
                            this.nameError = true
                        }, 1);
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
            getDoughs() {
                const rw = this;
                axios.get('http://127.0.0.1:5000/getSemiFinished').then((res) => {
                    let resp = [];
                    for (let i = 0; i < res.data.length; i++) {
                        let elem = {
                            name: res.data[i][1],
                            type: res.data[i][0],
                            id: res.data[i][3],
                            isDough: res.data[i][2],
                        };
                        resp.push(elem);
                    }
                    rw.globalItems = resp;
                    rw.syncStuff();
                }).catch((res) => {
                    console.log(res);
                })
            },
            syncStuff() {
                this.items = this.globalItems;
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
            document.title = 'Полуфабрикаты';
            window.addEventListener("resize", this.getTableHeight);
            this.getTableHeight();
        },
        destroyed() {
            window.removeEventListener("resize", this.getTableHeight);
        },
        mounted() {
            this.getDoughs();
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
