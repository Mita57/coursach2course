<template>
    <div class="mt-4 ml-2">
        <div id="table">
            <v-data-table fixed-header hide-default-footer disable-pagination :height="tableHeight" :headers="headers"
                          :items="items"
                          class="elevation-2">
                <template v-slot:item.image="{ item }">
                    <div class="p-2">
                        <v-avatar class="profile" color="white" size="100" tile>
                            <v-img :src="item.image"></v-img>
                        </v-avatar>
                    </div>
                </template>
                <template v-slot:top>
                    <v-toolbar flat color="white">
                        <v-text-field v-model="search" @input="searchFieldChanged()" class="mb-2"
                                      append-icon="mdi-magnify" dense outlined label="Поиск" hide-details/>
                        <v-spacer></v-spacer>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ on }">
                                <v-btn tile color="primary" dark class="mb-2" v-on="on">Добавить</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="headline">Предмет инвентаря</span>
                                </v-card-title>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-col>
                                                <v-text-field dense v-model="editedItem.name" ref="editName"
                                                              :error="nameError" label="Название"/>
                                            </v-col>
                                        </v-row>
                                        <v-row>
                                            <v-col>
                                                <v-text-field dense v-model="editedItem.amount" ref="editAmount"
                                                              :error="amountError" @input="validateAmount()"
                                                              :label="changeAmountLabel"/>
                                            </v-col>
                                        </v-row>
                                        <v-file-input dense accept="image/png, image/jpeg, image/bmp"
                                                      placeholder="Добавьте изображение" prepend-icon="mdi-camera"
                                                      label="Изображение"></v-file-input>

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
    import axios from 'axios';

    export default {
        name: "Inventory",
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
                globalItems: [],
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
                if (this.$refs.editName.value != '' && !this.amountError) {
                    this.nameError = false;
                    if (this.editedIndex > -1) {
                        Object.assign(this.items[this.editedIndex], this.editedItem)
                    } else {
                        this.items.push(this.editedItem)
                    }
                    this.close()
                } else {
                    this.nameError = false;
                    setTimeout(() => {
                        this.nameError = true
                    }, 1);
                }
            },
            getInventory() {
                const rw = this;
                axios.get('http://127.0.0.1:5000/getInventory').then((res) => {
                    let resp = [];
                    for (let i = 0; i < res.data.length; i++) {
                        let elem = {
                            name: res.data[i][0],
                            amount: res.data[i][1]
                        };
                        resp.push(elem);
                    }
                    rw.globalItems = resp;
                    console.log(rw.globalItems);
                    rw.syncStuff();
                }).catch((res) => {
                    console.log(res);
                })
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
            validateAmount() {
                if (isNaN(this.editedItem.amount) || this.editedItem.amount <= 0) {
                    this.amountError = false;
                    setTimeout(() => {
                        this.amountError = true;
                    }, 1);
                    this.changeAmountLabel = 'Количество должно быть числом больше 0';
                } else {
                    this.amountError = false;
                    this.changeAmountLabel = 'Количество';
                }
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
            },
            syncStuff() {
                this.items = this.globalItems;
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
            this.getInventory();
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
