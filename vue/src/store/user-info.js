import UserInfoService from '@/services/user-info.service';
import VueCookies from 'vue-cookies';

export default {
    namespaced: true,
    state: {
        loading: false,
        data: {
            name: '',
            selected_sectors: [],
            terms_agreed: 0,
        },
    },
    mutations: {
        data(state, data) {
            state.data = data;
        },
        name(state, name) {
            state.data.name = name;
        },
        selected_sectors(state, selected_sectors) {
            state.data.selected_sectors = selected_sectors;
        },
        terms_agreed(state, terms_agreed) {
            state.data.terms_agreed = terms_agreed;
        },
    },
    actions: {
        init({ dispatch }) {
            if (VueCookies.get('session_id')) {
                dispatch('getUserInfo');
            }
        },
        getUserInfo({ commit, dispatch }) {
            dispatch('setLoading', true, { root: true });
            return UserInfoService.getUserInfo()
                .then((res) => {
                    if (res.hasOwnProperty('data')) {
                        commit('data', res.data)
                    }
                })
                .finally(() => {
                    dispatch('setLoading', false, { root: true });
                })
        },
        updateUserInfoData({ commit }, data) {
            commit(data.name, data.value);
        },
        saveData({ state, dispatch }) {
            dispatch('setLoading', true, { root: true });
            return UserInfoService.saveUserInfo(state.data)
                .finally(() => {
                    dispatch('setLoading', false, { root: true });
                });
        },
    },
};
