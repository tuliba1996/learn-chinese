<template>
        <el-container id="app">
            <el-header>
                <MenuBar/>
            </el-header>
            <el-container>
                <el-aside width="200px"></el-aside>
                <el-main>
                    <router-view/>
                </el-main>
            </el-container>
        </el-container>

</template>

<script>
    import MenuBar from './components/MenuBar'

    export default {
        name: "App",
        data() {
            return {
                activeIndex: '1',
                activeIndex2: '1'
            };
        },
        components: {
            MenuBar
          },
        methods: {}
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
