<script setup lang="ts">
import type { STData } from '@/types/st'

import QrScanner from '@/components/QrScanner.vue'
import { ST } from '@/utils/st'

import { ref } from 'vue'

const stData = ref<STData | null>(null)

const parseSTPayload = (text: string) => {
  try {
    stData.value = ST.parse(text)
  } catch (error) {
    console.error(error)
  }
}
</script>

<template>
  <div>
    <QrScanner @decode="parseSTPayload" />
    <div v-if="stData">
      <div v-for="(value, key) in stData" :key="key">
        <span style="font-weight: 700; margin-end: 15px">{{ key }}</span>
        <span>{{ value }}</span>
      </div>
    </div>
  </div>
</template>
