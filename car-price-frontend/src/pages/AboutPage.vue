<template>
  <main class="about-page">
    <section class="about-hero">
      <div class="container">
        <div class="hero-badge">داستان ما</div>
        <h1>تکنولوژی در خدمت <span>شفافیت بازار خودرو</span></h1>
        <p>
          ما در «ارزش‌سنج»، با بهره‌گیری از هوش مصنوعی و داده‌های لحظه‌ای بازار، 
          تلاش می‌کنیم تا تجربه خرید و فروش خودرو را برای هر ایرانی، ساده، امن و عادلانه کنیم.
        </p>
      </div>
    </section>

    <section class="stats-section">
      <div class="container">
        <div class="stats-grid">
          <div class="stat-item">
            <span class="stat-number">+۱۵۰,۰۰۰</span>
            <span class="stat-label">تخمین قیمت موفق</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">+۴۵</span>
            <span class="stat-label">کارشناس متخصص</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">۹۸٪</span>
            <span class="stat-label">رضایت کاربران</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">۲۴/۷</span>
            <span class="stat-label">پشتیبانی فعال</span>
          </div>
        </div>
      </div>
    </section>

    <section class="mission-section">
      <div class="container">
        <div class="mission-grid">
          <div class="mission-card">
            <div class="m-icon"><Target :size="32" /></div>
            <h2>ماموریت ما</h2>
            <p>ایجاد بستری هوشمند برای حذف واسطه‌های غیرضروری و ارائه قیمت‌های واقعی بر اساس پارامترهای فنی و بدنه خودرو.</p>
          </div>
          <div class="mission-card highlight">
            <div class="m-icon"><Eye :size="32" /></div>
            <h2>چشم‌انداز ما</h2>
            <p>تبدیل شدن به مرجع شماره یک استعلام قیمت و کارشناسی خودرو در خاورمیانه تا سال ۱۴۰۵.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="values-section">
      <div class="container">
        <div class="section-header">
          <h2>چرا به ارزش‌سنج اعتماد کنید؟</h2>
          <div class="divider"></div>
        </div>
        
        <div class="values-grid">
          <div class="value-item">
            <div class="v-icon"><ShieldCheck :size="28" /></div>
            <h3>دقت و امنیت</h3>
            <p>داده‌های ما روزانه از معتبرترین منابع بازار استخراج و پردازش می‌شوند.</p>
          </div>
          <div class="value-item">
            <div class="v-icon"><Zap :size="28" /></div>
            <h3>سرعت بالا</h3>
            <p>تنها با چند کلیک، گزارش کامل قیمت خودروی خود را دریافت کنید.</p>
          </div>
          <div class="value-item">
            <div class="v-icon"><Users :size="28" /></div>
            <h3>تیم متخصص</h3>
            <p>ترکیبی از نخبگان هوش مصنوعی و خبرگان بازار سنتی خودرو.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="about-cta">
      <div class="container">
        <div class="cta-box">
          <h2>همین حالا قیمت خودروی خود را بدانید</h2>
          <p>با سیستم هوشمند ما، هیچ‌کس نمی‌تواند خودروی شما را ارزان بخرد!</p>
          <router-link to="/predict" class="cta-btn">شروع تخمین قیمت</router-link>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { Target, Eye, ShieldCheck, Zap, Users } from 'lucide-vue-next'
</script>

<style scoped lang="scss">
@import '../assets/styles/variables';

.about-page {
  direction: rtl;
  padding-top: 85px;
  background: #fff;
}

.container {
  max-width: 1140px;
  margin: 0 auto;
  padding: 0 20px;
}

.about-hero {
  padding: 80px 0;
  background: radial-gradient(circle at top left, rgba($secondary, 0.05), transparent),
              radial-gradient(circle at bottom right, rgba($primary, 0.05), transparent);
  text-align: center;

  .hero-badge {
    display: inline-block;
    padding: 6px 16px;
    background: rgba($secondary, 0.1);
    color: $secondary;
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 800;
    margin-bottom: 20px;
  }

  h1 {
    font-size: 3rem;
    font-weight: 900;
    color: #1e293b;
    margin-bottom: 20px;
    line-height: 1.3;

    span { color: $secondary; }
  }

  p {
    font-size: 1.15rem;
    color: #64748b;
    max-width: 750px;
    margin: 0 auto;
    line-height: 1.8;
  }
}

.stats-section {
  margin-top: -40px;
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    background: #fff;
    padding: 40px;
    border-radius: 24px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.06);
    text-align: center;
  }

  .stat-item {
    display: flex;
    flex-direction: column;
    gap: 8px;
    border-left: 1px solid #f1f5f9;
    &:last-child { border-left: none; }

    .stat-number { font-size: 2rem; font-weight: 900; color: $secondary; }
    .stat-label { font-size: 0.95rem; color: #64748b; font-weight: 600; }
  }
}

.mission-section {
  padding: 100px 0;
  .mission-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }

  .mission-card {
    padding: 40px;
    border-radius: 24px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    transition: 0.3s;

    &:hover { transform: translateY(-5px); border-color: $secondary; }

    .m-icon {
      width: 60px;
      height: 60px;
      background: #fff;
      color: $secondary;
      border-radius: 16px;
      display: grid;
      place-items: center;
      margin-bottom: 20px;
      box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }

    h2 { font-size: 1.6rem; font-weight: 800; color: #1e293b; margin-bottom: 15px; }
    p { color: #64748b; line-height: 1.8; margin: 0; }

    &.highlight {
      background: #1e293b;
      h2 { color: #fff; }
      p { color: #94a3b8; }
      .m-icon { background: $secondary; color: #fff; }
    }
  }
}

.values-section {
  padding-bottom: 100px;
  .section-header {
    text-align: center;
    margin-bottom: 50px;
    h2 { font-size: 2rem; font-weight: 900; color: #1e293b; }
    .divider { width: 60px; height: 4px; background: $secondary; margin: 15px auto; border-radius: 2px; }
  }

  .values-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
  }

  .value-item {
    text-align: center;
    .v-icon {
      width: 70px;
      height: 70px;
      margin: 0 auto 20px;
      background: rgba($secondary, 0.05);
      color: $secondary;
      border-radius: 50%;
      display: grid;
      place-items: center;
    }
    h3 { font-size: 1.25rem; font-weight: 800; color: #1e293b; margin-bottom: 12px; }
    p { color: #64748b; line-height: 1.7; }
  }
}

.about-cta {
  padding-bottom: 80px;
  .cta-box {
    background: linear-gradient(135deg, $secondary, darken($secondary, 15%));
    border-radius: 30px;
    padding: 60px;
    text-align: center;
    color: #fff;

    h2 { font-size: 2.2rem; font-weight: 900; margin-bottom: 15px; }
    p { font-size: 1.1rem; opacity: 0.9; margin-bottom: 30px; }

    .cta-btn {
      display: inline-block;
      padding: 16px 40px;
      background: #fff;
      color: $secondary;
      border-radius: 14px;
      font-weight: 800;
      text-decoration: none;
      transition: 0.3s;
      &:hover { transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
    }
  }
}

@media (max-width: 992px) {
  .stats-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 20px; }
  .stat-item { border: none !important; }
  .about-hero h1 { font-size: 2.2rem; }
  .mission-grid { grid-template-columns: 1fr !important; }
  .values-grid { grid-template-columns: 1fr !important; }
}
</style>
