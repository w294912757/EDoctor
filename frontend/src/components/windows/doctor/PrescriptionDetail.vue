<template>
  <div>
    <el-form>
      <el-form-item label="患者姓名：" size="mini" style="display: inline">
        <el-input v-model="patientName" placeholder="" :disabled="true"></el-input>
      </el-form-item>

      <el-form-item label="性别：" size="mini" style="display: inline">
        <el-input v-model="sex" placeholder="" :disabled="true"></el-input>
      </el-form-item>

      <el-form-item label="年龄：" size="mini" style="display: inline">
        <el-input v-model="age" placeholder="" :disabled="true"></el-input>
      </el-form-item>

      <el-form-item label="联系电话：" size="mini" style="display: inline">
        <el-input v-model="phoneNum" placeholder="" :disabled="true"></el-input>
      </el-form-item>

      <el-form-item label="症状：" size="mini">
        <el-input v-model="feature" placeholder="" type="textarea" :autosize="{ minRows: 2, maxRows: 6}"
                  :disabled="true"></el-input>
      </el-form-item>

      <el-form-item label="诊断结果：" size="mini">
        <el-input v-model="diagnosis" placeholder="" type="textarea" :autosize="{ minRows: 2, maxRows: 6}"
                  :disabled="true"></el-input>
      </el-form-item>

      <el-form-item label="治疗手段：" size="mini">
        <el-input v-model="treatment" placeholder="" type="textarea" :autosize="{ minRows: 2, maxRows: 6}"
                  :disabled="true"></el-input>
      </el-form-item>

      <el-button @click="back2prescriptions" type="button">返回</el-button>

    </el-form>
  </div>
</template>

<script>
  export default {
    name: "PrescriptionDetail",
    data() {
      return {
        patientName: '',
        sex: '',
        age: '',
        phoneNum: '',
        diagnosis: '',
        feature: '',
        treatment: '',

        photos: '',
      }
    },
    methods:{
      back2prescriptions() {
        this.$router.go(-1);
      }
    },
    created() {
      let prescriptionId = this.$route.params.prescriptionId;
      let params = new FormData();
      let operatorId = this.$cookies.get('operatorId');
      params.append('keyword', prescriptionId);
      params.append('searchtype', 'id');
      params.append('operatorId', operatorId);
      this.$axios({
        method: 'post',
        url: '/api/query_prescription/',
        data: params
      }).then(function (response) {
        let data = response.data.data;
        this.patientName = data.patientName;
        this.sex = data.sex;
        this.age = data.age;
        this.phoneNum = data.phoneNum;
        this.feature = data.feature;
        this.diagnosis = data.diagnosis;
        this.treatment = data.treatment;

      }.bind(this));
    }
  }
</script>

<style scoped>
  .remarks >>> .is-disabled .el-input__inner {
    　　background-color: white;
    　　border-color: white；
  }
</style>
