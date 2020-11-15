import HttpService from '@/services/http.service';

class SectorService {

    getSectors() {
        return HttpService.get('sectors')
            .then((res) => {
                return res.data
            });
    }
}

export default new SectorService();
