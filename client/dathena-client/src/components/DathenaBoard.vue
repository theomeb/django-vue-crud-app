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
        <v-dialog v-model="dialog" max-width="500px">
          <v-btn slot="activator" color="primary" dark class="mb-2">New Item</v-btn>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.name" label="Name"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.short_name" label="Short name (if language)"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.total_docs" label="Total of documents"></v-text-field>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" flat @click.native="close">Cancel</v-btn>
              <v-btn color="blue darken-1" flat @click.native="save">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-btn color="secondary" dark class="mb-2" @click.native="init"> Init database</v-btn> 
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
          <td class="justify-center layout px-0">
            <v-icon
              small
              class="mr-2"
              @click="editItem(props.item)"
            >
              edit
            </v-icon>
            <v-icon
              small
              @click="deleteItem(props.item)"
            >
              delete
            </v-icon>
          </td>
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
      dialog: false,
      choices: ['Language', 'DocType', 'Confidentiality'],
      choiceSelected: 'language',
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
        { text: 'Actions', value: 'name', sortable: false },
      ],
      items: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        short_name: 0,
        total_docs: 0,
      },
      defaultItem: {
        name: '',
        short_name: 0,
        total_docs: 0,
      }
      };
  },
  computed: {
    formTitle () {
          return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
        }
  },
  methods: {
    getData(table) {
      const path = ('http://localhost:8000/apidathena/').concat(table.toLowerCase()).concat('/?format=json');
      axios.get(path)
        .then((res) => {
          this.items = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    editItem(item) {
      this.editedIndex = this.items.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      const tableName = this.choiceSelected.toLowerCase();
      const name = item.name;
      let path = ('http://localhost:8000/apidathena/delete/?table=').concat(tableName).concat('&name=').concat(name)
      confirm('Are you sure you want to delete this item?') && this.triggerBase(path);
      this.getData(tableName);
    },
    triggerBase (path) {
      axios.get(path)
        .then((res) => {
          console.log(res.data)
        })
        .catch((error) => {
          console.error(error);
        });
    },
    close () {
      this.dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      }, 300)
      this.getData(this.choiceSelected);

    },
    save () {
      const tableName = this.choiceSelected.toLowerCase()
      if (this.editedIndex > -1) {
        const nameToChanged = this.items[this.editedIndex].name
        const name = this.editedItem.name
        const total_docs = this.editedItem.total_docs
        let path = ('http://localhost:8000/apidathena/edit/?table=').concat(tableName).concat('&name_to_changed=').concat(nameToChanged).concat('&name=').concat(name).concat('&total_docs=').concat(total_docs);
        
        if (tableName=="language") {
          const short_name = this.editedItem.short_name
          path = path.concat('&short_name=').concat(short_name);
        }
        this.triggerBase(path);

      } else {
        const name = this.editedItem.name
        const total_docs = this.editedItem.total_docs
        let path = ('http://localhost:8000/apidathena/create/?table=').concat(tableName).concat('&name=').concat(name).concat('&total_docs=').concat(total_docs);

        if (tableName=="language") {
          const short_name = this.editedItem.short_name
          path = path.concat(total_docs).concat('&short_name=').concat(short_name);
        }
        this.triggerBase(path);
      }
      this.close();
    },
    init () {
      let path = ('http://localhost:8000/apidathena/init');
      this.triggerBase(path);
    }
  },
  created() {
  },
  watch: {
    choiceSelected(newValue) {
      this.getData(newValue);
    },
    dialog (val) {
      val || this.close()
    },
  },
};
</script>

<style>
.select-box__container {
  padding-top: 30px;
}
</style>
