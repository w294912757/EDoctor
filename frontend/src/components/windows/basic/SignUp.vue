<template>
  <div id="signupwindow">
    <el-form>
      <div style="float: left;width: 30%;margin-left: 5%">
        <el-form-item label="账号：" required style="margin-bottom: 2px" size="mini">
          <el-input v-model="username" placeholder="请输入账号" style="width: 50%"></el-input>
        </el-form-item>

        <el-form-item label="密码：" required style="margin-bottom: 2px" size="mini">
          <el-input v-model="password" placeholder="请输入密码" show-password style="width: 50%"></el-input>
        </el-form-item>

        <el-form-item label="重复密码：" required style="margin-bottom: 2px" size="mini">
          <el-input v-model="passwordverify" placeholder="请重复密码" show-password style="width: 50%"
          ></el-input>
        </el-form-item>

        <el-form-item label="用户类型：" required style="margin-bottom: 2px" size="mini">
          <el-radio v-model="usertype" label="1">诊所</el-radio>
          <el-radio v-model="usertype" label="2">医生</el-radio>
        </el-form-item>


        <el-form-item label="资质凭证:" size="mini" required>
          <el-upload
            list-type="picture-card"
            :auto-upload="false"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            ref="qualifications"
            accept="image/jpeg,image/png,image/jpg"
          >
            <i class="el-icon-plus"></i>
          </el-upload>

          <el-dialog :visible.sync="qualificationVisible">
            <img width="100%" :src="qualificationUrl" alt="">
          </el-dialog>
        </el-form-item>

        <el-form-item label="诊所/个人照片:" size="mini" required>
          <el-upload
            list-type="picture-card"
            :auto-upload="false"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
            ref="photos"
            accept="image/jpeg,image/png,image/jpg"
          >
            <i class="el-icon-plus"></i>
          </el-upload>

          <el-dialog :visible.sync="photoVisible">
            <img width="100%" :src="photoUrl" alt="">
          </el-dialog>
        </el-form-item>
      </div>

      <div style="float: left;width: 60%;margin-left: 5%">
        <div v-if="clinicSignUpWindow">
          <el-row>
            <el-col span="11">
              <el-form-item label="诊所名：" style="margin-bottom: 2px;" size="mini" required>
                <el-input v-model="clinicName" placeholder="请输入诊所名"></el-input>
              </el-form-item>
            </el-col>

            <el-col span="11">
              <el-form-item label="地址：" style="margin-bottom: 2px;" size="mini" required>
                <el-input v-model="address" placeholder="请输入地址"></el-input>
              </el-form-item>
            </el-col>
          </el-row>
          <el-row>
            <el-col span="11">
              <el-form-item label="联系电话：" style="margin-bottom: 2px;" size="mini" required>
                <el-input v-model="phoneNum" placeholder="请输入联系电话"></el-input>
              </el-form-item>
            </el-col>
            <el-col span="2">
              <div></div>
            </el-col>
            <el-col span="11">
              <el-form-item label="科室：" style="margin-bottom: 2px;" size="mini" required>
                <el-input v-model="clinicDepartment" placeholder="请输入科室"></el-input>
              </el-form-item>
            </el-col>
          </el-row>
        </div>

        <div v-if="doctorSignUpWindow">
          <div style="height: 20%">
            <el-row>
              <el-col span="6">
                <el-form-item label="姓名：" style="margin-bottom: 2px;" size="mini" required>
                  <el-input v-model="doctorName" placeholder="请输入诊所名"></el-input>
                </el-form-item>
              </el-col>
              <el-col span="12">
                <div></div>
              </el-col>
              <el-col span="6">
                <el-form-item label="科室：" style="margin-bottom: 2px;" size="mini" required>
                  <el-input v-model="doctorDepartment" placeholder="请输入科室"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>
              <el-col span="6">
                <el-form-item label="性别：" style="margin-bottom: 2px;" size="mini" required>
                  <el-input v-model="sex" placeholder="请输入性别"></el-input>
                </el-form-item>
              </el-col>
              <el-col span="12">
                <div></div>
              </el-col>
              <el-col span="6">
                <el-form-item label="年龄：" style="margin-bottom: 2px;" size="mini" required>
                  <el-input v-model="age" placeholder="请输入年龄"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
          </div>

          <div>
            <el-table
              size="mini"
              :data="tableData"
              stripe
              border
              empty-text="加载中"
              highlight-current-row
              @current-change="singleclickrow"
              style="height: 70%;margin-top: 5px;">
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
                  v-if="false"
                >
                </el-table-column>
                <el-table-column
                  sortable
                  prop="name"
                  label="名称"
                  min-width="19%">
                </el-table-column>
                <el-table-column
                  sortable
                  prop="department"
                  label="科室"
                  min-width="19%">
                </el-table-column>
                <el-table-column
                  sortable
                  prop="address"
                  label="地址"
                  min-width="19%">
                </el-table-column>
                <el-table-column
                  sortable
                  prop="phoneNum"
                  label="联系电话"
                  min-width="19%">
                </el-table-column>
              </el-table-column>
            </el-table>
          </div>
        </div>
      </div>
    </el-form>
    <div style="clear: both;margin-left: 30%">
      <p>{{message}}</p>
      <el-button @click="signup" type="button">注册</el-button>
      <router-link to="/login">
        <el-button>返回登录界面</el-button>
      </router-link>
    </div>

  </div>
</template>

<script>
  export default {
    name: "SignUp",
    data() {
      return {
        qualificationUrl: '',
        qualificationVisible: false,

        photoUrl: '',
        photoVisible: false,

        username: '',
        password: '',
        passwordverify: '',
        message: '',
        usertype: '1',

        clinicSignUpWindow: true,
        doctorSignUpWindow: false,
        clinicName: '',
        address: '',
        phoneNum: '',
        clinicDepartment: '',
        doctorName: '',
        doctorDepartment: '',
        sex: '',
        age: '',
        clinicIdOfDoctor: '',

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
      singleclickrow(row) {
        this.clinicIdOfDoctor = row.id;
        console.log(this.clinicIdOfDoctor);
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
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.qualificationUrl = file.url;
        this.qualificationVisible = true;
      },

      signup: function () {
        if (this.password !== this.passwordverify) {
          this.message = '两次输入的密码不一致，请重试!';
        } else {
          let params = new FormData();
          params.append('username', this.username);
          params.append('password', this.password);
          params.append('usertype', this.usertype);
          for (let i = 0; i < this.$refs.qualifications.uploadFiles.length; i++) {
            params.append('qualifications', this.$refs.qualifications.uploadFiles[i].raw);
          }
          for (let i = 0; i < this.$refs.photos.uploadFiles.length; i++) {
            params.append('photos', this.$refs.photos.uploadFiles[i].raw);
          }
          if (this.clinicSignUpWindow) {
            params.append('name', this.clinicName);
            params.append('department', this.clinicDepartment);
            params.append('address', this.address);
            params.append('phoneNum', this.phoneNum);
          } else {
            params.append('name', this.doctorName);
            params.append('department', this.doctorDepartment);
            params.append('sex', this.sex);
            params.append('age', this.age);
            params.append('clinicIdOfDoctor', this.clinicIdOfDoctor);
          }
          this.$axios({
            method: 'post',
            url: '/api/add_user/',
            data: params,
            headers: {'Content-Type': 'multipart/form-data'}
          }).then(function (response) {
            let checkCode = response.data.checkCode;
            if (checkCode === '3') {
              this.message = '该用户已存在，请直接登录';
            } else {
              this.$router.push({path: '/default'});
            }
          }.bind(this));
        }

      }
    },
    watch: {
      usertype(val) {
        if (val === '1') {
          this.clinicSignUpWindow = true;
          this.doctorSignUpWindow = false;
        } else {
          //加载诊所信息
          let params = new FormData();
          params.append('status', '1');
          this.$axios({
            method: 'post',
            url: '/api/show_clinic/',
            data: params
          }).then(function (response) {
            this.allClinics = response.data.data;
            this.tableData = this.allClinics;
            this.tableData_length = this.allClinics.length;
          }.bind(this));
          this.clinicSignUpWindow = false;
          this.doctorSignUpWindow = true;
        }
      }
    }
  }
</script>

<style scoped>
  #signupwindow {
    height: 100%;
    background-color: orange;
  }
</style>
