<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Dathena</span>
        <span class="font-weight-light">Dashboard</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="http://localhost:8000/apidathena/"
        target="_blank"
      >
        <span class="mr-2">Fan of JSON ? Get directly on the API !</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <DathenaBoard msg="Welcome on Dathena Board"/>
    </v-content>
  </v-app>
</template>

<script>
import DathenaBoard from './components/DathenaBoard.vue';

export default {
  name: 'App',
  components: {
    DathenaBoard,
  },
  data() {
    return {
    };
  },
};
</script>
