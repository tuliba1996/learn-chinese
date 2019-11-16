<template>
    <el-container>
        <el-table
                :data="lessons"
                style="width: 100%">
            <el-table-column
                    prop="id"
                    label="Id"
                    width="200">
            </el-table-column>
            <el-table-column
                    prop="name"
                    label="Name"
                    width="200">
            </el-table-column>
            <el-table-column
                    width="200">
                <template slot-scope="scope">
                    <router-link :to="{ name: 'wordinlesson', params: { id: scope.row.id } }">Go</router-link>
                </template>
            </el-table-column>
        </el-table>
    </el-container>

</template>

<script>

    import { mapState, mapActions } from 'vuex'
    export default {
        name: "Lessons",
        data() {
            return {

            }
        },
        methods: {
            ...mapActions('lessons', [
                'addLesson',
                'deleteLesson'
            ]),
        },
        computed: mapState({
            lessons: state => state.lessons.lessons
        }),
        created() {
            this.$store.dispatch('lessons/getLessons');
        }
    }
</script>

<style scoped>

</style>