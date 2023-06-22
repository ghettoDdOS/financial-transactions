<script setup lang="ts">
import type { AInput } from 'anu-vue'

import { toTypedSchema } from '@vee-validate/yup'
import { useForm } from 'vee-validate'
import { ref } from 'vue'
import { object, string, ref as yupRef } from 'yup'

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
      firstName: string().required(messages.required),
      lastName: string().required(messages.required),
      email: string().required(messages.required).email(messages.email),
      password: string().required(messages.required).min(8, messages.min(8)),
      passwordConfirm: string().when('password', {
        is: (val: string) => val !== '',
        then: (schema) =>
          schema
            .required(messages.required)
            .oneOf([yupRef('password')], 'Пароли не совпадают')
      })
    })
  )
})

const onSubmit = handleSubmit(authStore.register)

const passwordInput = ref<AInput>()
const passwordInputAttrs = usePasswordInput(passwordInput)
</script>

<template>
  <div container mx-auto pa-5>
    <ATypography title="Регистрация" />
    <form
      flex
      flex-col
      gap-2
      mt-5
      @submit="onSubmit"
      @change="() => validate()"
    >
      <AInput
        v-model="loginData.firstName"
        :error="errors.firstName"
        name="firstName"
        placeholder="Имя"
      />
      <AInput
        v-model="loginData.lastName"
        :error="errors.lastName"
        name="lastName"
        placeholder="Фамилия"
      />
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
      <AInput
        class="input_password"
        v-model="loginData.passwordConfirm"
        :error="errors.passwordConfirm"
        name="passwordConfirm"
        placeholder="Подтверждение пароля"
        ref="passwordInput"
        v-bind="passwordInputAttrs"
      />
      <ABtn type="submit" :disabled="isSubmitting" mt-4>
        Зарегистрироваться
      </ABtn>
    </form>
  </div>
</template>

<style lang="css">
.input_password .a-base-input-append-inner-icon {
  cursor: pointer;
}
</style>
