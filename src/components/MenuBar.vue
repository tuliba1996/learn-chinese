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
            <el-menu-item  index="messages">
                Messages
            </el-menu-item>
            <el-menu-item index="login" v-if="!status.loggedIn">
                Login
            </el-menu-item>
            <el-menu-item @click="logout" v-if="status.loggedIn">
                Logout
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    import {mapActions, mapState} from "vuex";

    export default {
        name: "MenuBar",
        data() {
            return {
                activeIndex: '1',
                route: true
            };
        },
        computed: {
            ...mapState({
                status: state => state.auth.status
            })
        },
        methods: {
            ...mapActions('auth', ['login', 'logout']),
        }
    }
</script>

<style scoped>

</style>