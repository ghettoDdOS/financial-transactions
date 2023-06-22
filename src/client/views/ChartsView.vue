<script setup lang="ts">
import {
BarElement,
CategoryScale,
Chart as ChartJS,
LinearScale,
Title,
Tooltip
} from 'chart.js'
import _ from 'lodash'
import { Bar } from 'vue-chartjs'

import { useTransactionsStore } from '@/stores/transactions'
import { computed, onMounted } from 'vue'

ChartJS.register(Title, Tooltip, BarElement, CategoryScale, LinearScale)

const transactionStore = useTransactionsStore()

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false
}
const groupedData = computed(() => _.groupBy(transactionStore.payments, 'date'))
const chartData = computed(() => ({
  labels: Object.keys(groupedData.value).map((d) =>
    new Date(d).toLocaleDateString('ru-RU', {
      day: '2-digit',
      month: '2-digit',
      year: '2-digit'
    })
  ),
  datasets: [
    {
      data: Object.values(groupedData.value).map((v) =>
        v.reduce((acc, curr) => {
          if (curr?.Sum) acc += parseInt(curr.Sum)

          return acc
        }, 0)
      )
    }
  ]
}))

onMounted(async () => {
  await transactionStore.fetchPaymentsList()
})
</script>

<template>
  <div flex flex-col h-full>
    <header bg-primary pa-4 text-center text-white font-medium>График</header>
    <div flex-1 container w-full mx-auto pa-5>
      <div class="h-1/2" relative>
        <!-- <ATypography title="" /> -->

        <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
      </div>
    </div>
  </div>
</template>
