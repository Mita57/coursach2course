import Vue from 'vue';
import Router from 'vue-router';
import Login from "./views/Login";
import Info from "@/views/Info";
import store from "./store/store";
import Invalid from "./views/Invalid";

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path:'*',
      component: Invalid
    },
    {
      path:'/info',
      name:'Info',
      component: Info,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path:'/invalid',
      name:'Invalid',
      component: Invalid
    },
  ],
  mode: 'history'
});

const isAdmin = (to, from, next) => {
  if(store.state.type == 'admin') {
    next();
    return
  }
  next('/invalid');
}

const isBaker = (to, from, next) => {
  if(store.state.type == 'baker') {
    next();
    return
  }
  next('/invalid');
}

const isCashier = (to, from, next) => {
  if(store.state.type == 'cashier') {
    next();
    return
  }
  next('/invalid');
}


export default router;
