<template>
  <p>DoctorDetailWindow</p>
</template>

<script>
  export default {
    name: "DoctorDetail",
    created() {
      let doctorId = this.$route.params.doctorId;
      let params = new FormData();
      let operatorId = this.$cookies.get('operatorId');
      params.append('keyword', doctorId);
      params.append('searchtype', 'id');
      params.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/query_doctor/',
        data: params
      }).then(function (response) {
        console.log(response.data.data);
      }.bind(this));
    }
  }
</script>

<style scoped>

</style>
