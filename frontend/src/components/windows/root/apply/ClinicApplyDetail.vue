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
    <el-image v-for="qualification in qualifications"
              :src="qualification"
              style="width: 10vw;height: 15vh;display: block"
    >

    </el-image>

    <el-image v-for="photo in photos"
              :src="photo"
              style="width: 10vw;height: 15vh;display: block"
    >

    </el-image>
    <el-button size="mini" @click="changeAuthority('1')">批准</el-button>
    <el-button size="mini" @click="changeAuthority('0')">驳回</el-button>
  </div>
</template>

<script>
  export default {
    name: "ClinicApplyDetail",
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
      imageParams.append('imageType', 'all');
      imageParams.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/get_image/',
        data: imageParams
      }).then(function (response) {
        this.qualifications = response.data.qualifications;
        this.photos = response.data.photos;
      }.bind(this));
    }, methods: {
      changeAuthority: function (changeTo) {
        let params = new FormData();
        let clinicId = this.$route.params.clinicId;
        let operatorId = this.$cookies.get('operatorId');
        params.append('id', clinicId);
        params.append('usertype', '1');
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
