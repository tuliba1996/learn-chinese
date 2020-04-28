<template>
    <div class="search-word">
        <div>
            <el-autocomplete
              class="inline-input"
              v-model="search_text"
              :fetch-suggestions="querySearch"
              placeholder="Please Input"
              :trigger-on-focus="false"
              @select="handleSelectSearch"
            >
            </el-autocomplete>
        </div>
        <div v-if="text_result">
            <div>
                <h2>Chinese</h2>
                <span>{{text_result.chinese}}</span>
            </div>
            <div>
                <h2>Pinyin</h2>
                <p>{{text_result.pinyin}}</p>
            </div>
            <div>
                <h2>Vietnamese</h2>
                <p>{{text_result.vietnamese}}</p>
            </div>

        </div>
        <div id="character-target"></div>
        <el-button @click="animateWord()" type="primary">Primary</el-button>
    </div>
</template>

<script>
    import api from '../services/api';
    import authHeader from "../utils/authHeader";
    import HanziWriter from 'hanzi-writer';

    export default {
        name: "Search_word",
        data() {
            return {
                search_text: '',
                text_result: {},
                write: '',
            }
        },
        created() {
            api.defaults.headers.common['Authorization'] = authHeader();
        },
        computed () {

        },
        methods: {
            querySearch (queryString, cb){
                api.get(`common/?search=${queryString}&search_fields=vietnamese`)
                .then(res => {
                    const {data} = res;
                    const result = data.map(d =>{
                        return {'value': `${d.chinese} - ${d.vietnamese}`, 'id': d.id}
                    })
                    cb(result);
                })
            },
            handleSelectSearch(item){
                if(item){
                    api.get(`common/${item.id}`)
                    .then(res => {
                        this.text_result = res.data;
                         this.writer = HanziWriter.create('character-target', this.text_result.chinese, {
                              width: 300,
                              height: 300,
                              padding: 25,
                             showOutline: true
                        });
                    })
                }else {
                    alert('Word not found.')
                }
            },
            animateWord (){
                this.writer.animateCharacter();
            }

        }
    }
</script>

<style scoped>
    .search-word{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        width: 60%;
        height: auto;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        margin-top: 20px;
        padding-bottom: 20px;
    }
    .inline-input{
        width: 300px;
        padding-top: 20px;

    }
</style>