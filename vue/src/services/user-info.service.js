import HttpService from '@/services/http.service';

class UserInfoService {

    getUserInfo() {
        return HttpService.get('user_info')
            .then((res) => res.data);
    }

    saveUserInfo(data) {
        return HttpService.post('user_info', {
            data,
        })
            .then(res => res.data);
    }
}

export default new UserInfoService();
