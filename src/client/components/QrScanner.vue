<script lang="ts" setup>
import QrScanner from 'qr-scanner'

import { onMounted, onUnmounted, ref } from 'vue'

const videoElement = ref<HTMLVideoElement>()
const scanner = ref<QrScanner | null>(null)

const emit = defineEmits<{
  decode: [value: string]
}>()

const onDecode = (result: QrScanner.ScanResult) => {
  emit('decode', result.data)
}
const onDecodeError = (error: Error | string) => {
  console.error(error)
}

onMounted(async () => {
  if (!(await QrScanner.hasCamera())) return

  scanner.value = new QrScanner(videoElement.value!, onDecode, {
    onDecodeError,
    returnDetailedScanResult: true,
    maxScansPerSecond: 10,
    highlightScanRegion: false,
    highlightCodeOutline: true
  })
})

onUnmounted(() => {
  scanner.value?.stop()
})
const start = () => {
  scanner.value?.start()
}
const stop = () => {
  scanner.value?.stop()
}
defineExpose({
  start,
  stop
})
</script>

<template>
  <video style="width: 600px" ref="videoElement"></video>
</template>
