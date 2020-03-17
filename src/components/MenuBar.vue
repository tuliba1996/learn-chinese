<template>
    <div>
        <el-menu
                :default-active="activeIndex2"
                router="true"
                class="el-menu-demo"
                mode="horizontal"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b"
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
                activeIndex2: '1'
            };
        },
        methods: {}
    }
</script>

<style scoped>

</style>