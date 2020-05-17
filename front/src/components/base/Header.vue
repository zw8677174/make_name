<template>
  <div>
      <el-row style="background-color: rgb(84, 92, 100);">
          <el-col  :span="6">
              <img style="width:50px; margin-left:10px; margin-top:3px" src="@/assets/logo.jpg" />
          </el-col>
          <el-col :span="18">
              <el-menu
                  :default-active="activeIndex2"
                  class="el-menu-demo"
                  mode="horizontal"
                  @select="handleSelect"
                  background-color="#545c64"
                  text-color="#fff"
                  active-text-color="#ffd04b">
                  <el-menu-item index="1">首页</el-menu-item>
                  <el-menu-item index="2">我的</el-menu-item>
                  <el-menu-item index="3">展示</el-menu-item>
                  <el-menu-item index="4">文化</el-menu-item>
              </el-menu>
          </el-col>
      </el-row>
  </div>
</template>

<script>
export default {
    name: 'HomePage',
    data () {
        return {
            msg: '中文名字',
            activeIndex2: '1'
       }
    },

    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        }
    }
}
</script>

<style scoped>
</style>
