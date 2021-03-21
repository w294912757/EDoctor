<template>
  <div id="signupwindow">
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
      <tr>
        <td>重复密码：</td>
        <td>
          <input lass="login-input" type="password" v-model="passwordverify" placeholder="请重复密码">
        </td>
      </tr>
    </table>
    <br>
    <template>
      <span>用户类型</span>
      <el-radio v-model="usertype" label="1">诊所</el-radio>
      <el-radio v-model="usertype" label="2">医生</el-radio>

      <div v-show="clinicSignUpWindow">
        资格证明：<input id="qualification" type="file" accept="image/jpg,image/png,image/jpeg">
        <table>
          <tr>
            <td>诊所名：</td>
            <td>
              <input class="login-input" type="text" v-model="username" placeholder="请输入诊所名">
            </td>
          </tr>
          <tr>
            <td>地址：</td>
            <td>
              <input lass="login-input" type="password" v-model="password" placeholder="请输入密码">
            </td>
          </tr>
          <tr>
            <td>联系电话：</td>
            <td>
              <input lass="login-input" type="password" v-model="passwordverify" placeholder="请重复密码">
            </td>
          </tr>
          <tr>
            <td>科室：</td>
            <td>
              <input lass="login-input" type="password" v-model="passwordverify" placeholder="请重复密码">
            </td>
          </tr>
        </table>
      </div>

      <div v-show="doctorSignUpWindow">
        资格证明：<input id="qualification" type="file" accept="image/jpg,image/png,image/jpeg">
        <table>
          <tr>
            <td>诊所名：</td>
            <td>
              <input class="login-input" type="text" v-model="username" placeholder="请输入诊所名">
            </td>
          </tr>
          <tr>
            <td>地址：</td>
            <td>
              <input lass="login-input" type="password" v-model="password" placeholder="请输入密码">
            </td>
          </tr>
          <tr>
            <td>联系电话：</td>
            <td>
              <input lass="login-input" type="password" v-model="passwordverify" placeholder="请重复密码">
            </td>
          </tr>
          <tr>
            <td>科室：</td>
            <td>
              <input lass="login-input" type="password" v-model="passwordverify" placeholder="请重复密码">
            </td>
          </tr>
        </table>
      </div>

    </template>
    <br>
    {{message}}
    <br>
    <button @click="signup" type="submit">注册</button>
    <router-link to="/loginwindow">
      <button>返回登录界面</button>
    </router-link>
  </div>
</template>

<script>
  export default {
    name: "SignUpWindow",
    data() {
      return {
        username: '',
        password: '',
        passwordverify: '',
        message: '',
        usertype: '1',
        clinicSignUpWindow: true,
        doctorSignUpWindow: false,
      }
    },
    methods: {
      signup: function () {
        if (this.password !== this.passwordverify) {
          this.message = '两次输入的密码不一致，请重试!';
        } else {
          let data = new FormData();
          let image = document.getElementById('qualification').files[0];
          data.append('username', this.username);
          data.append('password', this.password);
          data.append('usertype', this.usertype);
          data.append('image', image);
          this.$axios({
            method: 'post',
            url: '/api/add_user/',
            data: data
          }).then(function (response) {
            let checkCode = response.data.checkCode;
            if (checkCode === '3') {
              this.message = '该用户已存在，请直接登录';
            } else {
              this.$router.push({path: '/defaultwindow'});
            }
          }.bind(this));

          if (this.usertype === '1') {

          } else {

          }
        }

      }
    },
    watch: {
      usertype(val) {
        if (val === '1') {
          this.clinicSignUpWindow = true;
          this.doctorSignUpWindow = false;
        } else {
          this.clinicSignUpWindow = false;
          this.doctorSignUpWindow = true;
        }
      }
    }
  }
</script>

<style scoped>
  #signupwindow {
    height: 100%;
    background-color: orange;
  }
</style>
