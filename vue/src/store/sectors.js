import Sector from '@/store/models/sector';
import SectorService from '@/services/sector.service';

export default {
    namespaced: true,
    actions: {
        init({ dispatch }) {
            dispatch('getSectors');
        },
        getSectors({ dispatch }) {
            dispatch('setLoading', true, { root: true });
            return SectorService.getSectors()
                .then((res) => {
                    Sector.create({
                        data: res.data,
                    })
                })
                .finally(() => {
                    dispatch('setLoading', false, { root: true });
                })
        },
    },
    getters: {
        sectors() {
            return Sector.query().all();
        },
    },
};
