<template>
  <div id="loginwindow">
    <table>
      <tr>
        <td>用户名：</td>
        <td>
          <input class="login-input" type="text" v-model="username" placeholder="请输入账号">
        </td>
      </tr>
      <tr>
        <td>密码：</td>
        <td>
          <input lass="login-input" type="password" v-model="password" placeholder="请输入密码">
        </td>
      </tr>
    </table>
    <br>
    {{message}}
    <br>
    <button @click="login" type="submit">登陆</button>
    <router-link to="/signupwindow">
      <button>注册</button>
    </router-link>
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
