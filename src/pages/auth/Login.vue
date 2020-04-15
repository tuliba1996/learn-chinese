<template>
    <div class="login">
        <el-card class="box-card">
            <el-alert
                    v-if="show_error"
                    title="error alert"
                    type="error"
                    :closable="false"
                    show-icon>
            </el-alert>
            <el-form size="medium" status-icon ref="ruleForm" label-width="80px" class="form-login">
                <el-form-item label="Username" prop="pass">
                    <el-input type="username" v-model="email" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="Password" prop="checkPass">
                    <el-input type="password" v-model="password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="success" :disabled="status.loggingIn" @click="handleSubmit()">Login</el-button>
                </el-form-item>
            </el-form>
        </el-card>
    </div>
</template>

<script>
    import {mapState, mapActions} from 'vuex'

    export default {
        name: "Login",
        data() {
            return {
                email: '',
                password: '',
                show_error: false,
                submitted: false
            };
        },
        computed: {
            ...mapState({
                status: state => state.auth.status
            })
        },
        methods: {
            ...mapActions('auth', ['login', 'logout']),
            handleSubmit() {
                this.submitted = true;
                const {email, password} = this;
                if (email && password) {
                    this.login({email, password})
                }
            }
        }
    }
</script>

<style scoped>
    .login {
        display: flex;
        justify-content: center;
        margin-top: 150px;
    }

    .form-login {
        padding: 50px;
    }

    .box-card {
        width: 45%;
    }
</style>