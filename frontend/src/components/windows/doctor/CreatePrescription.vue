<template>
  <div id="createprescriptionwindow">
    <el-form>
      <el-form-item label="患者姓名：" size="mini" required style="display: inline">
        <el-input v-model="patientName" placeholder=""></el-input>
      </el-form-item>

      <el-form-item label="性别：" size="mini" required style="display: inline">
        <el-input v-model="sex" placeholder=""></el-input>
      </el-form-item>

      <el-form-item label="年龄：" size="mini" required style="display: inline">
        <el-input v-model="age" placeholder=""></el-input>
      </el-form-item>

      <el-form-item label="联系电话：" size="mini" required style="display: inline">
        <el-input v-model="phoneNum" placeholder=""></el-input>
      </el-form-item>

      <el-form-item label="症状：" size="mini" required>
        <el-input v-model="feature" placeholder="" type="textarea" :autosize="{ minRows: 2, maxRows: 6}"></el-input>
      </el-form-item>

      <el-form-item label="诊断结果：" size="mini" required>
        <el-input v-model="diagnosis" placeholder="" type="textarea" :autosize="{ minRows: 2, maxRows: 6}"></el-input>
      </el-form-item>

      <el-form-item label="治疗手段：" size="mini" required>
        <el-input v-model="treatment" placeholder="" type="textarea" :autosize="{ minRows: 2, maxRows: 6}"></el-input>
      </el-form-item>

      <el-button @click="createPrescription" type="button">新建</el-button>

    </el-form>

  </div>
</template>

<script>

  export default {
    name: "CreatePrescription",
    data() {
      return {

        patientName: '',
        sex: '',
        age: '',
        phoneNum: '',
        diagnosis: '',
        feature: '',
        treatment: '',
      }
    },
    methods: {

      createPrescription: function () {
        let params = new FormData();
        params.append('patientName', this.patientName);
        params.append('sex', this.sex);
        params.append('age', this.age);
        params.append('phoneNum', this.phoneNum);
        params.append('feature', this.feature);
        params.append('diagnosis', this.diagnosis);
        params.append('treatment', this.treatment);
        params.append('doctorId', this.$cookies.get('doctorId'));
        params.append('operatorId', this.$cookies.get('operatorId'));

        this.$axios({
          method: 'post',
          url: '/api/add_prescription/',
          data: params
        }).then(function (response) {
          this.$router.push({path: '/allprescriptions'});
        }.bind(this));

      }
    }
  }
</script>

<style scoped>

</style>
