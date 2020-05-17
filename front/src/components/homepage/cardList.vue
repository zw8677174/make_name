<template>
  <div>
      <el-row>
          <el-col :span="8" style="padding:30px" v-for="item in picList" :key="item.key">
              <el-card class="box-card" :body-style="{ padding: '0px' }">
                  <img :src="item.src" class="image">
                  <div style="padding: 14px;">
                      <span>{{ item.title  }}</span>
                  </div>
              </el-card>
          </el-col>
      </el-row>
  </div>
</template>

<script>
export default {
    name: 'cardList',
    data () {
        return {
            picList: [
                {'title': '游戏', 'key': '1', 'src': require('@/assets/homePage/cardList/1.jpg')},
                {'title': '商业', 'key': '2', 'src': require('@/assets/homePage/cardList/2.jpg')},
                {'title': '批量', 'key': '3', 'src': require('@/assets/homePage/cardList/3.jpg')}
            ]
        }
    },
}
</script>

<style scoped>
  .image {
    width: 100%;
    display: block;
    height:600px;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
</style>
