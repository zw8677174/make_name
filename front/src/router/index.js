import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/homepage/HomePage.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'homepage',
      component: HomePage
    }
  ]
})
