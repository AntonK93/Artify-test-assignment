<template>
  <div class="form-group">
    <label :for="field" v-if="label">{{ label }}</label>
    <TreeSelect :value="value"
                :loading="!options"
                :multiple="multiple"
                :flat="flat"
                :defaultExpandLevel="expandLevel"
                :autoDeselectDescendants="autoDeselectDescendants"
                :autoSelectAncestors="autoSelectAncestors"
                :disabled="disabled"
                :class="{
                     'treeselect-invalid': errors && errors.hasOwnProperty(field)
                 }"
                :normalizer="normalizer"
                :placeholder="placeholder"
                valueFormat="valueFormat"
                @input="onInput($event)"
                :options="options">
      <template v-for="(_, name) in $scopedSlots" :slot="name" slot-scope="slotData">
        <slot :name="name" v-bind="slotData"/>
      </template>
      <div slot="value-label" slot-scope="{ node }">{{ node.parentNode ? `${node.parentNode.label} > ${node.label}` : node.label }}</div>
    </TreeSelect>
    <AppError v-if="errors" :field="field"/>
  </div>
</template>
<script>
import TreeSelect from '@riophae/vue-treeselect';
import AppError from '@/components/form/AppError';
import { mapState } from "vuex";

export default {
  components: {
    TreeSelect,
    AppError,
  },
  computed: {
    ...mapState({
      errors: state => state.errors.requestErrors,
    }),
  },
  props: {
    field: {},
    label: {},
    value: {},
    options: {},
    autoDeselectDescendants: {},
    autoSelectAncestors: {},
    disabled: {},
    expandLevel: {},
    placeholder: {},
    valueFormat: {
      default: 'object',
    },
    flat: {},
    multiple: {},
    normalizer: {
      type: Function,
      default(node) {
        return {
          id: node.hasOwnProperty('id') ? node.id : 0,
          label: node.hasOwnProperty('name') ? node.name : undefined,
          isDisabled: node.hasOwnProperty('is_disabled') ? node.is_disabled : undefined,
          children: node.hasOwnProperty('children') && node.children.length > 0 ? node.children : undefined,
        };
      },
    },
  },
  methods: {
    onInput(event) {
      this.$store.dispatch('errors/clearFieldError', this.field);
      return this.$emit('input', this.selectedIds(event));
    },
    selectedIds(data) {
      return data.map(dataElement => ({
        id: dataElement.id
      }));
    },
  },
};
</script>
