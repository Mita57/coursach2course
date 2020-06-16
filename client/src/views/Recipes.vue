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
                        <span class="headline">Рецепт</span>
                        <v-divider style="visibility: hidden"/>
                        <v-btn tile color="primary" @click="dialog2 = true">Перейти к шагам</v-btn>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-text-field dense v-model="editedItem.name" ref="editName" :error="nameError"
                                              label="Название"/>
                            </v-row>
                            <v-row>
                                <v-text-field dense v-model="editedItem.amount" ref="editAmount" :error="amountError"
                                              label="Количество на противень"/>
                            </v-row>
                            <v-row>
                                <v-text-field dense v-model="editedItem.weight" ref="editWeight" :error="weightError"
                                              label="Вес одного"/>
                            </v-row>
                            <v-row>
                                <v-text-field dense v-model="editedItem.description"
                                              label="Описание"/>
                            </v-row>
                            <v-row>
                                <v-select :items="doughTypes" v-model="editedItem.doughType" label="Тип теста" dense
                                          solo ref="editDough" :error="doughError"/>
                            </v-row>
                            <v-row>
                                <v-select :items="ovenTypes" v-model="editedItem.ovenType" label="Тип печки" dense
                                          solo ref="editOven" :error="ovenError"/>
                            </v-row>
                            <v-row>
                                <v-file-input dense accept="image/png, image/jpeg, image/bmp"
                                              placeholder="Добавьте изображение" prepend-icon="mdi-camera"
                                              label="Изображение"/>
                            </v-row>
                            <v-row>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" text @click="close">Отменить</v-btn>
                        <v-btn color="primary" text @click="validateInputs">Сохранить</v-btn>
                    </v-card-actions>

                </v-card>
            </v-dialog>

            <v-dialog v-model="dialog2" max-width="1000px">
                <v-divider/>
                <v-card>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" tile @click="dialog3 = true">Добавить</v-btn>
                        <v-btn color="primary" tile @click="validateInputs">Сохранить</v-btn>
                    </v-card-actions>
                    <v-list three-line v-scroll">
                        <template v-for="(item, index) in items">
                            <v-subheader v-if="item.header" :key="item.header" v-text="item.header"></v-subheader>

                            <v-divider v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>

                            <v-list-item v-else :key="item.title" @click="editItem(item)">
                                <v-list-item-avatar size="100px" tile>
                                    <v-img :src="item.avatar"></v-img>
                                </v-list-item-avatar>

                                <v-list-item-content>
                                    <v-list-item-title v-html="item.title"></v-list-item-title>
                                    <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-divider/>
                        </template>
                    </v-list>
                </v-card>
            </v-dialog>

            <v-dialog v-model="dialog3" max-width="700px">
                <v-card>
                    <v-card-title>
                        <span class="headline">Рецепт</span>
                        <v-divider style="visibility: hidden"/>
                        <v-btn tile color="primary" @click="dialog2 = true">Перейти к шагам</v-btn>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-text-field dense v-model="editedItem.name" ref="editName" :error="nameError"
                                              label="Название"/>
                            </v-row>
                            <v-row>
                                <v-text-field dense v-model="editedItem.amount" ref="editAmount" :error="amountError"
                                              label="Количество на противень"/>
                            </v-row>
                            <v-row>
                                <v-text-field dense v-model="editedItem.weight" ref="editWeight" :error="weightError"
                                              label="Вес одного"/>
                            </v-row>
                            <v-row>
                                <v-text-field dense v-model="editedItem.description"
                                              label="Описание"/>
                            </v-row>
                            <v-row>
                                <v-select :items="doughTypes" v-model="editedItem.doughType" label="Тип теста" dense
                                          solo ref="editDough" :error="doughError"/>
                            </v-row>
                            <v-row>
                                <v-select :items="ovenTypes" v-model="editedItem.ovenType" label="Тип печки" dense
                                          solo ref="editOven" :error="ovenError"/>
                            </v-row>
                            <v-row>
                                <v-file-input dense accept="image/png, image/jpeg, image/bmp"
                                              placeholder="Добавьте изображение" prepend-icon="mdi-camera"
                                              label="Изображение"/>
                            </v-row>
                            <v-row>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" text @click="close">Отменить</v-btn>
                        <v-btn color="primary" text @click="validateInputs">Сохранить</v-btn>
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
                            <v-list-item-title v-html="item.title"></v-list-item-title>
                            <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
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
        name: "Recipes",
        data: () => ({
            globalItems: [],
            items: [],
            steps: [],
            dialog: false,
            dialog2: false,
            search: '',
            dialog3: false,
            listStyle: '',
            nameError: false,
            amountError: false,
            weightError: false,
            doughError: false,
            progError: false,
            ovenError: false,
            editedIndex: -1,
            doughTypes: ['Без теста', 'Дрожжевое', 'Дрожжевое сдобное', 'Песочное', 'Слоеное', 'Заварное', 'Бисквитное', 'Жидкое'],
            ovenTypes: ['Подовая', 'Конвекционная', 'Пицца', 'Без печи'],
            bakingProgs: [],
            editedItem: {
                name: '',
                doughType: '',
                amount: 1, // на противень
                weight: 1,
                description: '',
                ovenType: '',
                id: 1
            },
            defaultItem: {
                name: '',
                dough: '',
                amount: 1, // на противень
                weight: 1,
                description: '',
                ovenType: '',
            },
        }),
        methods: {
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
            deleteItem(item) {
                const rw = this;
                const globalIndex = this.gloalItems.indexOf(item)
                confirm('Удалить ' + this.items[index].name + '?') && this.globaiItems.splice(globalIndex, 1) &&
                axios.get('http://127.0.0.1:5000/removeRecipe?id=' + id).then(() => {
                    rw.searchFieldChanged();
                }).catch((err) => {
                    console.log(err);
                })
            },
            searchFieldChanged() {

            },
            validateInputs() {
                this.save();
            },
            save() {
                if (this.editedIndex > -1) {
                    Object.assign(this.items[this.editedIndex], this.editedItem)
                    let self = this;
                    axios.get('http://127.0.0.1:5000/editRecipe', {
                        params: {
                            id: self.editedItem.id,
                            name: self.editedItem.name,
                            amount: self.editedItem.amount,
                            dough: self.editedItem.doughType,
                            weight: self.editedItem.weight,
                            description: self.editedItem.description,
                            ovenType:self.editedItem.ovenType
                        }
                    }).catch((err) => {
                        console.log(err);
                    })
                } else {
                    this.items.push(this.editedItem)
                    let self = this;
                    axios.get('http://127.0.0.1:5000/addRecipe', {
                        params: {
                            name: self.editedItem.name,
                            amount: self.editedItem.amount,
                            dough: self.editedItem.doughType,
                            weight: self.editedItem.weight,
                            description: self.editedItem.description,
                            ovenType:self.editedItem.ovenType
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

            getRecipes() {
                const rw = this;
                axios.get('http://127.0.0.1:5000/getRecipes').then((res) => {
                    let resp = [];
                    for (let i = 0; i < res.data.length; i++) {
                        let elem = {
                            name: res.data[i][0],
                            amount: res.data[i][1],
                            id: res.data[i][2]
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
            }
        },
        created() {
            document.title = 'Рецепты и ТТК';
            window.addEventListener("resize", this.getListStyle);
            this.getListStyle();
            this.items = this.globalItems;
        },
        destroyed() {
            window.removeEventListener("resize", this.getListStyle);
        },
        mounted() {
            this.getRecipes();
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

