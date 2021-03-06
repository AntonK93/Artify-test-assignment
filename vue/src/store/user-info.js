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
            return UserInfoService.getUserInfo()
                .then((res) => {
                    if (res.hasOwnProperty('data')) {
                        commit('data', res.data)
                    }
                });
        },
        updateUserInfoData({ commit }, data) {
            commit(data.name, data.value);
        },
        handleData({ dispatch }) {
            if (VueCookies.get('session_id')) {
                return dispatch('updateData');
            } else {
                return dispatch('saveData')
            }
        },
        updateData({ state, dispatch }) {
            return UserInfoService.updateUserInfo(state.data);
        },
        saveData({ state, dispatch }) {
            return UserInfoService.saveUserInfo(state.data);
        },
    },
};
