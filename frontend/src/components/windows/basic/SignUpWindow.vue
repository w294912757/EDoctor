<template>
  <div id="signupwindow">
    <el-form>
      <el-form-item label="账号：" required>
        <el-input v-model="username" placeholder="请输入账号" size="mini"></el-input>
      </el-form-item>

      <el-form-item label="密码：" required>
        <el-input v-model="password" placeholder="请输入密码" size="mini" show-password></el-input>
      </el-form-item>

      <el-form-item label="重复密码：" required>
        <el-input v-model="passwordverify" placeholder="请重复密码" size="mini" show-password></el-input>
      </el-form-item>

      <template>
        <span>用户类型</span>
        <el-radio v-model="usertype" label="1">诊所</el-radio>
        <el-radio v-model="usertype" label="2">医生</el-radio>

        <el-form-item>
          <el-upload
            list-type="picture-card"
            :auto-upload="false"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            ref="upload"
            accept="image/jpeg,image/png,image/jpg"
          >
            <i class="el-icon-plus"></i>
          </el-upload>

          <el-dialog :visible.sync="dialogVisible">
            <img width="100%" :src="dialogImageUrl" alt="">
          </el-dialog>
        </el-form-item>


        <div v-if="clinicSignUpWindow">
          <el-form-item label="诊所名：">
            <el-input v-model="clinicName" placeholder="请输入诊所名" size="mini"></el-input>
          </el-form-item>

          <el-form-item label="地址：">
            <el-input v-model="address" placeholder="请输入地址" size="mini"></el-input>
          </el-form-item>

          <el-form-item label="联系电话：">
            <el-input v-model="phoneNum" placeholder="请输入联系电话" size="mini"></el-input>
          </el-form-item>

          <el-form-item label="科室：">
            <el-input v-model="clinicDepartment" placeholder="请输入科室" size="mini"></el-input>
          </el-form-item>
        </div>

        <div v-if="doctorSignUpWindow">

          <el-form-item label="姓名：">
            <el-input v-model="doctorName" placeholder="请输入诊所名" size="mini"></el-input>
          </el-form-item>

          <el-form-item label="科室：">
            <el-input v-model="doctorDepartment" placeholder="请输入科室" size="mini"></el-input>
          </el-form-item>

          <el-form-item label="性别：">
            <el-input v-model="sex" placeholder="请输入性别" size="mini"></el-input>
          </el-form-item>

          <el-form-item label="年龄：">
            <el-input v-model="age" placeholder="请输入年龄" size="mini"></el-input>
          </el-form-item>

        </div>

      </template>
      <br>
      {{message}}
      <br>
    </el-form>
    <el-button @click="signup" type="button">注册</el-button>
    <router-link to="/loginwindow">
      <el-button>返回登录界面</el-button>
    </router-link>
  </div>

</template>

<script>
  export default {
    name: "SignUpWindow",
    data() {
      return {
        dialogImageUrl: '',
        dialogVisible: false,

        username: '',
        password: '',
        passwordverify: '',
        message: '',
        usertype: '1',

        clinicSignUpWindow: true,
        doctorSignUpWindow: false,
        clinicName: '',
        address: '',
        phoneNum: '',
        clinicDepartment: '',
        doctorName: '',
        doctorDepartment: '',
        sex: '',
        age: '',

      }
    },
    methods: {

      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },

      signup: function () {
        if (this.password !== this.passwordverify) {
          this.message = '两次输入的密码不一致，请重试!';
        } else {
          let data = new FormData();
          let images = new Array();
          for (let i = 0; i < this.$refs.upload.uploadFiles.length; i++) {
            images[i] = this.$refs.upload.uploadFiles[i].raw;
          }
          data.append('username', this.username);
          data.append('password', this.password);
          data.append('usertype', this.usertype);
          for (let i = 0; i < this.$refs.upload.uploadFiles.length; i++) {
            data.append('image', this.$refs.upload.uploadFiles[i].raw);
          }
          if (this.clinicSignUpWindow) {
            data.append('name', this.clinicName);
            data.append('department', this.clinicDepartment);
            data.append('address', this.address);
            data.append('phoneNum', this.phoneNum);
          } else {

          }
          this.$axios({
            method: 'post',
            url: '/api/add_user/',
            data: data,
            headers: {'Content-Type': 'multipart/form-data'}
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
