<template>
  <p>ClinicDetailWindow</p>
</template>

<script>
  export default {
    name: "ClinicDetail",
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
    }
  }
</script>

<style scoped>

</style>
