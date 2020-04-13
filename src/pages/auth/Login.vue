<template>
    <div class="form-container">
        <el-alert
                v-if="show_error"
            title="error alert"
            type="error"
            :closable="false"
            show-icon>
          </el-alert>
        <el-form size="medium" status-icon ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item  label="Username" prop="pass">
                <el-input type="username" v-model="username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="Password" prop="checkPass">
                <el-input type="password" v-model="password" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" :disabled="status.loggingIn" @click="handleSubmit()">Submit</el-button>
                <el-button>Reset</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    import { mapState, mapActions } from 'vuex'
    export default {
        name: "Login",
        data() {
            return {
                username: '',
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
            handleSubmit () {
                this.submitted = true;
                const { username, password } = this;
                if (username && password) {
                    this.login({ username, password })
                }
            }
        }
    }
</script>

<style scoped>
    .form-container{
        display: flex;
        justify-content: center;
        margin-top: 100px;

    }
    .demo-ruleForm{
        width: 40%;
    }
</style>