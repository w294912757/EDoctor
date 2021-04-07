<template>
  <div>
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
  </div>
</template>

<script>
  export default {
    name: "ClinicApplyDetail",
    data() {
      return {
        qualifications: [],
        photos: [],
      }
    },
    created() {
      let clinicId = this.$route.params.clinicId;
      let operatorId = this.$cookies.get('operatorId');
      let data = new FormData();
      data.append('keyword', clinicId);
      data.append('searchtype', 'id');
      data.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/query_clinic/',
        data: data
      }).then(function (response) {
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
