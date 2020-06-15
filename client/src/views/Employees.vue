<template>
    <div>
        <div id="searcher" class="mt-2">
            <v-text-field v-model="search" @input="searchFieldChanged()"
                          append-icon="mdi-magnify" dense outlined label="Поиск"
                          hide-details></v-text-field>
        </div>
        <div id="list" class="mt-2 elevation-4">

            <v-dialog v-model="dialog" max-width="500px">
                <template v-slot:activator="{ on }">
                    <v-btn v-on="on" absolute dark fab bottom class="mb-12" right color="primary">
                        <v-icon>mdi-plus</v-icon>
                    </v-btn>
                </template>
                <v-card>
                    <v-card-title>
                        <span class="headline">Сотрудник</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col>
                                    <v-text-field dense v-model="editedItem.name" :error="nameError"
                                                  label="Имя"/>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-text-field dense v-model="editedItem.email" :error="emailError"
                                                  type="email" label="Email"/>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-text-field dense v-model="editedItem.pwrd" :error="pwrdError"
                                                  type="password" label="Пароль (не менее четырех символов)"/>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-select dense :items="userTypes" v-model="editedItem.type" :error="typeError"
                                              label="Тип учетной записи" solo/>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-file-input accept="image/png, image/jpeg, image/bmp"
                                              placeholder="Добавьте изображение"
                                              prepend-icon="mdi-camera" label="Изображение"/>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="danger" v-if="editedIndex != -1" text @click="deleteItem()">Удалить</v-btn>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" text @click="close">Отменить</v-btn>
                        <v-btn color="primary" text @click="validateInputs()">Сохранить</v-btn>
                    </v-card-actions>

                </v-card>
            </v-dialog>

            <v-list three-line v-scroll :style="listStyle">
                <template v-for="(item, index) in items">
                    <v-subheader v-if="item.header" :key="item.header" v-text="item.header"></v-subheader>

                    <v-divider v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>

                    <v-list-item v-else :key="item.title" @click="editItem(item)">
                        <v-list-item-avatar size="100px" tile>
                            <v-img :src="item.avatar"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
                            <v-list-item-title>{{item.name}}</v-list-item-title>
                            <v-list-item-subtitle>{{item.type}} , {{item.email}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                    <v-divider/>
                </template>
            </v-list>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "Employees",
        data: () => ({
            globalItems: [],
            items: [],
            userTypes: ['Администратор', 'Кассир', 'Пекарь'],
            dialog: false,
            nameError: false,
            emailError: false,
            pwrdError: false,
            typeError: false,
            search: '',
            listStyle: '',
            editedIndex: -1,
            editedItem: {
                name: '',
                email: '',
                pwrd: '',
                type: '',
                id: 0
            },
            defaultItem: {
                name: '',
                email: '',
                pwrd: '',
                type: '',
            },
        }),
        methods: {
            //todo: images
            getListStyle() {
                if (window.innerHeight <= 600) {
                    this.listStyle = 'height: ' + window.innerHeight * 0.80 + 'px';
                } else if (window.innerHeight < 800) {
                    this.listStyle = 'height: ' + window.innerHeight * 0.83 + 'px';
                } else {
                    this.listStyle = 'height: ' + window.innerHeight * 0.85 + 'px';
                }
            },
            editItem(item) {
                this.editedIndex = this.items.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.globalItems[this.globalItems.indexOf(item)] = Object.assign({}, item);
                this.searchFieldChanged();
                this.dialog = true
            },
            searchFieldChanged() {

            }
            ,
            deleteItem() {
                const rw = this;
                const globalIndex = this.globalItems.indexOf(this.items[this.editedIndex]);
                const id = this.globalItems[globalIndex].id;
                confirm('Удалить ' + this.globalItems[globalIndex].name + '?') &&
                this.globalItems.splice(globalIndex, 1) &&
                axios.get('http://127.0.0.1:5000/removeEmployee?id=' + id).then(() => {
                    rw.searchFieldChanged();
                }).catch((err) => {
                    console.log(err);
                })
                this.dialog = false;
            },

            validateInputs() {
                let nameFlag = false;
                let emailFlag = false;
                let pwrdFlag = false;
                let typeFlag = false;

                if (this.editedItem.name.length > 2) {
                    nameFlag = true;
                    this.nameError = false;
                } else {
                    nameFlag = false;
                    this.nameError = false;
                    setTimeout(() => {
                        this.nameError = true;
                    }, 1)
                }

                let email = this.editedItem.email;
                const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

                if (re.test(email)) {
                    emailFlag = true;
                    this.emailError = false;
                } else {
                    emailFlag = false;
                    this.emailError = false;
                    setTimeout(() => {
                        this.emailError = true;
                    }, 1)
                }

                if (this.editedItem.pwrd >= 4) {
                    pwrdFlag = true;
                    this.pwrdError = false;
                } else {
                    pwrdFlag - false;
                    this.pwrdError = false;
                    setTimeout(() => {
                        this.pwrdError = true;
                    }, 1);
                }


                if (this.editedItem.type != '') {
                    typeFlag = true;
                    this.typeError = false;
                } else {
                    typeFlag = false;
                    this.typeError = false;
                    setTimeout(() => {
                        this.typeError = true;
                    }, 1);
                }

                if (nameFlag && emailFlag && pwrdFlag && typeFlag) {
                    this.save();
                }


            },
            getEmployees() {
                const rw = this;
                axios.get('http://127.0.0.1:5000/getEmployees').then((res) => {
                    let resp = [];
                    for (let i = 0; i < res.data.length; i++) {
                        let elem = {
                            email: res.data[i][0],
                            type: res.data[i][1],
                            name: res.data[i][2],
                            id: res.data[i][3]
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
                this.items = this.globalItems
            },
            save() {
                if (this.editedIndex > -1) {
                    Object.assign(this.items[this.editedIndex], this.editedItem)

                    let self = this;
                    axios.get('http://127.0.0.1:5000/editEmployee', {
                        params: {
                            email: self.editedItem.email,
                            name: self.editedItem.name,
                            pwrd: self.editedItem.pwrd,
                            type: self.editedItem.type,
                            id: self.editedItem.id,
                        }
                    }).catch((err) => {
                        console.log(err);
                    })
                } else {
                    this.items.push(this.editedItem)
                    let self = this;

                    axios.get('http://127.0.0.1:5000/addEmployee', {
                        params: {
                            email: self.editedItem.email,
                            name: self.editedItem.name,
                            pwrd: self.editedItem.pwrd,
                            type: self.editedItem.type,
                        }
                    }).catch((err) => {
                        console.log(err);
                    })
                }
                this.close()
            },
            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },
        },
        created() {
            document.title = 'Сотрудники';
            window.addEventListener("resize", this.getListStyle);
            this.getListStyle();
            this.items = this.globalItems;
        },
        destroyed() {
            window.removeEventListener("resize", this.getListStyle);
        },
        mounted() {
            this.getEmployees();
        }
    }
</script>

<style scoped>
    #list {
        margin: auto;
        width: 80%;
        overflow-y: auto;
    }

    #searcher {
        width: 80%;
        margin: auto;
    }

</style>

