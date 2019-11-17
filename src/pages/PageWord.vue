<template>
        <el-row align="top"  :gutter="20">
            <el-col  :span="8">
                <div class="word-chinese-outer">
                    <p class="word-chinese" v-text="word.chinese"></p>
                </div>
            </el-col>
            <el-col :span="16">
                <div class="word-detail-outer">
                    <b class="word-detail-title">Pinyin: </b> <span class="" v-text="word.pinyin"></span>
                </div>
                <div class="word-detail-outer">
                    <b class="word-detail-title">Vietnamese: </b> <span class="" v-text="word.vietnamese"></span>
                </div>
                <div id="character-target-div">

                </div>
            </el-col>
        </el-row>
</template>

<script>
    import {mapState} from 'vuex'

    export default {
        name: "PageWord",
        data() {
            return {
                wordId : ``,
            }
        },
        computed: mapState({
            word: state => state.words.word
        }),
        created() {
            this.wordId = this.$route.params.id;

            this.$store.dispatch('words/getWord', this.wordId);

        }
    }
//TODO: coding hanzi writer.

</script>
<style scoped>
    .word-chinese-outer{
        border: solid 1px #000000;
        background-color: silver;
        width: 200px;
        /*height: 200px;*/
    }
    .word-chinese{
        font-size: 200px;

    }
    .word-detail-outer{
        padding: 20px;
        font-size: 30px;
    }
    .word-detail-title{

    }
</style>