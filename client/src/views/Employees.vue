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
                    <span class="headline">Сотрудник</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col>
                                <v-text-field dense v-model="editedItem.name" :error="nameError" ref="editName" label="Имя"/>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-text-field dense v-model="editedItem.email" :error="emailError" ref="editEmail" type="email" label="Email"/>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-text-field dense v-model="editedItem.pwrd" :error="pwrdError" ref="editPwrd" type="password" label="Пароль (не менее четырех символов)"/>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-select dense :items="userTypes" v-model="editedItem.type" :error="typeError" ref="editType" label="Тип учетной записи" solo/>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-file-input accept="image/png, image/jpeg, image/bmp" placeholder="Добавьте изображение" prepend-icon="mdi-camera" label="Изображение"/>
                        </v-row>
                    </v-container>
                </v-card-text>
                <v-card-actions>
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
        name: "Employees",
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
            userTypes: ['Администратор', 'Кассир', 'Пекарь'],
            dialog: false,
            nameError: false,
            emailError: false,
            pwrdError: false,
            typeError: false,
            listStyle: '',
            editedIndex: -1,
            editedItem: {
                name: '',
                email: '',
                pwrd: '',
                type: '',
                img: new Blob()
            },
            defaultItem: {
                name: '',
                email: '',
                pwrd: '',
                type: '',
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
            validateInputs() {
                let nameFlag = false;
                let emailFlag = false;
                let pwrdFlag = false;
                let typeFlag = false;

                if(this.$refs.editName.value.length > 0) {
                    nameFlag = true;
                    this.nameError = false;
                }
                else {
                    nameFlag = false;
                    this.nameError = false;
                    setTimeout(() => {this.nameError = true;}, 1)
                }

                let email = this.$refs.editEmail.value;
                const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

                if(re.test(email)) {
                    emailFlag = true;
                    this.emailError = false;
                }
                else {
                    emailFlag = false;
                    this.emailError = false;
                    setTimeout(() => {this.emailError = true;}, 1)
                }

                if(this.$refs.editPwrd.value.length >= 4) {
                    pwrdFlag = true;
                    this.pwrdError = false;
                }
                else {
                    pwrdFlag - false;
                    this.pwrdError = false;
                    setTimeout(() => {this.pwrdError = true;}, 1);
                }

                if(this.$refs.editType.selectedIndex != -1) {
                    typeFlag = true;
                    this.typeError = false;
                }
                else {
                    typeFlag = false;
                    this.typeError = false;
                    setTimeout(() => {this.typeError = true;}, 1);
                }

                console.log('dsasdasd');
                if(nameFlag && emailFlag && pwrdFlag && typeFlag) {
                    this.save();
                }


            },
            save() {
                if (this.editedIndex > -1) {
                    Object.assign(this.items[this.editedIndex], this.editedItem)
                } else {
                    this.items.push(this.editedItem)
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

