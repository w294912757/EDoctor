<template>
  <div id="loginwindow">
    <el-form>
      <el-form-item label="账号："  size="mini" required>
        <el-input v-model="username" placeholder="请输入账号"></el-input>
      </el-form-item>

      <el-form-item label="密码："  size="mini" required>
        <el-input v-model="password" placeholder="请输入密码" show-password></el-input>
      </el-form-item>

      <br>
      {{message}}
      <br>
      <el-button @click="login" type="button">登陆</el-button>
      <router-link to="/signupwindow">
        <el-button>注册</el-button>
      </router-link>

    </el-form>

  </div>
</template>

<script>

  export default {
    name: "LoginWindow",
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
          let data = new FormData();
          data.append('username', this.username);
          data.append('password', this.password);
          this.$axios({
            method: 'post',
            url: '/api/login/',
            data: data
          }).then(function (response) {
            let checkCode = response.data.checkCode;
            if (checkCode === '2') {
              let title = response.data.title;
              this.$cookies.set('title', title);
              this.$router.push({path: '/defaultwindow'});
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
    height: 100%;
    background-color: red;
  }
</style>
