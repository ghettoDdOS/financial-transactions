<script setup lang="ts">
import { useTransactionsStore } from '@/stores/transactions'
import { onMounted } from 'vue'

const transactionStore = useTransactionsStore()

onMounted(async () => {
  await transactionStore.fetchPaymentsList()
})
</script>

<template>
  <div flex flex-col h-full>
    <header bg-primary pa-4 text-center text-white font-medium>График</header>
    <div flex-1 container w-full mx-auto pa-5>
      <table w-full>
        <thead>
          <tr font-bold>
            <td>Наименование</td>
            <td>Дата</td>
            <td>По тарифу</td>
            <td>Счет</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="payment in transactionStore.payments" :key="payment.id">
            <td>Вода</td>
            <td>
              {{
                new Date(payment.date!).toLocaleDateString('ru-RU', {
                  day: '2-digit',
                  month: '2-digit',
                  year: '2-digit'
                })
              }}
            </td>
            <td>{{ payment.Sum }}</td>
            <td :style="payment.id % 2 ? 'color:#19B332' : 'color:#EE0606'">
              {{ payment.Sum }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
