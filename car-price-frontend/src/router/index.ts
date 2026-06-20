import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/HomePage.vue'
import ContactPage from '../pages/ContactPage.vue'
import AboutPage from '../pages/AboutPage.vue'
import PredictPage from '../pages/PredictPage.vue'



const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/predict',
      name: 'predict',
      component: PredictPage
    },
    {
      path: '/contact',
      name: 'contanctUs',
      component: ContactPage
    },
    {
      path: '/about',
      name: 'about',
      component: AboutPage
    }
  ]
})

export default router
