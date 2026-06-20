<template>
  <header class="header">
    <div class="container">
      
      <div class="logo-wrap">
        <div class="logo">ارزش‌سنج خودرو</div>
      </div>

      <div class="nav-wrap">
        <nav class="nav desktop">
          <router-link to="/" class="nav-link">صفحه اصلی</router-link>
          <router-link to="/predict" class="nav-link">تخمین قیمت</router-link>
          <router-link to="/about" class="nav-link">درباره ما</router-link>
          <router-link to="/contact" class="nav-link">تماس با ما</router-link>
        </nav>

        <button class="menu-btn mobile" @click="toggleMenu" aria-label="باز کردن منو">
          <Menu :size="28" />
        </button>
      </div>

    </div>

    <div class="overlay" :class="{ open: menuOpen }" @click="toggleMenu"></div>

    <aside class="drawer" :class="{ open: menuOpen }">
      <nav class="drawer-nav">
        <router-link to="/" @click="toggleMenu">صفحه اصلی</router-link>
        <router-link to="/predict" @click="toggleMenu">تخمین قیمت</router-link>
        <router-link to="/about" @click="toggleMenu">درباره ما</router-link>
        <router-link to="/contact" @click="toggleMenu">تماس با ما</router-link>
      </nav>
    </aside>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Menu } from 'lucide-vue-next'

const menuOpen = ref(false)
const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}
</script>

<style scoped lang="scss">
@import '../assets/styles/variables';

.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(255,255,255,0.98);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0,0,0,0.06);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  height: 72px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  direction: ltr;
}

.logo-wrap {
  flex: 0 0 auto;
}

.logo {
  font-size: 20px;
  font-weight: 900;
  color: $primary;
  white-space: nowrap;
  direction: rtl;
}

.nav-wrap {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 12px;
  flex: 1;
}

.nav {
  display: flex;
  align-items: center;
  gap: 30px;
}

.nav-link {
  font-size: 14px;
  color: $text-main;
  text-decoration: none;
  font-weight: 500;
  transition: 0.2s;
  padding: 8px 0;
  position: relative;
  direction: rtl;

  &:hover {
    color: $secondary;
  }

  &.router-link-active {
    color: $secondary;
    font-weight: 700;
  }

  &.router-link-active::after {
    content: '';
    position: absolute;
    right: 0;
    bottom: -4px;
    width: 100%;
    height: 2px;
    background: $secondary;
    border-radius: 999px;
  }
}

.menu-btn {
  display: none;
  border: none;
  background: transparent;
  cursor: pointer;
  color: $text-main;
  padding: 8px;
  border-radius: 10px;

  &:hover {
    background: #f3f4f6;
  }
}

.overlay {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.35);
  opacity: 0;
  visibility: hidden;
  transition: 0.25s ease;
  z-index: 1001;

  &.open {
    opacity: 1;
    visibility: visible;
  }
}

.drawer {
  position: fixed;
  top: 0;
  right: -280px;
  width: 280px;
  height: 100vh;
  background: #fff;
  z-index: 1002;
  box-shadow: -18px 0 40px rgba(15, 23, 42, 0.12);
  transition: right 0.28s ease;
  padding: 88px 18px 20px;
  direction: rtl;

  &.open {
    right: 0;
  }
}

.drawer-nav {
  display: flex;
  flex-direction: column;
  gap: 10px;

  a {
    text-decoration: none;
    color: $text-main;
    font-weight: 600;
    padding: 14px 12px;
    border-radius: 12px;
    background: #f8fafc;
    transition: 0.2s;

    &:hover,
    &.router-link-active {
      background: rgba($secondary, 0.08);
      color: $secondary;
    }
  }
}

.desktop {
  display: flex;
}

.mobile {
  display: none;
}

@media (max-width: 1024px) {
  .header {
    position: fixed;
  }

  .container {
    height: 66px;
    padding: 0 14px;
  }

  .desktop {
    display: none;
  }

  .mobile {
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }

  .logo {
    font-size: 18px;
  }
}
</style>
