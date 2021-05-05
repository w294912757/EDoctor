<template>
  <div id="prescriptionstatisticswindow">
    <el-date-picker
      v-model="timevalue"
      type="daterange"
      align="right"
      unlink-panels
      range-separator="至"
      start-placeholder="开始日期"
      end-placeholder="结束日期"
      :picker-options="pickerOptions"
      value-format="yyyy-MM-dd">
    </el-date-picker>

    <el-select v-model="selectvalue" placeholder="请选择统计数据" @change=changevalue>
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>

    <el-button @click="statistic">统计</el-button>
    <div id="myChart" :style="{width: '400px', height: '300px'}"></div>
  </div>
</template>

<script>
  export default {
    name: "ClinicStatistics",
    data() {
      return {
        xdata: '',
        hiddenxdata: '',
        ydata: '',

        options: [{
          value: 'sex',
          label: '性别'
        }, {
          value: 'age',
          label: '年龄'
        }, {
          value: 'feature',
          label: '症状'
        }, {
          value: 'diagnosis',
          label: '诊断结果'
        }, {
          value: 'treatment',
          label: '治疗方案'
        }],

        selectvalue: '',

        pickerOptions: {
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近15天',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 15);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        timevalue: '',

        label: ''
      }
    },
    methods: {
      changevalue(value) {
        let obj = {};
        obj = this.options.find((item) => {
          return item.value === value;
        });
        this.label = obj.label
      },

      statistic() {
        let myChart = this.$echarts.init(document.getElementById('myChart'));
        let params = new FormData();
        params.append('date1', this.timevalue[0]);
        params.append('date2', this.timevalue[1]);
        params.append('operatortype', 'clinic');
        params.append('userid', this.$cookies.get('clinicId'));
        params.append('statistictype', this.selectvalue);
        this.charttext = this.timevalue[0] + '至' + this.timevalue[1] + ' ' + this.label + '统计';
        this.$axios({
          method: 'post',
          url: '/api/date_type_statistic/',
          data: params
        }).then(function (response) {
          let data = response.data;
          console.log(data);
          myChart.setOption({
            title: {text: this.charttext},
            tooltip: {},
            xAxis: {
              data: data.xdata
            },
            yAxis: {},
            series: [{
              name: '人次',
              type: 'bar',
              data: data.ydata
            }],
          });
          myChart.hideLoading();
        }.bind(this));
      }
    },
    created() {
    },
    mounted() {
    }
  }
</script>

<style scoped>

</style>
