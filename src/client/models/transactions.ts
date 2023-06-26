import type { STData } from '@/types/st'
export interface PaymentCategory {
  readonly id: number
  name: string
}
export interface Payment extends STData {
  readonly id: number
  category: PaymentCategory
}
