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
          <el-menu-item index="">选项1</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="/createprescription">
        <i class="el-icon-document"></i>
        <span slot="title">新建病例</span>
      </el-menu-item>
      <el-menu-item index="allprescriptions">
        <i class="el-icon-document"></i>
        <span slot="title">查看病历</span>
      </el-menu-item>
      <el-menu-item index="prescriptionstatistics">
        <i class="el-icon-document"></i>
        <span slot="title">病历统计</span>
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
    name: "Doctor",
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
    }, updated() {
      this.title = this.$cookies.get('title');
    }
  }
</script>

<style scoped>
  #navigator {
    margin-top: 50%;
  }
</style>
