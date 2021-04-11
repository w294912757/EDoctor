<template>
  <p>ClinicDetailWindow</p>
</template>

<script>
  export default {
    name: "ClinicDetail",
    created() {
      let clinicId = this.$route.params.clinicId;
      let params = new FormData();
      let operatorId = this.$cookies.get('operatorId');
      params.append('keyword', clinicId);
      params.append('searchtype', 'id');
      params.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/query_clinic/',
        data: params
      }).then(function (response) {
        console.log(response.data.data);
      }.bind(this));
    }
  }
</script>

<style scoped>

</style>
