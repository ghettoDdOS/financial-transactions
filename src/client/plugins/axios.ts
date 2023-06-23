import type { App } from 'vue'

import { useAuthStore } from '@/stores/auth'
import axios from 'axios'

export const api = axios.create({ baseURL: '/api/' })

api.interceptors.request.use((config) => {
  const authStore = useAuthStore()
  if (authStore.isAuth)
    config.headers.Authorization = `Bearer ${authStore.token}`

  return config
})

export default {
  install(app: App) {
    app.config.globalProperties.$axios = axios
    app.config.globalProperties.$api = api
  }
}
