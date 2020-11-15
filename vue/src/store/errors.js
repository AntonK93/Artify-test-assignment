export default {
    namespaced: true,
    state: {
        requestErrors: [],
    },
    mutations: {
        requestErrors(state, requestErrors) {
            state.requestErrors = requestErrors;
        },
    },
    actions: {
        setRequestErrors({ commit }, errors) {
            commit('requestErrors', errors);
        },
        clearErrors({ commit }) {
            commit('requestErrors', []);
        },
        clearFieldError({ commit, state }, field) {
            if (state.requestErrors.hasOwnProperty(field)) {
                const errors = { ...state.requestErrors }
                delete errors[field];
                commit('requestErrors', errors);
            }
        }
    },
};
