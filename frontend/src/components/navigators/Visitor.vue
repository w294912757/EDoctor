<template>
  <div id="navigator">
    <el-menu
      default-active="1"
      @open="handleOpen"
      @close="handleClose"
      router
    >
      <el-menu-item index="/default">
        <i class="el-icon-menu"></i>
        <span slot="title">主页</span>
      </el-menu-item>
      <el-menu-item index="/login">
        <i class="el-icon-menu"></i>
        <span slot="title">登录/注册</span>
      </el-menu-item>
      <el-menu-item index="/clinics">
        <i class="el-icon-document"></i>
        <span slot="title">诊所查询</span>
      </el-menu-item>
      <el-menu-item index="/doctors">
        <i class="el-icon-setting"></i>
        <span slot="title">医生查询</span>
      </el-menu-item>

      <el-submenu index="">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>导航一</span>
        </template>
        <el-menu-item-group>
          <template slot="title">分组一</template>
          <el-menu-item index="">选项1</el-menu-item>
          <el-menu-item index="">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="">
          <template slot="title">选项4</template>
          <el-menu-item index="2-4-1">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
  export default {
    name: "Visitor",
    data() {
      return {}
    },
    methods: {
      handleOpen: function (key, keyPath) {

      },
      handleClose: function (key, keyPath) {

      }
    }
  }
</script>

<style scoped>
  #navigator {
    margin-top: 50%;
  }
</style>
