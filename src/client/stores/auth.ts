import type {
  JWTToken,
  ObtainTokenRequest,
  User,
  UserCreateRequest
} from '@/models/auth'

import { useLocalStorage } from '@vueuse/core'
import jwtDecode from 'jwt-decode'
import { defineStore } from 'pinia'

import authService from '@/services/auth.service'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: useLocalStorage<JWTToken | null>('auth/token', null),
    user: useLocalStorage<User | null>('auth/user', null, {
      serializer: {
        read: (v: any) => (v ? JSON.parse(v) : null),
        write: (v: any) => JSON.stringify(v)
      }
    })
  }),
  getters: {
    isAuth: (state) => state.token !== null
  },
  actions: {
    async login(loginData: ObtainTokenRequest) {
      try {
        const { data } = await authService.token(loginData)
        this.token = data.access
        this.user = jwtDecode(this.token)
        return this.router.push({ name: 'home' })
      } catch (error) {
        console.error(error)
      }
    },
    logout() {
      this.token = null
      this.user = null
    },
    async verify() {
      try {
        await authService.verify({ token: this.token! })
      } catch (error) {
        console.error(error)
        this.logout()
      }
    },
    async register(registrationData: UserCreateRequest) {
      try {
        await authService.userCreate(registrationData)
        return this.router.push({ name: 'login' })
      } catch (error) {
        console.error(error)
      }
    }
  }
})
