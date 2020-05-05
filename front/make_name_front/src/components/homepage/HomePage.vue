<template>
  <div >
      <carousel></carousel>
      <el-row>
          <el-col :span="12" style="background-image:url('@/assets/homepage.jpg')">
              test
          </el-col>
      </el-row>
  </div>
</template>

<script>
import carousel from './carousel.vue' 
export default {
    name: 'HomePage',
    data () {
        return {
            msg: '中文名字',
        }
    },
    components:{
        'carousel': carousel
    }

}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
