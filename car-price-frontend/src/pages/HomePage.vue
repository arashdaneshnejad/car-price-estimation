<template>
    <main class="home-page">
        <section class="hero">
            <div class="container hero-grid">
                <div class="hero-content">
                    <h1>دقیق‌ترین سامانه هوشمند <span>تخمین قیمت خودرو</span> در ایران</h1>
                    <p>
                        با استفاده از الگوریتم‌های پیشرفته یادگیری ماشین و تحلیل داده‌های لحظه‌ای بازار، قیمت واقعی
                        خودروی خود را در کمتر از ۱ دقیقه محاسبه کنید.
                    </p>

                    <div class="hero-actions">
                        <router-link to="/estimate" class="btn-primary">شروع تخمین قیمت</router-link>
                        <router-link to="/reports" class="btn-outline">مشاهده گزارش بازار</router-link>
                    </div>

                    <div class="hero-trust">
                        <div class="trust-icons">
                            <CheckCircle :size="18" />
                            <span>بیش از ۱۰ هزار تخمین موفق</span>
                        </div>
                    </div>
                </div>
                <!-- hoy arash inja aks dodrost bezar-->
                <div class="hero-image">
                    <img
                        src="https://images.unsplash.com/photo-1503376780353-7e6692767b70?q=80&w=2000&auto=format&fit=crop"
                        alt="Car Price Estimation"
                    />
                </div>
            </div>
        </section>

        <section class="features-section">
            <div class="container">
                <div class="section-title">
                    <h2>چرا ارزش‌سنج را انتخاب کنیم؟</h2>
                    <p>تلفیق تکنولوژی و تخصص برای ارائه معتبرترین قیمت بازار</p>
                </div>

                <div class="features-grid">
                    <div class="feature-card">
                        <div class="f-icon"><ShieldCheck :size="32" /></div>
                        <h3>دقت بالا</h3>
                        <p>
                            محاسبات ما با خطای کمتر از ۳ درصد، بر اساس متغیرهای فنی خودرو از جمله رنگ‌شدگی، کارکرد و
                            وضعیت موتور انجام می‌شود.
                        </p>
                    </div>

                    <div class="feature-card">
                        <div class="f-icon"><RefreshCw :size="32" /></div>
                        <h3>بروزرسانی لحظه‌ای</h3>
                        <p>
                            قیمت‌ها به صورت هوشمند و هر ۵ دقیقه یکبار بر اساس آخرین معاملات ثبت شده در نمایشگاه‌ها و
                            پلتفرم‌های آنلاین آپدیت می‌شوند.
                        </p>
                    </div>

                    <div class="feature-card">
                        <div class="f-icon"><Zap :size="32" /></div>
                        <h3>رایگان بودن</h3>
                        <p>
                            تمامی فرآیندهای استعلام و تخمین قیمت در ارزش‌سنج برای کاربران عادی کاملاً رایگان است و هیچ
                            هزینه‌ای در بر نخواهد داشت.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <section class="stats-bar">
            <div class="container stats-grid">
                <div class="stat-item">
                    <strong>+۱م</strong>
                    <span>کاربر ماهانه</span>
                </div>
                <div class="stat-item">
                    <strong>۸۵٪</strong>
                    <span>دقت معاملات نهایی</span>
                </div>
                <div class="stat-item">
                    <strong>۲۴/۷</strong>
                    <span>پشتیبانی و تحلیل</span>
                </div>
                <div class="stat-item">
                    <strong>+۱۵۰</strong>
                    <span>مدل خودروی فعال</span>
                </div>
            </div>
        </section>

        <section class="ready-cta">
            <div class="container">
                <div class="cta-card">
                    <h2>آماده‌اید قیمت واقعی خودروی خود را بدانید؟</h2>
                    <p>همین حالا فرآیند تخمین قیمت را شروع کنید و از ضرر در معاملات جلوگیری کنید.</p>
                    <router-link to="/predict" class="btn-white">شروع تخمین قیمت</router-link>
                </div>
            </div>
        </section>
    </main>
</template>

<script setup lang="ts">
import { CheckCircle, ShieldCheck, RefreshCw, Zap } from "lucide-vue-next";
</script>

<style scoped lang="scss">
@import "../assets/styles/variables";

.home-page {
    direction: rtl;
    padding-top: 85px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
}

/* Hero Section */
.hero {
    padding: 80px 0 140px;
    background: #f8fafc;
    position: relative;
    overflow: hidden;

    .hero-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        align-items: center;
        gap: 40px;
    }

    h1 {
        font-size: 3.2rem;
        font-weight: 900;
        line-height: 1.2;
        color: #1e293b;
        margin-bottom: 24px;
        span {
            color: $secondary;
        }
    }

    p {
        font-size: 1.15rem;
        color: #64748b;
        line-height: 1.8;
        margin-bottom: 40px;
        max-width: 550px;
    }

    .hero-actions {
        display: flex;
        gap: 16px;
        margin-bottom: 30px;
    }

    .hero-image {
        position: relative;
        z-index: 1;
        img {
            width: 140%;
            height: auto;
            transform: translateX(10%);
            filter: drop-shadow(0 30px 60px rgba(0, 0, 0, 0.12));
        }
    }

    .hero-trust {
        color: #94a3b8;
        font-size: 0.95rem;
        .trust-icons {
            display: flex;
            align-items: center;
            gap: 8px;
        }
    }
}

.features-section {
    padding: 100px 0;
    background: #fff;
    .section-title {
        text-align: center;
        margin-bottom: 60px;
        h2 {
            font-size: 2.2rem;
            font-weight: 900;
            color: #1e293b;
            margin-bottom: 15px;
        }
        p {
            color: #64748b;
            font-size: 1.1rem;
        }
    }
    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
    }
    .feature-card {
        padding: 40px;
        background: #fff;
        border-radius: 24px;
        border: 1px solid #f1f5f9;
        transition: 0.4s;
        text-align: center;
        &:hover {
            transform: translateY(-10px);
            border-color: $secondary;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.05);
        }
        .f-icon {
            width: 70px;
            height: 70px;
            background: rgba($secondary, 0.08);
            color: $secondary;
            border-radius: 20px;
            display: grid;
            place-items: center;
            margin: 0 auto 24px;
        }
        h3 {
            font-size: 1.4rem;
            font-weight: 800;
            color: #1e293b;
            margin-bottom: 16px;
        }
        p {
            color: #64748b;
            line-height: 1.8;
        }
    }
}

.stats-bar {
    background: #1e293b;
    padding: 70px 0;
    color: #fff;
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        text-align: center;
    }
    .stat-item {
        display: flex;
        flex-direction: column;
        gap: 8px;
        strong {
            font-size: 2.4rem;
            font-weight: 900;
            color: #60a5fa;
        }
        span {
            font-size: 1rem;
            opacity: 0.8;
        }
    }
}

.ready-cta {
    padding: 100px 0;
    .cta-card {
        background: linear-gradient(135deg, $secondary, darken($secondary, 15%));
        padding: 70px;
        border-radius: 35px;
        text-align: center;
        color: #fff;
        h2 {
            font-size: 2.3rem;
            font-weight: 900;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 40px;
        }
    }
}

.btn-primary {
    background: $secondary;
    color: #fff;
    padding: 16px 32px;
    border-radius: 14px;
    font-weight: 800;
    text-decoration: none;
    transition: 0.3s;
    &:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px rgba($secondary, 0.3);
    }
}

.btn-outline {
    border: 2px solid $secondary;
    color: $secondary;
    padding: 14px 32px;
    border-radius: 14px;
    font-weight: 800;
    text-decoration: none;
    transition: 0.3s;
    &:hover {
        background: rgba($secondary, 0.05);
    }
}

.btn-white {
    background: #fff;
    color: $secondary;
    padding: 16px 45px;
    border-radius: 14px;
    font-weight: 800;
    text-decoration: none;
    display: inline-block;
    transition: 0.3s;
    &:hover {
        transform: scale(1.05);
    }
}

@media (max-width: 992px) {
    .hero-grid {
        grid-template-columns: 1fr !important;
        text-align: center;
    }
    .hero-image {
        display: none;
    }
    .hero-actions {
        justify-content: center;
    }
    .features-grid {
        grid-template-columns: 1fr !important;
    }
    .stats-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 40px;
    }
}
</style>
