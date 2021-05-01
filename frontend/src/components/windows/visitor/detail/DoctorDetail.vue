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
    <el-button @click="goback" type="button">返回</el-button>
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
    methods: {
      goback() {
        this.$router.go(-1);
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

    }
  }
</script>

<style scoped>
  .remarks >>> .is-disabled .el-input__inner {
    　　background-color: white;
    　　border-color: white；
  }
</style>
