import Vue from 'vue';
import Router from 'vue-router';
import Login from "./views/Login";
import Info from "@/views/Info";
import store from "./store/store";
import Invalid from "./views/Invalid";
import DayPlanAdmin from "./views/DayPlanAdmin";
import ChangeDefaultDayPlan from "./views/ChangeDefaultDayPlan";
import Inventory from "./views/Inventory";
import Equipment from "./views/Equipment";
import DayPlanBaker from "./views/DayPlanBaker";
import Recipes from "./views/Recipes";
import Employees from "./views/Employees";
import RecipesBaker from "./views/RecipesBaker";
import CheckList from "./views/CheckList";
import OnlineOrders from "./views/OnlineOrders";
import KitchenSituation from "./views/KitchenSituation";
import Profile from "./views/Profile";
import BakingProgs from "./views/BakingProgs";
import SemiFinished from "./views/SemiFinished";

Vue.use(Router);


const isAdmin = (to, from, next) => {
    if (store.state.type == 'admin') {
        next();
        return
    }
    next('/invalid');
}


const router = new Router({
    routes: [
        {
            path: '/',
            name: 'Info',
            component: Info,
        },
        {
            path: '/info',
            name: 'Info',
            component: Info,
        },
        {
            path: '/login',
            name: 'Login',
            component: Login,
        },
        {
            path: '/invalid',
            name: 'Invalid',
            component: Invalid,
        },
        {
            path: '/dayPlanAdmin',
            name: 'dayPlanAdmin',
            component: DayPlanAdmin,
            beforeEnter: isAdmin,
        },
        {
            path: '/dayPlanAdmin/changeDayPlan',
            name: 'ChangeDayPlan',
            component: ChangeDefaultDayPlan,
            beforeEnter: isAdmin
        },
        {
            path: '/inventory',
            name: 'Inventory',
            component: Inventory,
            beforeEnter: isAdmin
        },
        {
            path: '/equipment',
            name: 'Equipment',
            component: Equipment,
            beforeEnter: isAdmin
        },
        {
            path: '/bakingProgs',
            name: 'BakingProgs',
            component: BakingProgs,
            beforeEnter: isAdmin
        },
        {
            path: '/semiFinished',
            name:'SemiFinished',
            component: SemiFinished,
            beforeEnter:isAdmin
        },
        {
            path: '/recipes',
            name: 'Recipes',
            component: Recipes,
            beforeEnter: isAdmin
        },
        {
            path: '/employees',
            name: 'Employees',
            component: Employees,
            beforeEnter: isAdmin
        },
        {
            path: '/dayPlanBaker',
            name: 'DayPlanBaker',
            component: DayPlanBaker,
            beforeEnter: isBaker
        },
        {
            path: '/recipesBaker',
            name: 'RecipesBaker',
            component: RecipesBaker,
            beforeEnter: isBaker
        },
        {
            path: '/checklist',
            name: 'CheckList',
            component: CheckList,
            beforeEnter: isBaker
        },
        {
            path: '/onlineOrders',
            name: 'OnlineOrders',
            component: OnlineOrders,
            beforeEnter: isCashier
        },
        {
            path: '/kitchenSituation',
            name: 'KitchenSituation',
            component: KitchenSituation,
            beforeEnter: isCashier
        },
        {
            path: '/profile',
            name: 'Profile',
            component: Profile,
            beforeEnter: isAuth
        },
        {
            path: '*',
            component: Invalid
        },
    ],
    mode: 'history'
});

const isBaker = (to, from, next) => {
    if (store.state.type == 'baker') {
        next();
        return
    }
    next('/invalid');
}

const isCashier = (to, from, next) => {
    if (store.state.type == 'cashier') {
        next();
        return
    }
    next('/invalid');
    recipesBaker
}

const isAuth = (to, from, next) => {
    if (store.state.loggedIn) {
        next();
        return;
    }
    next('/invalid');
}


export default router;
