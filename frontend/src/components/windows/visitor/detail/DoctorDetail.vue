<template>
  <p>DoctorDetailWindow</p>
</template>

<script>
  export default {
    name: "DoctorDetailWindow",
    created() {
      let doctorId = this.$route.params.doctorId;
      let data = new FormData();
      let operatorId = this.$cookies.get('operatorId');
      data.append('keyword', doctorId);
      data.append('searchtype', 'id');
      data.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/query_doctor/',
        data: data
      }).then(function (response) {
        console.log(response.data.data);
      }.bind(this));
    }
  }
</script>

<style scoped>

</style>
