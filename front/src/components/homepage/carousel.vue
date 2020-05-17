<template>
  <div>
      <el-carousel indicator-position="outside" type="card">
          <el-carousel-item v-for="item in picList" :key="item.key">
                  <el-image
                            :src="item.src"
                            fit="fill"></el-image>
          </el-carousel-item>
      </el-carousel>
  </div>
</template>

<script>
export default {
    name: 'carousel',
    data () {
        return {
            picList: [
                {'key': '1', 'src': require('@/assets/homePage/carousel/1.jpg')},
                {'key': '2', 'src': require('@/assets/homePage/carousel/2.jpg')},
                {'key': '3', 'src': require('@/assets/homePage/carousel/3.jpg')}
            ]
        }
    },
}
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
