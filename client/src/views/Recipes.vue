<template>
    <div id="list" class="mt-4 elevation-4">

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
                    <v-btn tile color="primary">Перейти к шагам</v-btn>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-text-field dense v-model="editedItem.name" ref="editName" :error="nameError" label="Название"/>
                        </v-row>
                        <v-row>
                            <v-text-field  dense v-model="editedItem.amount" ref="editAmount" :error="amountError"
                                          label="Количество"/>
                        </v-row>
                        <v-row>
                            <v-text-field dense v-model="editedItem.weight" ref="editWeight" :error="weightError"
                                          label="Вес"/>
                        </v-row>
                        <v-row>
                            <v-text-field dense v-model="editedItem.description"
                                          label="Описание"/>
                        </v-row>
                        <v-row>
                            <v-select  :items="doughTypes" v-model="editedItem.doughType" label="Тип теста" dense
                                      solo ref="editDough" :error="doughError"/>
                        </v-row>
                        <v-row>
                            <v-select :items="bakingProgs" v-model="editedItem.bakingProg" label="Программа" dense
                                      solo ref="editProg" :error="progError"/>
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
                    <v-btn color="primary" text @click="save">Сохранить</v-btn>
                </v-card-actions>

            </v-card>
        </v-dialog>

        <v-list three-line v-scroll :style="listStyle">
            <template v-for="(item, index) in items">
                <v-subheader v-if="item.header" :key="item.header" v-text="item.header"></v-subheader>

                <v-divider v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>

                <v-list-item v-else :key="item.title" @click="">
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
</template>

<script>
    export default {
        // TODO; steps dialog, search bar
        name: "Recipes",
        data: () => ({
            items: [
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                    title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
                    subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
                    title: 'Oui oui',
                    subtitle: "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
                    title: 'Birthday gift',
                    subtitle: "<span class='text--primary'>Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
                    title: 'Recipe to try',
                    subtitle: "<span class='text--primary'>Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.",
                }, {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                    title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
                    subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
                    title: 'Oui oui',
                    subtitle: "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
                    title: 'Birthday gift',
                    subtitle: "<span class='text--primary'>Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
                    title: 'Recipe to try',
                    subtitle: "<span class='text--primary'>Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                    title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
                    subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
                    title: 'Oui oui',
                    subtitle: "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
                    title: 'Birthday gift',
                    subtitle: "<span class='text--primary'>Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
                    title: 'Recipe to try',
                    subtitle: "<span class='text--primary'>Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
                    title: 'Brunch this weekend?',
                    subtitle: "<span class='text--primary'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
                    title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
                    subtitle: "<span class='text--primary'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
                    title: 'Oui oui',
                    subtitle: "<span class='text--primary'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
                    title: 'Birthday gift',
                    subtitle: "<span class='text--primary'>Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?",
                },
                {
                    avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
                    title: 'Recipe to try',
                    subtitle: "<span class='text--primary'>Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.",
                }
            ],
            dialog: false,
            listStyle: '',
            nameError: false,
            amountError: false,
            weightError: false,
            doughError: false,
            progError: false,
            ovenError: false,
            editedIndex: -1,
            doughTypes: ['Дрожжевое', 'Дрожжевое сдобное', 'Песочное', 'Слоеное', 'Заварное', 'Бисквитное', 'Жидкое'],
            ovenTypes: ['подовая', 'конвекционная', 'пицца'],
            bakingProgs: [],
            editedItem: {
                name: '',
                doughType: '',
                amount: 0, // на противень
                weight: 0,
                bakingProg: '', //idk
                description: '',
                ovenType: '',
                img: new Blob()
            },
            defaultItem: {
                name: '',
                dough: '',
                amount: 0, // на противень
                weight: 0,
                bakingProg: '', //idk
                description: '',
                ovenType: '',
                img: new Blob()
            },
        }),
        methods: {
            getListStyle() {
                if (window.innerHeight <= 600) {
                    this.listStyle = 'height: ' + window.innerHeight * 0.87 + 'px';
                } else if (window.innerHeight < 800) {
                    this.listStyle = 'height: ' + window.innerHeight * 0.89 + 'px';
                } else {
                    this.listStyle = 'height: ' + window.innerHeight * 0.91 + 'px';
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
                const index = this.items.indexOf(item)
                const globalIndex = this.gloalItems.indexOf(item)
                confirm('Удалить ' + this.items[index].name + '?') && this.items.splice(index, 1) && this.globaiItems.splice(globalIndex, 1)
            },
            save() {
                if (this.editedIndex > -1) {
                    Object.assign(this.items[this.editedIndex], this.editedItem)
                } else {
                    this.items.push(this.editedItem)
                }
                this.close()
            },
            //TODO: validators
            
            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            },
        },
        created() {
            document.title = 'Инвентарь';
            window.addEventListener("resize", this.getListStyle);
            this.getListStyle();
        },
        destroyed() {
            window.removeEventListener("resize", this.getListStyle);
        },
        // TODO: make an overlay thing that is used to create and edit recipezzzzzzzzzzzzzzzzzzzzzzzzzzzzz
    }
</script>

<style scoped>
    #list {
        margin: auto;
        width: 80%;
        overflow-y: auto;
    }

</style>

