<template>
    <el-container>
        <el-table
                :data="words"
                style="width: 100%">
            <el-table-column
                type="index"
                width="200">
            </el-table-column>
            <el-table-column
                    prop="chinese"
                    label="Chinese"
                    width="200">
            </el-table-column>
            <el-table-column
                    prop="pinyin"
                    label="Pinyin"
                    width="200">
            </el-table-column>
            <el-table-column
                    prop="vietnamese"
                    label="Vietnamese"
                    width="200">
            </el-table-column>
            <el-table-column
                    label="Detail"
                    width="200">
                <template slot-scope="scope">
                    <router-link :to="{ name: 'word', params: { id: scope.row.id } }">Detail</router-link>
                </template>
            </el-table-column>
        </el-table>
    </el-container>

</template>

<script>

    import { mapState, mapActions } from 'vuex'
    export default {
        name: "PageLesson",
        data() {
            return {
                lessonId : ``
            }
        },
        methods: {
            ...mapActions('words', [
                'addWord',
                'deleteWord'
            ]),

        },
        computed: mapState({
            words: state => state.words.words
        }),
        created() {
            this.lessonId = this.$route.params.id;
            // console.log(this.lessonId);
            this.$store.dispatch('words/getWords', this.lessonId);
        }
    }
</script>

<style scoped>

</style>