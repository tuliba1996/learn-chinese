<template>
    <div class="form-container">
        <el-alert
                v-if="show_error"
            title="error alert"
            type="error"
            :closable="false"
            show-icon>
          </el-alert>
        <el-form size="medium" :model="ruleForm" status-icon ref="ruleForm" label-width="120px" class="demo-ruleForm">
            <el-form-item  label="Username" prop="pass">
                <el-input type="username" v-model="ruleForm.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="Password" prop="checkPass">
                <el-input type="password" v-model="ruleForm.password" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="submitFormLogin()">Submit</el-button>
                <el-button @click="resetForm('ruleForm')">Reset</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                token: ``,
                ruleForm: {
                    username: '',
                    password: '',
                },
                show_error: false,
            };
        },
        methods: {
            submitFormLogin() {
                this.$store.dispatch('auth/login', this.ruleForm)
                    .then(() => {
                        console.log('token', this.$store.getters["auth/token"]);
                const token = this.$store.state.auth.token;
                console.log('token', token);
                console.log('store', this.$store);
                const show_error = this.$store.state.auth.show_error;
                console.log('show', show_error);
                if (token !== '' && !show_error){
                    console.log('vaof day');
                    this.$router.push('/');
                }else{
                    this.show_error = true;
                }
                        }

                    )

            },
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