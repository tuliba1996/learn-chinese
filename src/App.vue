<template>
    <div>
        <MenuBar v-if="status.loggedIn"/>
        <div class="app-container">
            <router-view/>
        </div>
    </div>

</template>

<script>
    import MenuBar from './components/MenuBar'
    import {mapState} from "vuex";

    export default {
        name: "App",
        components: {
            MenuBar,
        },
        computed:{
            ...mapState({
                status: state => state.auth.status
            })
        },
        watch: {
            $route (to, from){
                // clear alert on location change
            }
        }
    }
</script>
<style lang="styl" scoped>
    @import "static/main.styl";

    .app-container {
        display: flex;
        justify-content: center;
        /*width: 60%;*/
        /*box-shadow: #cccccc;*/
        /*border: 1px solid black;*/
    }
</style>
