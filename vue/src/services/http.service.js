import axios from 'axios';
import { stringify } from 'qs';
import app from '@/main';
import config from '@/config/app.config';
import NotificationService from '@/services/notification.service';
import VueCookies from 'vue-cookies';

const instance = axios.create({
    baseURL: config.api_url,
    paramsSerializer: params => stringify(params),
    withCredentials: true
});

instance.interceptors.request.use((request) => {
    if (typeof request.hideLoading === 'undefined' || !request.hideLoading) {
        app.$Progress.start();
    }

    return request;
}, (error) => {
    app.$Progress.finish();

    NotificationService.error('Network error. Check your connection');
    return Promise.reject(error);
});

instance.interceptors.response.use((response) => {
    app.$Progress.finish();

    // Show Api errors
    if (typeof response.data.ok !== 'undefined') {
        if (!response.data.ok) {
            NotificationService.error(response.data.desc);
            return Promise.reject(response.data.desc);
        }
    }

    return response;
}, (error) => {
    app.$Progress.finish();

    if (typeof error.response === 'undefined'
        || typeof error.response.status === 'undefined') {
        NotificationService.error('Network error. Check your connection');
        return Promise.reject(error);
    }

    // Server down
    if (error.response.status >= 500) {
        NotificationService.error('Server Unavailable.');
        return Promise.reject(error);
    }

    // Form validation errors
    if (error.response.status === 422) {
        NotificationService.error('Please correct the form and submit again.', error.response.data.message);
        return Promise.reject(error);
    }

    // Api errors that are returned with error codes
    NotificationService.stickyError(error.response.data.message);
    return Promise.reject(error);
});

export default instance;
