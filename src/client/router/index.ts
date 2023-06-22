import { createRouter, createWebHistory } from 'vue-router'

import DefaultLayout from '@/layouts/DefaultLayout.vue'
import EmptyLayout from '@/layouts/EmptyLayout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '',
      component: DefaultLayout,
      children: [
        {
          path: '',
          name: 'home',
          component: () => import('@/views/HomeView.vue')
        },
        {
          path: 'charts',
          name: 'charts',
          component: () => import('@/views/ChartsView.vue')
        }
      ]
    },
    {
      path: '',
      component: EmptyLayout,
      children: [
        {
          path: 'login',
          name: 'login',
          component: () => import('@/views/LoginView.vue')
        },
        {
          path: 'registration',
          name: 'registration',
          component: () => import('@/views/RegistrationView.vue')
        }
      ]
    }
  ]
})

export default router
