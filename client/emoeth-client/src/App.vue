<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Emoeth</span>
        <span class="font-weight-light">Dashboard</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="http://localhost:8000/apiemoeth/"
        target="_blank"
      >
        <span class="mr-2">Fan of JSON ? Get directly on the API !</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <Board msg="Welcome on Emoeth Board"/>
    </v-content>
  </v-app>
</template>

<script>
import Board from './components/Board.vue';

export default {
  name: 'App',
  components: {
    Board,
  },
  data() {
    return {
    };
  },
};
</script>
