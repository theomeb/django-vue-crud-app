<template>
    <div>
    <v-app id="inspire">
    <v-card>
      <v-card-title>
        Nutrition
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
        :items="desserts"
        :search="search"
      >
        <template slot="items" slot-scope="props">
          <td>{{ props.item.id }}</td>
          <td class="text-xs-right">{{ props.item.name }}</td>
          <td class="text-xs-right">{{ props.item.short_name }}</td>
          <td class="text-xs-right">{{ props.item.total_docs }}</td>
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
export default {
  name: 'DathenaBoard',
  props: {
    msg: String,
  },
  data: function(){
    return {
      search: '',
      headers: [
        {
          text: 'ID',
          align: 'left',
          value: 'id'
        },
        { text: 'Name', value: 'name' },
        { text: 'Short Name (for languages)', value: 'short_name' },
        { text: 'Total of documents', value: 'total_docs' }
      ],
      desserts: [
        {
          "name": "Afrikaans",
          "short_name": "af",
          "total_docs": 76
        },
        {
          "name": "Aragonese",
          "short_name": "an",
          "total_docs": 119
        },
        {
          "name": "Arabic",
          "short_name": "ar",
          "total_docs": 21
        },
        {
          "name": "Asturian",
          "short_name": "ast",
          "total_docs": 116
        },
        {
          "name": "Belarusian",
          "short_name": "be",
          "total_docs": 1
        },
        {
          "name": "Bulgarian",
          "short_name": "bg",
          "total_docs": 18
        },
        {
          "name": "Bengali",
          "short_name": "bn",
          "total_docs": 205
        },
      ]
    }
  }
};
</script>

