<template>
  <div h-full flex flex-col>
    <main flex-1>
      <RouterView />
    </main>
    <footer flex shadow>
      <ABtn
        v-for="link in links"
        :key="link.toName"
        :icon="link.icon"
        @click="$router.push({ name: link.toName })"
        w-full
        rounded-0
        variant="text"
        class="footer__button"
        h-auto
        pa-2
      >
        {{ link.label }}
      </ABtn>
    </footer>
  </div>
</template>

<script setup lang="ts">
const links = [
  { toName: 'home', icon: 'i-bx-home', label: 'Главная' },
  { toName: 'charts', icon: 'i-bx-calendar', label: 'График'  },
  { toName: 'statistics', icon: 'i-bx-wallet', label: 'Расчеты'},

]
</script>

<style lang="css">
.footer__button .a-btn-content {
  flex-direction: column;
}
</style>
