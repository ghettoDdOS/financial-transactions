import type { AInput } from 'anu-vue'
import type { AInputProps } from 'node_modules/anu-vue/dist/types/packages/anu-vue/src/components/input'

import { useEventListener } from '@vueuse/core'
import { computed, onMounted, ref, type Ref } from 'vue'

export const usePasswordInput = (passwordInput: Ref<AInput | undefined>) => {
  const hidePassword = ref(true)

  const passwordInputAttrs = computed<Partial<AInputProps>>(() =>
    hidePassword.value
      ? { appendInnerIcon: 'i-bx-hide', type: 'password' }
      : { appendInnerIcon: 'i-bx-show', type: 'text' }
  )

  onMounted(() => {
    if (!passwordInput.value) return

    const passwordInputWrapper = passwordInput.value?.$el as HTMLDivElement
    const passwordInputIcon = passwordInputWrapper.querySelector(
      '.a-base-input-append-inner-icon'
    )

    useEventListener(
      passwordInputIcon,
      'click',
      () => (hidePassword.value = !hidePassword.value)
    )
  })

  return passwordInputAttrs
}
