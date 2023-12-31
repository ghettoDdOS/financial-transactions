import { fileURLToPath, URL } from 'node:url'

import basicSsl from '@vitejs/plugin-basic-ssl'
import vue from '@vitejs/plugin-vue'
import { AnuComponentResolver } from 'anu-vue'
import UnoCSS from 'unocss/vite'
import Components from 'unplugin-vue-components/vite'

import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
  root: './src/client',
  plugins: [
    vue(),
    UnoCSS(),
    Components({
      dts: './types/components.d.ts',
      resolvers: [AnuComponentResolver()]
    }),
    basicSsl()
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src/client', import.meta.url))
    }
  }
})
