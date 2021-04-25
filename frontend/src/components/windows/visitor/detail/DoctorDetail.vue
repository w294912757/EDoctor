<template>
  <div>
    <div>
      <el-form>
        <el-row>
          <el-col span="4">
            <el-form-item label="姓名：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="name" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col span="16">
            <el-form-item label="所属诊所：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="clinicName" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col span="4">
            <el-form-item label="科室：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="department" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col span="11">
            <el-form-item label="性别：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="sex" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col span="2">
            <div></div>
          </el-col>
          <el-col span="11">
            <el-form-item label="年龄：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="age" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>


    <el-image v-for="photo in photos"
              :src="photo"
              style="width: 10vw;height: 15vh;display: block"
    >

    </el-image>

  </div>
</template>

<script>
  export default {
    name: "DoctorDetail",
    data() {
      return {
        qualifications: [],
        photos: [],
        name: '',
        clinicName: '',
        department: '',
        sex: '',
        age: '',
      }
    },
    created() {
      let doctorId = this.$route.params.doctorId;
      let operatorId = this.$cookies.get('operatorId');
      let params = new FormData();
      params.append('keyword', doctorId);
      params.append('searchtype', 'id');
      params.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/query_doctor/',
        data: params
      }).then(function (response) {
        let data = response.data.data;
        this.name = data.name;
        this.clinicName = data.clinicName;
        this.department = data.department;
        this.sex = data.sex;
        this.age = data.age;

      }.bind(this));

      let imageParams = new FormData();
      imageParams.append('id', doctorId);
      imageParams.append('ownerType', 'doctors');
      imageParams.append('imageType', 'photos');
      imageParams.append('operatorId', '');
      this.$axios({
        method: 'post',
        url: '/api/get_image/',
        data: imageParams
      }).then(function (response) {
        this.photos = response.data.photos;
      }.bind(this));
    }, methods: {
      changeAuthority: function (changeTo) {
        let params = new FormData();
        let doctorId = this.$route.params.doctorId;
        let operatorId = this.$cookies.get('operatorId');
        params.append('id', doctorId);
        params.append('usertype', '2');
        params.append('operatorId', operatorId);
        params.append('changeTo', changeTo);
        this.$axios({
          method: 'post',
          url: '/api/change_user_authority/',
          data: params
        }).then(function (response) {
          this.$router.go(-1);
        }.bind(this));
      }
    }
  }
</script>

<style scoped>
  .remarks >>> .is-disabled .el-input__inner {
    　　background-color: white;
    　　border-color: white；
  }
</style>
