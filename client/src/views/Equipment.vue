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
                                    <span class="headline">Печь</span>
                                </v-card-title>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.name" :error="nameError"
                                                          ref="editName" label="Название"/>
                                        </v-row>
                                        <v-row>
                                            <v-text-field dense v-model="editedItem.sheetsAmount" ref="editSheetsAmount"
                                                          :error="sheetsAmountError" @input="validateSheetsAmount()" type="number"
                                                          :label="sheetsAmountLabel"></v-text-field>
                                        </v-row>
                                        <v-row>
                                            <v-col>
                                                <v-select dense :items="ovenTypes" v-model="editedItem.type" :error="typeError"
                                                          ref="editType" label="Тип печи" solo/>
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
        name: "Equipment",
        data() {
            return {
                search: '',
                dialog: false,
                nameError: false,
                typeError:false,
                ovenTypes:['Подовая', 'Конвекционная', 'Пицца'],
                sheetsAmountError: false,
                sheetsAmountLabel: 'Количество противень',

                tableHeight: 0,
                headers: [
                    {text: '', align: 'start', value: 'image'}, //img
                    {text: 'Название', align: 'start', value: 'name'},
                    {text: 'Количество противень', align: 'start', value: 'sheetsAmount'},
                    {text: 'Тип', align: 'start', value: 'type'},
                    {text: 'Действия', align: 'start', value: 'actions', sortable: false},
                ],
                globalItems: [],
                items: [],
                editedIndex: -1,
                editedItem: {
                    name: '',
                    sheetsAmount: 1,
                    image: '',
                    type: ''
                },
                defaultItem: {
                    name: '',
                    sheetsAmount: 1,
                    image: '',
                    type: ''
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
                axios.get('http://127.0.0.1:5000/removeEquipment?id=' + id).then(() => {
                    rw.searchFieldChanged();
                }).catch((err) => {
                    console.log(err);
                })
            },
            save() {
                if (this.$refs.editName.value != '' && !this.sheetsAmountError && !this.editedItem.type == '') {
                    this.nameError = false;
                    if (this.editedIndex > -1) {
                        Object.assign(this.items[this.editedIndex], this.editedItem);
                        let self = this;
                        axios.get('http://127.0.0.1:5000/editEquipment', {
                            params: {
                                id: self.editedItem.id,
                                name: self.editedItem.name,
                                sheetsAmount: self.editedItem.sheetsAmount,
                                type: self.editedItem.type
                            }
                        }).catch((err) => {
                            console.log(err);
                        })
                    } else {
                        this.items.push(this.editedItem)
                        let self = this;
                        axios.get('http://127.0.0.1:5000/addEquipment', {
                            params: {
                                name: self.editedItem.name,
                                sheetsAmount: self.editedItem.sheetsAmount,
                                type: self.editedItem.type
                            }
                        }).then().catch((err) => {
                            console.log(err);
                        })
                    }
                    this.close()
                } else {
                    if(this.$refs.editName.value == '') {
                        this.nameError = false;
                        setTimeout(() => {
                            this.nameError = true
                        }, 1);
                    }
                    if(this.amountError){
                        this.amountError = false;
                        setTimeout(() => {
                            this.amountError = true
                        }, 1);
                    }
                    if(this.editedItem.type == '') {
                        this.typeError = false;
                        setTimeout(() => {
                            this.typeError = true
                        }, 1);
                    }
                }
            },
            validateSheetsAmount() {
                if (this.editedItem.sheetsAmount == "") {
                    this.sheetsAmountError = false;
                    setTimeout(() => {
                        this.sheetsAmountError = true;
                    }, 1);
                    this.sheetsAmountLabel = 'Количество противень должно быть числом больше 0';
                } else {
                    this.sheetsAmountError = false;
                    this.sheetsAmountLabel = 'Количество противень';
                }
            },
            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },
            getEquipment() {
                const rw = this;
                axios.get('http://127.0.0.1:5000/getEquipment').then((res) => {
                    let resp = [];
                    for (let i = 0; i < res.data.length; i++) {
                        let elem = {
                            name: res.data[i][1],
                            sheetsAmount: res.data[i][2],
                            id: res.data[i][0],
                            type: res.data[i][3],
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
            document.title = 'Оборудование';
            window.addEventListener("resize", this.getTableHeight);
            this.getTableHeight();
        },
        destroyed() {
            window.removeEventListener("resize", this.getTableHeight);
        },
        mounted() {
            this.getEquipment();
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
