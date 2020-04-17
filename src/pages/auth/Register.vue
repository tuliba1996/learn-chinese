<template>
    <div class="register">
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>Register</span>
            </div>
            <el-form v-if="!status.registered" size="medium" :model="ruleForm" status-icon ref="ruleForm" :rules="rules"
                      class="form-register">
                <el-form-item label="First Name" prop="first_name">
                    <el-input v-model="ruleForm.first_name" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="Last Name" prop="last_name">
                    <el-input v-model="ruleForm.last_name" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="Email" prop="email">
                    <el-input type="email" v-model="ruleForm.email" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="Password" prop="password">
                    <el-input type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="Confirm Password" prop="checkPass">
                    <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="handleSubmit('ruleForm')">Register</el-button>
                </el-form-item>
            </el-form>
            <div class="register-success" v-if="status.registered">
                <el-alert
                        title="Register Success"
                        type="success"
                        :closable="false"
                        center
                        show-icon
                >
                </el-alert>
                <el-button class="register-btnLogin" type="success" @click="goToLogin()">Login</el-button>
            </div>

        </el-card>
    </div>
</template>

<script>
    import {mapActions, mapState} from "vuex";

    export default {
        name: "Register",
        data() {
            const validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('Please input the password'));
                } else {
                    if (this.ruleForm.checkPass !== '') {
                        this.$refs.ruleForm.validateField('checkPass');
                    }
                    callback();
                }
            }
            const validateCheckPass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('Please input the password again'));
                } else if (value !== this.ruleForm.password) {
                    callback(new Error('Two inputs don\'t match!'));
                } else {
                    callback();
                }
            }
            return {
                ruleForm: {
                    email: '',
                    password: '',
                    checkPass: '',
                    first_name: '',
                    last_name: '',
                },
                show_error: false,
                submitted: false,
                rules: {
                    email: [
                        {required: true, message: 'Please input Email', trigger: 'blur', type: 'email'},
                    ],
                    password: [
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    checkPass: [
                        {validator: validateCheckPass, trigger: 'blur'}
                    ],
                }
            };
        },
        computed: {
            ...mapState({
                status: state => state.auth.status
            })
        },
        methods: {
            ...mapActions('auth', ['register']),
            handleSubmit(formName) {
                // this.submitted = true;
                this.$refs[formName].validate((valid) => {
                  if (valid) {
                    const {email, password, last_name, first_name} = this.ruleForm;
                    const data = {
                        email,
                        password,
                        first_name,
                        last_name
                    }
                        this.register(data);
                  } else {
                    return false;
                  }
                });
            },
            goToLogin() {
                this.$router.push('/login')
            }
        }
    }
</script>

<style scoped>
    .register {
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }

    .form-register {
        padding-left: 30px;
        padding-right: 30px;
        padding-top: 10px;
    }

    .clearfix:before,
    .clearfix:after {
        background-color: bisque;
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }

    .box-card {
        width: 55%;
    }

    .register-success {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .register-btnLogin {
        margin-top: 20px;

    }
</style>