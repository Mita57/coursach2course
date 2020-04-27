import Vue from 'vue';
import Router from 'vue-router';
import Login from "./views/Login";
import Info from "@/views/Info";

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '*',
      redirect: '/info'
    },
    {
      path:'/info',
      name:'Info',
      component: Info
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ],
  mode: 'history'
});


export default router;
