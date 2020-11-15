<template>
  <div class="text-danger" v-if="errors.hasOwnProperty(field)">
        <span>
            {{ errors[field][0] }} <br>
        </span>
  </div>
</template>

<script>

import { mapState } from "vuex";

export default {
  props: {
    field: {},
  },
  computed: {
    ...mapState({
      errors: state => state.errors.requestErrors,
    }),
  },
};
</script>
