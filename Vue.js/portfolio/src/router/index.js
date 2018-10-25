import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Portfolio from '@/components/Portfolio'
import Biography from '@/components/Biography'
import Contact from '@/components/Contact'
import Information from '@/components/Information'
 

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Portfolio',
      name: 'Portfolio',
      component: Portfolio
    },
    {
      path: '/Biography',
      name: 'Biography',
      component: Biography
    },
    {
      path: '/Contact',
      name: 'Contact',
      component: Contact
    },
    {
      path: '/Information',
      name: 'Information',
      component: Information
    }
  ]
})
