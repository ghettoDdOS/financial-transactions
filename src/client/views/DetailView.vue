<script setup lang="ts">
import type { Payment } from '@/models/transactions'
import transactionsServices from '@/services/transactions.services'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const payment = ref<Payment>()
const route = useRoute()
onMounted(async () => {
  const { data } = await transactionsServices.retrievePayment(
    Number(route.params.id)
  )
  payment.value = data
})
</script>

<template>
  <div flex flex-col h-full>
    <header bg-primary pa-4 text-center text-white font-medium>График</header>
    <div flex-1 container w-full mx-auto pa-5 v-if="payment">
      <div flex flex-col space-y-3>
        <div bg-secondary pa-4 rounded flex justify-between w-full>
          <div>Наименование получателя платежа</div>
          <div>{{ payment.Name }}</div>
        </div>
        <div bg-secondary pa-4 rounded flex justify-between w-full>
          <div>Номер счета получателя платежа</div>
          <div>{{ payment.PersonalAcc }}</div>
        </div>
        <div bg-secondary pa-4 rounded flex justify-between w-full>
          <div>Наименование банка получателя платежа</div>
          <div>{{ payment.BankName }}</div>
        </div>
        <div bg-secondary pa-4 rounded flex justify-between w-full>
          <div>БИК</div>
          <div>{{ payment.BIC }}</div>
        </div>
        <div bg-secondary pa-4 rounded flex justify-between w-full>
          <div>Сумма платежа, в копейках</div>
          <div>{{ payment.Sum }}</div>
        </div>
        <div bg-secondary pa-4 rounded flex justify-between w-full>
          <div>ИНН плательщика</div>
          <div>{{ payment.PayeeINN }}</div>
        </div>
        <div flex space-x-2>
          <ABtn pa-3 w-full h-full style="background: #bf1e1e">Удалить</ABtn>
          <ABtn pa-3 w-full h-full>Редактировать</ABtn>
        </div>
      </div>
    </div>
  </div>
</template>
