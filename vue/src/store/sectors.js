import Sector from '@/store/models/sector';
import SectorService from '@/services/sector.service';

export default {
    namespaced: true,
    actions: {
        init({ dispatch }) {
            dispatch('getSectors');
        },
        getSectors({ dispatch }) {
            return SectorService.getSectors()
                .then((res) => {
                    Sector.create({
                        data: res.data,
                    })
                });
        },
    },
    getters: {
        sectors() {
            return Sector.query().all();
        },
    },
};
