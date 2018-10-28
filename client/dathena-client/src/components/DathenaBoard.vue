<template>
    <div>
    <v-app id="inspire">
    <v-card>
      <v-card-title>
        <v-layout wrap align-center class="select-box__container">
        <v-flex xs12 sm6 d-flex>
          <v-select
            :items="choices"
            label="Select your data"
            outline
            v-model="choiceSelected"
          ></v-select>
        </v-flex>
        </v-layout>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="items"
        :search="search"
      >
        <template slot="items" slot-scope="props">
          <td>{{ props.item.id }}</td>
          <td class="text-xs-left">{{ props.item.name }}</td>
          <td class="text-xs-left">{{ props.item.short_name }}</td>
          <td class="text-xs-left">{{ props.item.total_docs }}</td>
        </template>
        <v-alert slot="no-results" :value="true" color="error" icon="warning">
          Your search for "{{ search }}" found no results.
        </v-alert>
      </v-data-table>
    </v-card>
  </v-app>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'DathenaBoard',
  props: {
    msg: String,
  },
  data() {
    return {
      choices: ['Language', 'DocType', 'Confidentiality'],
      choiceSelected: '',
      search: '',
      headers: [
        {
          text: 'ID',
          align: 'left',
          value: 'id',
        },
        { text: 'Name', value: 'name' },
        { text: 'Short Name (for languages)', value: 'short_name' },
        { text: 'Total of documents', value: 'total_docs' },
      ],
      items: [],
    };
  },
  methods: {
    getData(table) {
      const path = ('http://localhost:8000/apidathena/').concat(table.toLowerCase()).concat('/?format=json');

      axios.get(path)
        .then((res) => {
          this.items = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
  },
  watch: {
    choiceSelected: function(newValue, oldValue) {
      this.getData(newValue)
    }
  },
};
</script>

<style>
.select-box__container {
  padding-top: 30px;
}
</style>
