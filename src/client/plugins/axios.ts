import type { App } from 'vue'

import axios from 'axios'

export const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default {
  install(app: App) {
    app.config.globalProperties.$axios = axios
    app.config.globalProperties.$api = api
  }
}
