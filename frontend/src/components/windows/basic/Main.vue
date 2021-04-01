<template>
  <div id="mainwindow">
    <el-row gutter="20">
      <el-col :span="4">
        <div id="navigatordiv">
          <Clinic v-show="clinicNavigatorShow" ref="clinicnavigator"></Clinic>
          <Doctor v-show="doctorNavigatorShow" ref="doctornavigator"></Doctor>
          <Root v-show="rootNavigatorShow" ref="rootnavigator"></Root>
          <Visitor v-show="visitorNavigatorShow" ref="visitornavigator"></Visitor>
        </div>
      </el-col>
      <el-col :span="20">
        <div id="routerdiv">
          <router-view>
          </router-view>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import Clinic from "../../navigators/Clinic";
  import Doctor from "../../navigators/Doctor";
  import Root from "../../navigators/Root";
  import Visitor from "../../navigators/Visitor";


  export default {
    name: "Main",
    components: {Visitor, Root, Doctor, Clinic},
    data() {
      return {
        title: '',
        clinicNavigatorShow: false,
        doctorNavigatorShow: false,
        rootNavigatorShow: false,
        visitorNavigatorShow: false,
      }
    },
    methods: {
      changenavigator: function () {
        //默认为访客登录
        let usertype = this.$cookies.get('usertype');
        let title = this.$cookies.get('title');
        //根据usertype加载左侧导航栏
        if (usertype === '1') {
          //诊所
          this.clinicNavigatorShow = true
          this.doctorNavigatorShow = false;
          this.rootNavigatorShow = false;
          this.visitorNavigatorShow = false;
          this.$refs.clinicnavigator.title = title;
        } else if (usertype === '2') {
          //医生
          this.clinicNavigatorShow = false
          this.doctorNavigatorShow = true;
          this.rootNavigatorShow = false;
          this.visitorNavigatorShow = false;
          this.$refs.doctornavigator.title = title;
        } else if (usertype === '3') {
          //管理员
          this.clinicNavigatorShow = false
          this.doctorNavigatorShow = false;
          this.rootNavigatorShow = true;
          this.visitorNavigatorShow = false;
          this.$refs.rootnavigator.title = title;
        } else {
          //访客
          this.clinicNavigatorShow = false
          this.doctorNavigatorShow = false;
          this.rootNavigatorShow = false;
          this.visitorNavigatorShow = true;
        }
      }
    },
    created() {
      this.$router.push({path: '/default'});
    }, updated() {
      this.changenavigator();
    }
    , mounted() {
      this.changenavigator();
    }

  }
</script>

<style scoped>
  #mainwindow {
    height: 95vh;
    width: 90vw;
    margin: auto;
    background-color: #409EFF;
  }

  #navigatordiv {
    height: 84vh;
  }

  #routerdiv {
    height: 84vh;
  }
</style>
