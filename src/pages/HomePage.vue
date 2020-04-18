<template>
    <el-table
    ref="singleTable"
    :data="list_book"
    highlight-current-row
    style="width: 100%">
    <el-table-column
      type="index"
      width="50">
    </el-table-column>
    <el-table-column
      property="name"
      label="Name"
      width="400">
    </el-table-column>
    <el-table-column
      property="description"
      label="Description"
      width="400">
    </el-table-column>
  </el-table>
</template>

<script>
    import MenuBar from "../components/MenuBar";
    import api from '../services/api';
    import authHeader from '../utils/authHeader';
    export default {
        name: "HomePage",
        components: {
            MenuBar,
        },
        data() {
            return {
                list_book: []
            }
        },
        created() {
            api.defaults.headers.common['Authorization'] = authHeader();
            this.getBook();
            console.log('list book', this.list_book);
        },
        methods: {
            getBook() {
                api.get('book')
                .then(res => {
                    this.list_book = res.data
                    console.log('list', this.list_book)
                })
            }
        }
    }
</script>

<style scoped>

</style>