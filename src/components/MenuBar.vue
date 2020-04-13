<template>
    <div>
        <el-menu
                :default-active="activeIndex"
                class="el-menu-demo"
                mode="horizontal"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b"
                :router="route"
        >
            <el-menu-item  index="/">Home</el-menu-item>
            <el-menu-item  index="lessons">
                Lesson
            </el-menu-item>
            <el-menu-item index="login">
                Login
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "MenuBar",
        data() {
            return {
                activeIndex: '1',
                route: true
            };
        },
        methods: {}
    }
</script>

<style scoped>

</style>