<template>
  <div id="defaultwindow">
    <div id="myChart" :style="{width: '300px', height: '300px'}"></div>
  </div>

</template>

<script>
  export default {
    name: "Default",
    data() {
      return {
        clinicsname: '',
        clinicsid: '',
        frequency: ''
      }
    },
    methods: {},
    created() {
    },
    mounted() {
      let myChart = this.$echarts.init(document.getElementById('myChart'));
      myChart.showLoading({text: '正在加载数据'});
      let date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      let currentdate = year + '-' + month + '-' + day;
      let params = new FormData();
      console.log(currentdate);
      params.append('date1', currentdate);
      params.append('date2', currentdate);
      params.append('type', 'mostclinictoday');
      this.$axios({
        method: 'post',
        url: '/api/date_type_statistic/',
        data: params
      }).then(function (response) {
        let data = response.data;
        this.clinicsid = data.clinicsid;
        this.clinicsname = data.clinicsname;
        this.frequency = data.frequency;
        myChart.setOption({
          title: {text: '今日诊所就诊人次排名'},
          tooltip: {},
          xAxis: {
            data: this.clinicsname
          },
          yAxis: {},
          series: [{
            name: '人次',
            type: 'bar',
            data: this.frequency
          }],
        });
        myChart.hideLoading();
      }.bind(this));
    }

  }
</script>

<style scoped>

</style>
