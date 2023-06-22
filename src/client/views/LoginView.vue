<script setup lang="ts">
import type { AInput } from 'anu-vue'

import { toTypedSchema } from '@vee-validate/yup'
import { useForm } from 'vee-validate'
import { ref } from 'vue'
import { object, string } from 'yup'

import { usePasswordInput } from '@/composables/password'
import { useAuthStore } from '@/stores/auth'
import { messages } from '@/utils/validation'

const authStore = useAuthStore()

const {
  values: loginData,
  handleSubmit,
  errors,
  isSubmitting,

  validate
} = useForm({
  validationSchema: toTypedSchema(
    object({
      email: string().required(messages.required).email(messages.email),
      password: string().required(messages.required).min(8, messages.min(8))
    })
  )
})

const onSubmit = handleSubmit((values) => authStore.login(values))

const passwordInput = ref<AInput>()
const passwordInputAttrs = usePasswordInput(passwordInput)
</script>

<template>
  <div h-full flex items-center justify-center>
    <form flex flex-col gap-4 @submit="onSubmit" @change="() => validate()">
      <ATypography title="Войти" text-center />
      <AInput
        v-model="loginData.email"
        :error="errors.email"
        name="email"
        type="email"
        placeholder="Email"
      />
      <AInput
        class="input_password"
        v-model="loginData.password"
        :error="errors.password"
        name="password"
        placeholder="Пароль"
        ref="passwordInput"
        v-bind="passwordInputAttrs"
      />
      <ABtn type="submit" :disabled="isSubmitting" mt-4>Войти</ABtn>
    </form>
  </div>
</template>

<style lang="css">
.input_password .a-base-input-append-inner-icon {
  cursor: pointer;
}
</style>
