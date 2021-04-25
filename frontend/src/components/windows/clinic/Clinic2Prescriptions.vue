<template>
  <div id="doctorswindow">
    <el-table
      :data="tableData"
      stripe
      border
      height="100%"
      width="100%"
      @row-dblclick="doubleclickrow">
      <el-table-column>
        <template slot="header" slot-scope="scope">
          <div style="width: 15%;float: left">
            <el-select v-model="value" filterable clearable placeholder="全局搜索">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
          <div style="width: 20%;float: left;margin-left: 10px">
            <el-input
              v-model="search"
              size="mini"
              placeholder="请输入关键字"
            />
          </div>
        </template>

        <el-table-column
          sortable
          prop="id"
          label="Id"
          v-if="false">
        </el-table-column>
        <el-table-column
          sortable
          prop="doctorId"
          label="doctorId"
          v-if="false">
        </el-table-column>
        <el-table-column
          sortable
          prop="doctorName"
          label="诊断医生"
          width="100">
        </el-table-column>
        <el-table-column
          sortable
          prop="patientName"
          label="姓名"
          width="100">
        </el-table-column>
        <el-table-column
          sortable
          prop="sex"
          label="性别"
          width="100">
        </el-table-column>
        <el-table-column
          sortable
          prop="age"
          label="年龄"
          width="100">
        </el-table-column>
        <el-table-column
          sortable
          prop="phoneNum"
          label="联系电话"
          width="180">
        </el-table-column>
        <el-table-column
          sortable
          prop="feature"
          label="症状"
          width="180">
        </el-table-column>
        <el-table-column
          sortable
          prop="diagnosis"
          label="诊断"
          width="180">
        </el-table-column>
        <el-table-column
          sortable
          prop="treatment"
          label="治疗方案"
          width="180">
        </el-table-column>
      </el-table-column>
    </el-table>
    <el-pagination
      @next-click="handleNextClick"
      @prev-click="handlePrevClick"
      @current-change="handleCurrentChange"
      :current-page="currentpage"
      background
      layout="prev, pager, next"
      :total="tableData_length"
    >
    </el-pagination>
  </div>
</template>

<script>
  export default {
    name: "Clinic2Prescriptions",
    data() {
      return {
        allPrescriptions: '',
        tableData: [],
        search: "",
        currentpage: 1, //当前页面
        tableData_length: 0, //总条目数

        options: [{
          value: 'patientName',
          label: '姓名'
        }, {
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
          label: '诊断'
        }, {
          value: 'treatment',
          label: '治疗方案'
        }, {
          value: 'doctorName',
          label: '诊断医生'
        }],
        value: ''
      }
    },
    methods: {
      doubleclickrow(row) {
        this.$router.push({name: 'prescriptiondetail', params: {prescriptionId: row.id}});
      },
      handleCurrentChange(val) {
        //点击中间页的按钮 执行的方法
        this.currentpage = val;
        this.handleTableData();
      },
      handlePrevClick(val) {
        //点击向前的按钮 执行的方法
        this.currentpage = val;
        this.handleTableData();
      },
      handleNextClick(val) {
        //点击向后的按钮 执行的方法
        //val的值是传递进来的参数，如果是在第一页，点击下一页，这里的val就是2
        //触发该方法后，将val赋值给 currentpage, currentpage =>用来存放当前页面值的量
        this.currentpage = val;
        //再调用handleTableData 方法
        this.handleTableData();
      },
      handleTableData() {
        this.tableData_length = this.allPrescriptions.length;
        this.tableData = this.allPrescriptions.slice(
          (this.currentpage - 1) * 10,
          this.currentpage * 10
        );
      },
      handleSearch(val) {
        let search = val;
        if (search == "") {
          this.tableData = this.allPrescriptions;
          this.tableData_length = this.tableData.length;
        }
        if (search != "") {
          if (this.value == '') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.patientName.toLowerCase().includes(search.toLowerCase())
                || data.sex.toLowerCase().includes(search.toLowerCase())
                || data.age.toLowerCase().includes(search.toLowerCase())
                || data.phoneNum.toLowerCase().includes(search.toLowerCase())
                || data.feature.toLowerCase().includes(search.toLowerCase())
                || data.diagnosis.toLowerCase().includes(search.toLowerCase())
                || data.treatment.toLowerCase().includes(search.toLowerCase()
                || data.doctorName.toLowerCase().includes(search.toLowerCase())
                ));
          } else if (this.value == 'patientName') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.patientName.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'sex') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.sex.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'age') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.age.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'phoneNum') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.phoneNum.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'feature') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.feature.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'diagnosis') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.diagnosis.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'treatment') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.treatment.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'doctorName') {
            this.tableData = this.allPrescriptions.filter(
              (data) =>
                !search || data.doctorName.toLowerCase().includes(search.toLowerCase())
            );
          }

          this.tableData_length = this.tableData.length;
        }
      },
    },
    created() {
      let params = new FormData();
      params.append('keyword', this.$cookies.get('clinicId'));
      params.append('searchtype', 'clinicId');
      params.append('operatorId', this.$cookies.get('operatorId'));
      this.$axios({
        method: 'post',
        url: '/api/query_prescription/',
        data: params
      }).then(function (response) {
        this.allPrescriptions = response.data.data;
        this.tableData = this.allPrescriptions;
        this.tableData_length = this.allPrescriptions.length;
      }.bind(this));
    },
    watch: {
      //watch监视input输入值的变化,只要是watch变化了 search()就会被调用
      search(newVal) {
        this.handleSearch(newVal);
      },
    },
  }

</script>

<style scoped>
  #doctorswindow {
    height: 100%;
  }
</style>
