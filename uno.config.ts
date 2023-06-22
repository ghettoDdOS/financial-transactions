import { presetThemeDefault } from '@anu-vue/preset-theme-default'
import { presetAnu, presetIconExtraProperties } from 'anu-vue'
import { defineConfig, presetAttributify, presetIcons, presetUno } from 'unocss'

export default defineConfig({
  presets: [
    presetUno(),
    presetIcons({
      scale: 1.2,
      extraProperties: presetIconExtraProperties
    }),
    presetAttributify(),
    presetAnu({ colors: ['secondary'] }),
    presetThemeDefault()
  ],
  content: {
    pipeline: { include: [/.*\/anu-vue\.js(.*)?$/, './src/client/**/*.vue'] }
  }
})
