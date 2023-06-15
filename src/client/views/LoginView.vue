<script setup lang="ts">
import { toTypedSchema } from '@vee-validate/yup'
import { useForm } from 'vee-validate'
import { object, string } from 'yup'

import { messages } from '@/utils/validation'
import { useAuthStore } from '@/stores/auth'

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

const onSubmit = handleSubmit(authStore.login)
</script>

<template>
  <div h-full flex items-center justify-center>
    <form flex flex-col gap-4 @submit="onSubmit" @change="() => validate()">
      <ATypography title="Вход в личный кабинет" />
      <AInput
        v-model="loginData.email"
        :error="errors.email"
        name="email"
        type="email"
        label="Email"
        append-inner-icon="i-bx-at"
        placeholder="example@mail.ru"
      />
      <AInput
        v-model="loginData.password"
        :error="errors.password"
        name="password"
        type="password"
        label="Пароль"
        append-inner-icon="i-bx-lock"
        placeholder="********"
      />
      <ABtn type="submit" :disabled="isSubmitting">Войти</ABtn>
    </form>
  </div>
</template>
