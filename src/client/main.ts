import { anu } from 'anu-vue'
import { createApp } from 'vue'

import '@anu-vue/preset-theme-default/dist/style.css'
import 'anu-vue/dist/style.css'
import 'uno.css'

import App from '@/App.vue'
import anuConfig from '@/anu.config'
import axios from '@/plugins/axios'
import pinia from '@/plugins/pinia'
import router from '@/router'

const app = createApp(App)

app.use(router)
app.use(pinia)
app.use(axios)
app.use(anu, anuConfig)

app.mount('#app')
