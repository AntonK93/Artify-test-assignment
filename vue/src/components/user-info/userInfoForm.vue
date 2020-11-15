<template>
    <div class="d-flex justify-content-center">
      <div class="col-5">
        <div class="card card-body mt-3 mb-3">
          <div class="m-2">
            <h6>Please enter your name and pick the Sectors you are currently involved in.</h6>
            <div class="mt-3">
              <AppInput
                  :value="userInfo.name"
                  :disabled="loading"
                  label="Name:"
                  field="name"
                  placeholder="Enter your name"
                  type="text"
                  @change="updateUserInfoData({ name: 'name', value: $event })"
              />

              <AppTreeSelect
                  :value="userInfo.selected_sectors"
                  :disabled="loading"
                  label="Sectors:"
                  field="selected_sectors"
                  :multiple="true"
                  :options="sectors"
                  :flat="true"
                  :expandLevel="Infinity"
                  @input="updateUserInfoData({ name: 'selected_sectors', value: $event })"
                  placeholder="Select sectors that you are you are currently involved in."
              />

              <AppCheckbox
                  :value="userInfo.terms_agreed"
                  :disabled="loading"
                  field="terms_agreed"
                  label="Agree to terms"
                  @input="updateUserInfoData({ name: 'terms_agreed', value: $event })"
              />
              <button
                  class="btn btn-primary mr-3 float-right"
                  :disabled="loading"
                  @click="saveData">
                Save
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>

import AppTreeSelect from '@/components/form/AppTreeSelect';
import AppCheckbox from '@/components/form/AppCheckbox';
import AppInput from '@/components/form/AppInput';
import NotificationService from '@/services/notification.service';
import { mapGetters, mapState } from 'vuex';

export default {
  components: {
    AppTreeSelect,
    AppCheckbox,
    AppInput,
  },
  computed: {
    ...mapState({
      userInfo: state => state.userInfo.data,
      errors: state => state.errors.requestErrors,
      loading: state => state.loading,
    }),
    ...mapGetters({
      sectors: 'sectors/sectors',
    }),
  },
  methods: {
    updateUserInfoData(data) {
      this.$store.dispatch('userInfo/updateUserInfoData', data);
    },
    saveData() {
      this.$store.dispatch('errors/clearErrors');
      this.$store.dispatch('userInfo/saveData')
          .then((res) => {
            NotificationService.success(res.message);
          })
          .catch((err) => {
            this.$store.dispatch('errors/setRequestErrors', err.response.data.errors);
          })
    }
  },
};
</script>
