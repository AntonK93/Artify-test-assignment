import Vue from 'vue';
import VueProgressBar from 'vue-progressbar';
import VueNotifications from 'vue-notification';
import { ModalPlugin } from 'bootstrap-vue';
import router from './router/router';
import App from './app.vue';
import store from './store/store';
import progressbarConfig from './config/progressbar.config';

Vue.use(VueNotifications);
Vue.use(ModalPlugin);
Vue.use(VueProgressBar, progressbarConfig);

let initDone = false;

router.beforeEach((to, from, next) => {
    if (!initDone) {
        store.dispatch('init', to);
        initDone = true;
    }
    next();
});

const app = new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount('#app');

export default app;
