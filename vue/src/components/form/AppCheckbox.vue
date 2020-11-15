<template>
  <div>
    <div class="form-check">
      <input type="checkbox" :id="field"
             :disabled="disabled"
             class="form-check-input"
             :class="{
                     'is-invalid': errors && errors.hasOwnProperty(field)
                 }"
             :checked="value"
             @input="onInput">
      <label class="form-check-label" :for="field">{{ label }}</label>
      <AppError v-if="errors" :field="field"/>
    </div>
  </div>
</template>

<script>
import AppError from '@/components/form/AppError';
import { mapState } from "vuex";

export default {
  components: {
    AppError,
  },
  props: {
    label: {},
    value: {},
    field: {},
    disabled: {},
  },
  computed: {
    ...mapState({
      errors: state => state.errors.requestErrors,
    }),
  },
  methods: {
    onInput(event) {
      this.$store.dispatch('errors/clearFieldError', this.field);
      return this.$emit('input', event.target.checked);
    },
  },
};
</script>
