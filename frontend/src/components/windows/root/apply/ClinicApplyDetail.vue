<template>
  <el-image v-for="qualification in qualifications" :src="qualification" lazy placeholder="凭证图片加载中">

  </el-image>

  <el-image v-for="photo in photos" :src="photo" lazy placeholder="诊所图片加载中">

  </el-image>
</template>

<script>
  export default {
    name: "ClinicApplyDetail",
    data() {
      return {
        qualifications: '',
        photos: '',
      }
    },
    created() {
      let clinicId = this.$route.params.clinicId;
      let data = new FormData();
      let operatorId = this.$cookies.get('operatorId');
      data.append('keyword', clinicId);
      data.append('searchtype', 'id');
      data.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/query_clinic/',
        data: data
      }).then(function (response) {
        console.log(response.data.data);
      }.bind(this));

      let imagedata = new FormData();
      imagedata.append('id', clinicId);
      imagedata.append('ownerType', 'clinics');
      imagedata.append('imageType', 'all');
      imagedata.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/get_image/',
        data: imagedata
      }).then(function (response) {
        this.qualifications = response.data.qualifications;
        this.photos = response.data.photos;
      }.bind(this));
    }
  }
</script>

<style scoped>

</style>
