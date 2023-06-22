import type { PluginOptions } from 'anu-vue'
import type { PartialDeep } from 'type-fest'

export default {
  registerComponents: false,
  themes: {
    light: {
      cssVars: {
        'body-bg-c': '252, 22%, 95%',
        'title-c': 'var(--a-primary)',
        'text-emphasis-high-opacity': '1',
        'text-emphasis-medium-opacity': '1',
        'text-emphasis-light-opacity': '1'
      },
      colors: {
        primary: '237, 41%, 40%',
        secondary: '0, 0%, 91%'
      }
    }
  }
} as PartialDeep<PluginOptions>
