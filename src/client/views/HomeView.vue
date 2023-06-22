<script setup lang="ts">
import QrScanner from '@/components/QrScanner.vue'
import { useTransactionsStore } from '@/stores/transactions'
import type { STData } from '@/types/st'
import { ST } from '@/utils/st'
import { camelize, onMounted, ref } from 'vue'
console.log(camelize('BankName'))

const scanner = ref<typeof QrScanner>()
const transactionsStore = useTransactionsStore()
const selectedTypeLabel = ref()
const selectedType = ref()
const isDialogShown = ref(false)
const currentQRData = ref<STData>()
const operationsTypes = ref([
  {
    name: 'asfsa',
    id: 1
  }
])

const parseSTPayload = (text: string) => {
  try {
    currentQRData.value = ST.parse(text)
  } catch (error) {
    console.error(error)
  }
}
const scanQR = () => {
  isDialogShown.value = true
  scanner.value?.start()
}
const cancelScanQR = () => {
  isDialogShown.value = false
  scanner.value?.stop()
}
const saveQRData = async () => {
  isDialogShown.value = false
  await transactionsStore.createPayment(currentQRData.value!)
  currentQRData.value = undefined
}
onMounted(async () => {
  await transactionsStore.fetchPaymentsList()
})
</script>

<template>
  <div flex flex-col>
    <header bg-primary pa-4 text-center text-white font-medium>
      Главная страница
    </header>
    <div flex-1 container mx-auto pa-5>
      <div grid grid-cols-2 gap-4>
        <ASelect v-model="selectedTypeLabel" placeholder="Тип">
          <template #default="{ handleListItemClick }">
            <AListItem
              v-for="operationType in operationsTypes"
              :key="operationType.id"
              @click="
                () => {
                  handleListItemClick(operationType.name)
                  selectedType = operationType
                }
              "
            >
              <span>{{ operationType.name }}</span>
            </AListItem>
          </template>
        </ASelect>
        <ABtn w-full h-full @click="scanQR">Сканировать QR</ABtn>
      </div>
      <div mt-4>
        <ATypography title="История" />
        <div flex space-y-3>
          <div
            v-for="transaction in transactionsStore.payments"
            :key="transaction.id"
            bg-secondary
            pa-4
            rounded
            flex
            justify-between
            w-full
          >
            <div>{{ transaction.Name }}</div>
            <div flex>
              <div v-if="transaction.date">
                {{
                  new Date(transaction.date).toLocaleDateString('ru-RU', {
                    day: '2-digit',
                    month: '2-digit',
                    year: '2-digit'
                  })
                }}
              </div>
              <div v-if="transaction.Sum" font-medium ms-2>
                {{
                  parseInt(transaction.Sum).toLocaleString('ru-RU', {
                    style: 'currency',
                    currency: 'RUB'
                  })
                }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <ADialog v-model="isDialogShown" title="Сканировать QR">
    <div class="a-card-body">
      <div py-4>
        <QrScanner ref="scanner" @decode="parseSTPayload" />
      </div>
      <div v-if="currentQRData" pa-4>
        <div><strong>Наименование:</strong> {{ currentQRData.Name }}</div>
        <div><strong>Банк:</strong> {{ currentQRData.BankName }}</div>
        <div v-if="currentQRData.PayerAddress">
          <strong>Адрес:</strong> {{ currentQRData.PayerAddress }}
        </div>
        <div v-if="currentQRData.Sum">
          <strong>Сумма:</strong>
          {{
            parseInt(currentQRData.Sum).toLocaleString('ru-RU', {
              style: 'currency',
              currency: 'RUB'
            })
          }}
        </div>
      </div>
      <div space-x-2>
        <ABtn variant="light" class="text-sm" @click="cancelScanQR">
          Отмена
        </ABtn>
        <ABtn variant="light" class="text-sm" @click="saveQRData">
          Сохранить
        </ABtn>
      </div>
    </div>
  </ADialog>
</template>
