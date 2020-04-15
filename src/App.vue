<template>
    <div>
        <MenuBar v-if="status.loggedIn"/>
        <router-view/>
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
</style>
