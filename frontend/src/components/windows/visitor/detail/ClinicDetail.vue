<template>
  <div>
    <div>
      <el-form>
        <el-row>
          <el-col span="11">
            <el-form-item label="诊所名：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="name" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>

          <el-col span="11">
            <el-form-item label="地址：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="address" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-col span="11">
            <el-form-item label="联系电话：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="phoneNum" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col span="2">
            <div></div>
          </el-col>
          <el-col span="11">
            <el-form-item label="科室：" style="margin-bottom: 2px;" size="mini">
              <el-input v-model="department" placeholder="" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>

    <el-button @click="goback" type="button">返回</el-button>

    <el-image v-for="photo in photos"
              :src="photo"
              style="width: 10vw;height: 15vh;display: block"
    >

    </el-image>
  </div>
</template>

<script>
  export default {
    name: "ClinicDetail",
    data() {
      return {
        qualifications: [],
        photos: [],
        name: '',
        address: '',
        department: '',
        phoneNum: '',
      }
    },
    methods: {
      goback() {
        this.$router.go(-1);
      }
    },
    created() {
      let clinicId = this.$route.params.clinicId;
      let operatorId = this.$cookies.get('operatorId');
      let params = new FormData();
      params.append('keyword', clinicId);
      params.append('searchtype', 'id');
      params.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/query_clinic/',
        data: params
      }).then(function (response) {
        let data = response.data.data;
        this.name = data.name;
        this.address = data.address;
        this.phoneNum = data.phoneNum;
        this.department = data.department;
      }.bind(this));

      let imageParams = new FormData();
      imageParams.append('id', clinicId);
      imageParams.append('ownerType', 'clinics');
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
