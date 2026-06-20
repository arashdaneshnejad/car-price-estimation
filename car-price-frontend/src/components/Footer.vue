<template>
  <footer class="footer">
    <div class="container">

      <div class="grid">

        <div class="col">
          <h3>ارزش‌سنج خودرو</h3>
          <p>
            سامانه هوشمند تخمین قیمت خودرو با استفاده از داده‌های بازار
            و مدل‌های یادگیری ماشین.
          </p>
        </div>

        <div class="col">
          <h4>دسترسی سریع</h4>
          <ul>
            <li>صفحه اصلی</li>
            <li>تخمین قیمت</li>
            <li>درباره ما</li>
            <li>تماس با ما</li>
          </ul>
        </div>

        <div class="col">
          <h4>تماس با ما</h4>

          <div class="contact">
            <Phone :size="16"/>
            <span>021-88884444</span>
          </div>

          <div class="contact">
            <Mail :size="16"/>
            <span>info@carvalue.ir</span>
          </div>

        </div>

      </div>

      <div class="bottom">
        © ۱۴۰۴ تمامی حقوق محفوظ است
      </div>

    </div>
  </footer>
</template>

<script setup lang="ts">
import { Phone, Mail } from 'lucide-vue-next'
</script>

<style scoped lang="scss">
@import '../assets/styles/variables';

.footer {
  margin-top: 80px;
  background: #f8fafc;
  border-top: 1px solid #e2e8f0;
}

.container {
  max-width: 1200px;
  margin: auto;
  padding: 50px 20px 20px;
}

.grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 40px;
}

.col {

  h3 {
    margin-bottom: 15px;
    color: $primary;
  }

  h4 {
    margin-bottom: 15px;
    color: $primary;
  }

  p {
    font-size: 14px;
    color: #718096;
    line-height: 1.8;
  }

  ul {
    display: flex;
    flex-direction: column;
    gap: 10px;

    li {
      font-size: 14px;
      cursor: pointer;

      &:hover {
        color: $secondary;
      }
    }
  }
}

.contact {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;

  font-size: 14px;
}

.bottom {
  margin-top: 40px;
  padding-top: 20px;

  border-top: 1px solid #e2e8f0;

  text-align: center;
  font-size: 13px;
  color: #a0aec0;
}

@media (max-width: 768px) {

  .grid {
    grid-template-columns: 1fr;
    text-align: center;
  }

  .contact {
    justify-content: center;
  }

}
</style>
