<template>
  <div id="clinicmanagewindow">
    <el-table
      :data="tableData"
      stripe
      border
      height="100%"
      width="100%"
      @row-dblclick="doubleclickrow">
      <el-table-column
        sortable
        prop="id"
        label="Id"
        v-if="false">
      </el-table-column>
      <el-table-column
        sortable
        prop="name"
        label="名称"
        width="180">
      </el-table-column>
      <el-table-column
        sortable
        prop="department"
        label="科室"
        width="180">
      </el-table-column>
      <el-table-column
        sortable
        prop="address"
        label="地址"
        width="180">
      </el-table-column>
      <el-table-column
        sortable
        prop="phoneNum"
        label="联系电话"
        width="180">
      </el-table-column>
      <el-table-column
        align="right">
        <template slot="header" slot-scope="scope">
          <div style="width: 30%;float: left">
            <el-select v-model="value" filterable clearable placeholder="全局搜索">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
          <div style="width: 65%;float: right">
            <el-input
              v-model="search"
              size="mini"
              placeholder="请输入关键字"
            />
          </div>
        </template>
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
    name: "ClinicApplyMenu",
    data() {
      return {
        allClinics: '',
        tableData: [],
        search: "",
        currentpage: 1, //当前页面
        tableData_length: 0, //总条目数

        options: [{
          value: 'name',
          label: '名称'
        }, {
          value: 'department',
          label: '科室'
        }, {
          value: 'address',
          label: '地址'
        }, {
          value: 'phoneNum',
          label: '联系电话'
        }],
        value: ''
      }
    },
    methods: {
      doubleclickrow(row) {
        this.$router.push({name: 'clinicapplydetail', params: {clinicId: row.id}});
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
        this.tableData_length = this.allClinics.length;
        this.tableData = this.allClinics.slice(
          (this.currentpage - 1) * 10,
          this.currentpage * 10
        );
      },
      handleSearch(val) {
        let search = val;
        if (search == "") {
          this.tableData = this.allClinics;
          this.tableData_length = this.tableData.length;
        }
        if (search != "") {
          if (this.value == '') {
            this.tableData = this.allClinics.filter(
              (data) =>
                !search || data.name.toLowerCase().includes(search.toLowerCase())
                || data.department.toLowerCase().includes(search.toLowerCase())
                || data.address.toLowerCase().includes(search.toLowerCase())
                || data.phoneNum.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'name') {
            this.tableData = this.allClinics.filter(
              (data) =>
                !search || data.name.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'department') {
            this.tableData = this.allClinics.filter(
              (data) =>
                !search || data.department.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'address') {
            this.tableData = this.allClinics.filter(
              (data) =>
                !search || data.address.toLowerCase().includes(search.toLowerCase())
            );
          } else if (this.value == 'phoneNum') {
            this.tableData = this.allClinics.filter(
              (data) =>
                !search || data.phoneNum.toLowerCase().includes(search.toLowerCase())
            );
          }

          this.tableData_length = this.tableData.length;
        }
      },
    },
    created() {
      //加载诊所信息
      let params = new FormData();
      params.append('status', '0');
      this.$axios({
        method: 'post',
        url: '/api/show_clinic/',
        data: params
      }).then(function (response) {
        this.allClinics = response.data.data;
        this.tableData = this.allClinics;
        this.tableData_length = this.allClinics.length;
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
  #clinicmanagewindow {
    height: 100%;
  }
</style>
