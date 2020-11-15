<template>
  <div class="form-group">
    <label :for="field" v-if="label">{{ label }}</label>
    <input :disabled="disabled"
           :type="type"
           :id="field"
           :placeholder="placeholder"
           class="form-control"
           :class="{
                     'is-invalid': errors && errors.hasOwnProperty(field)
                 }"
           :autocomplete="autocomplete"
           :maxlength="max"
           :value="value"
           @input="onInput($event)"
           @change="$emit('change', $event.target.value)"
           @keydown.self.enter.exact="$emit('submit', $event.target.value)"
    >
    <AppError v-if="errors" :field="field"/>
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
    type: {},
    max: {},
    disabled: {},
    placeholder: {},
    autocomplete: {
      default: 'off',
    },
  },
  computed: {
    ...mapState({
      errors: state => state.errors.requestErrors,
    }),
  },
  methods: {
    onInput(event) {
      this.$store.dispatch('errors/clearFieldError', this.field);
      return this.$emit('input', event.target.value);
    },
  },
};
</script>
