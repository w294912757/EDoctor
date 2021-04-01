<template>
  <div id="navigator">
    <el-menu
      default-active="1"
      @open=""
      @close=""
      router
    >
      <el-menu-item index="">
        <i class="el-icon-menu"></i>
        <span slot="title">{{title}}</span>
      </el-menu-item>
      <el-submenu index="">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>用户管理</span>
        </template>
        <el-menu-item-group>
          <template slot="title">申请批准</template>
          <el-menu-item index="/clinicapplymenu">诊所</el-menu-item>
          <el-menu-item index="/doctorapplymenu">医生</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="">
          <template slot="title">选项4</template>
          <el-menu-item index="">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="/">
        <i class="el-icon-document"></i>
        <span slot="title">用户管理</span>
      </el-menu-item>
      <el-menu-item @click.native="logout">
        <i class="el-icon-setting"></i>
        <span slot="title">注销</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
  export default {
    name: "Root",
    data() {
      return {
        title: '',
      }
    },
    methods: {
      logout: function () {
        this.$cookies.remove('operatorId');
        this.$cookies.remove('usertype');
        this.$router.go(0);
      }
    }
  }
</script>

<style scoped>
  #navigator {
    margin-top: 50%;
  }
</style>
