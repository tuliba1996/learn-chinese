<template>
    <div>
        <el-header>
            <MenuBar/>
        </el-header>
        <router-view/>
    </div>
</template>

<script>
    import MenuBar from './components/MenuBar'

    export default {
        name: "App",
        components: {
            MenuBar,
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
