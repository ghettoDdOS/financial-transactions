import type { STData } from '@/types/st'
import type { Payment } from '@/models/transactions'

import { defineStore } from 'pinia'

import transactionsServices from '@/services/transactions.services'

export const useTransactionsStore = defineStore('transactions', {
  state: () => ({
    payments: [] as Payment[]
  }),
  actions: {
    async fetchPaymentsList() {
      try {
        const { data } = await transactionsServices.getPaymentsList()
        this.payments = data
      } catch (error) {
        console.error(error)
      }
    },
    async fetchPaymentById(id: number) {
      try {
        const { data } = await transactionsServices.retrievePayment(id)
        return data
      } catch (error) {
        console.error(error)
      }
    },
    async deletePaymentById(id: number) {
      try {
        await transactionsServices.deletePayment(id)
      } catch (error) {
        console.error(error)
      }
    },
    async createPayment(paymentData: STData) {
      try {
        const { data } = await transactionsServices.createPayment(paymentData)
        this.payments.push(data)
      } catch (error) {
        console.error(error)
      }
    }
  }
})
