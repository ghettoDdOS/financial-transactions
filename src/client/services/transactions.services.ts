import type { Payment, PaymentCategory } from '@/models/transactions'
import type { STData } from '@/types/st'

import { api } from '@/plugins/axios'

export default {
  _endpoint: 'transactions/',

  getPaymentsList() {
    return api.get<Payment[]>(`${this._endpoint}payment/`)
  },
  createPayment(data: STData) {
    return api.post<Payment>(`${this._endpoint}payment/`, data)
  },
  retrievePayment(id: number) {
    return api.get<Payment>(`${this._endpoint}payment/${id}/`)
  },
  deletePayment(id: number) {
    return api.delete(`${this._endpoint}payment/${id}/`)
  },
  getCategoriesList() {
    return api.get<PaymentCategory[]>(`${this._endpoint}category/`)
  }
}
