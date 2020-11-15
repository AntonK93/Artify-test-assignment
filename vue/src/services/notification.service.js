import Vue from 'vue';

class NotificationService {
    success(text, title = 'Success!') {
        return Vue.notify({
            type: 'success',
            title,
            text,
        });
    }

    error(text, title = 'Error!') {
        return Vue.notify({
            type: 'error',
            title,
            text,
        });
    }

    stickyError(text, title) {
        return this.error(text, title);
    }
}

export default new NotificationService();
