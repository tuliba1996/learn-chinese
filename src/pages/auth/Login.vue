<template>
    <div class="login">
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>Login</span>
            </div>
            <el-form size="medium" :model="ruleForm" status-icon ref="ruleForm" :rules="rules" label-width="0px" class="form-login">
                <el-alert
                    title="Login Fail, Please check email and password"
                    type="error"
                    :closable="false"
                    center
                    show-icon
                    v-if="status.loginFail || show_error"
                    class="login-alert-fail"
                >
                  </el-alert>
                <el-form-item label="Email" prop="email">
                    <el-input type="email" v-model="ruleForm.email" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="Password" prop="password">
                    <el-input @change="handleSubmit('ruleForm')" type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item class="login-form-btn">
                    <el-button type="success" :disabled="status.loggingIn" @click="handleSubmit('ruleForm')">Login</el-button>
                    <el-button type="primary" @click="goToRegister()">Register</el-button>
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
                ruleForm: {
                    email: '',
                    password: '',
                },
                show_error: false,
                submitted: false,
                rules: {
                    email: [
                        { required: true, message: 'Please input Email', trigger: 'blur', type: 'email' },
                    ],
                    password: [
                        { required: true, message: 'Please input Password', trigger: 'blur' },
                    ]
                }
            };
        },
        computed: {
            ...mapState({
                status: state => state.auth.status
            })
        },
        methods: {
            ...mapActions('auth', ['login', 'logout']),
            handleSubmit(formName) {
                this.submitted = true;
                const {email, password} = this.ruleForm;
                this.$refs[formName].validate((valid) => {
                  if (valid) {
                    this.login({email, password})
                  } else {
                    return false;
                  }
                });
            },
            goToRegister () {
                this.$router.push('/register')
            }
        }
    }
</script>

<style scoped>
    .login {
        display: flex;
        justify-content: center;
        margin-top: 100px;
        width: 40%;
    }

    .form-login {
        padding: 50px;
    }

    .box-card {
        width: 100%;
    }
    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }
    .login-form-btn {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    .login-alert-fail {
        margin-bottom: 10px;
    }
</style>