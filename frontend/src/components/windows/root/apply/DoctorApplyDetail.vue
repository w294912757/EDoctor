<template>
  <div>
    <P>姓名：{{name}}</P>
    <P>所属诊所：{{clinicName}}</P>
    <P>科室：{{department}}</P>
    <P>性别：{{sex}}</P>
    <P>年龄：{{age}}</P>
    <el-image v-for="qualification in qualifications"
              :src="qualification"
              style="width: 5vw;height: 10vh;display: block"
    >

    </el-image>

    <el-image v-for="photo in photos"
              :src="photo"
              style="width: 5vw;height: 10vh;display: block"
    >

    </el-image>
    <el-button size="mini" @click="changeAuthority('1')">批准</el-button>
    <el-button size="mini" @click="changeAuthority('0')">驳回</el-button>
  </div>
</template>

<script>
  export default {
    name: "DoctorApplyDetail",
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

</style>
