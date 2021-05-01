<template>
  <div id="loginwindow">
    <el-form>
      <el-form-item label="账号：" size="mini" required>
        <el-input v-model="username" placeholder="请输入账号"></el-input>
      </el-form-item>

      <el-form-item label="密码：" size="mini" required>
        <el-input v-model="password" placeholder="请输入密码" show-password></el-input>
      </el-form-item>

      <br>
      {{message}}
      <br>
      <el-button @click="login" type="button">登陆</el-button>
      <router-link to="/signup">
        <el-button>注册</el-button>
      </router-link>

    </el-form>

  </div>
</template>

<script>

  export default {
    name: "Login",
    data() {
      return {
        username: '',
        password: '',
        message: ''
      }
    },
    methods: {
      login: function () {
        if (this.username == '') {
          this.message = '请输入用户名';
        } else if (this.password == '') {
          this.message = '请输入密码';
        } else {
          let params = new FormData();
          params.append('username', this.username);
          params.append('password', this.password);
          this.$axios({
            method: 'post',
            url: '/api/login/',
            data: params
          }).then(function (response) {
            let checkCode = response.data.checkCode;
            console.log(response);
            if (checkCode === '2') {
              let usertype = this.$cookies.get('usertype')
              if (usertype == '1') {
                this.$router.push({path: '/clinicdefault'});
              } else if (usertype == '2') {
                this.$router.push({path: '/doctordefault'});
              } else if (usertype == '3') {
                this.$router.push({path: '/rootdefault'});
              }


            } else if (checkCode === '1') {
              this.message = '该用户不存在，请注册！';
            } else if (checkCode === '3') {
              this.message = '密码错误，请重试！';
            }
          }.bind(this));
        }

      }
    },
  }
</script>

<style scoped>
  #loginwindow {
    height: 80%;
    width: 50vw;
    background-color: yellow;
  }
</style>
