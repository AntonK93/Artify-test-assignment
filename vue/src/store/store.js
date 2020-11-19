import Vue from 'vue';
import Vuex from 'vuex';
import VuexORM from '@vuex-orm/core';
import sectors from '@/store/sectors';
import userInfo from '@/store/user-info';
import errors from '@/store/errors';
import Sector from '@/store/models/sector';

Vue.use(Vuex);

const database = new VuexORM.Database();

database.register(Sector);

const store = new Vuex.Store({
    plugins: [VuexORM.install(database)],
    modules: {
        sectors,
        userInfo,
        errors,
    },
    state: {
        loading: false,
    },
    created() {
        console.log('test');
    },
    mutations: {
        loading(state, loading) {
            state.loading = loading;
        },
    },
    actions: {
        init({ dispatch }) {
            dispatch('sectors/init');
            dispatch('userInfo/init');
        },
        setLoading({ commit }, loading) {
            commit('loading', loading);
        }
    },
});

export default store;
