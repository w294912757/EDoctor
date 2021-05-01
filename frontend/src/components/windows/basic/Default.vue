<template>
  <div id="defaultwindow">
    <div id="myChart" :style="{width: '300px', height: '300px'}"></div>
  </div>

</template>

<script>
  export default {
    name: "Default",
    data() {
      return {}
    },
    methods: {
      drawLine() {
        // 基于准备好的dom，初始化echarts实例
        let myChart = this.$echarts.init(document.getElementById('myChart'))
        // 绘制图表
        myChart.setOption({
          title: {text: '今日诊所就诊人次排名'},
          tooltip: {},
          xAxis: {
            data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
          },
          yAxis: {},
          series: [{
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
          }]
        });
      }
    },
    created() {
      let date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      let currentdate = year+'-'+month+'-'+day;
      console.log(typeof currentdate);
      let params = new FormData();
      params.append('date1', currentdate);
      params.append('date2', currentdate);
      params.append('type', '1');
      this.$axios({
        method: 'post',
        url: '/api/date_type_statistic/',
        data: params
      }).then(function (response) {
        let checkCode = response.data;
        console.log(response);
      }.bind(this));
    },
    mounted() {
      this.drawLine();
    }

  }
</script>

<style scoped>

</style>
