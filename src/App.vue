<template>
    <div id="app">
        <el-header>
            <MenuBar/>
        </el-header>
        <router-view/>
    </div>

</template>

<script>
    import MenuBar from './components/MenuBar'
    import Store from './store/index'
    export default {
        name: "App",
        components: {
            MenuBar,
            Store
        },
    }
</script>
<style lang="styl" scoped>
    @import "static/main.styl";
    /*#app {*/
    /*    font-family:  'Roboto', sans-serif;*/
    /*    -webkit-font-smoothing: antialiased;*/
    /*    -moz-osx-font-smoothing: grayscale;*/
    /*    text-align: center;*/
    /*    color: #2c3e50;*/
    /*}*/
</style>
