<template>
    <main class="contact-page">
        <section class="hero">
            <div class="hero-overlay"></div>
            <div class="hero-content">
                <h1>
                    با ما در
                    <span>ارتباط</span>
                    باشید
                </h1>
                <p>
                    تیم پشتیبانی ما آماده پاسخگویی به سوالات شما در زمینه تخمین قیمت خودرو، فرآیند کارشناسی و همکاری‌های
                    تجاری است.
                </p>
            </div>
        </section>

        <section class="contact-section">
            <div class="contact-card">
                <div class="contact-form-wrap">
                    <h2>ارسال پیام</h2>

                    <form class="contact-form" @submit.prevent="sendMessage">
                        <div class="form-grid">
                            <div class="field">
                                <label for="name">نام و نام خانوادگی</label>
                                <input
                                    id="name"
                                    v-model="form.name"
                                    type="text"
                                    placeholder="مثلا: علی محمدی"
                                    required
                                />
                            </div>

                            <div class="field">
                                <label for="email">آدرس ایمیل</label>
                                <input
                                    id="email"
                                    v-model="form.email"
                                    type="email"
                                    placeholder="example@mail.com"
                                    required
                                />
                            </div>
                        </div>

                        <div class="field full">
                            <label for="subject">موضوع پیام</label>
                            <select id="subject" v-model="form.subject" required>
                                <option value="" disabled>انتخاب موضوع...</option>
                                <option value="inquiry">استعلام قیمت</option>
                                <option value="support">پشتیبانی</option>
                                <option value="collaboration">همکاری</option>
                                <option value="other">سایر موارد</option>
                            </select>
                        </div>

                        <div class="field full">
                            <label for="message">متن پیام</label>
                            <textarea
                                id="message"
                                v-model="form.message"
                                rows="6"
                                placeholder="پیام خود را اینجا بنویسید..."
                                required
                            ></textarea>
                        </div>

                        <button class="submit-btn" type="submit" :disabled="submitting">
                            {{ submitting ? "در حال ارسال..." : "ارسال پیام" }}
                        </button>
                    </form>

                    <p v-if="responseMessage" class="response-message" :class="responseClass">
                        {{ responseMessage }}
                    </p>
                </div>

                <div class="contact-info">
                    <div class="info-item">
                        <div class="icon-box">
                            <Phone :size="20" />
                        </div>
                        <div class="info-text">
                            <span>شماره تماس</span>
                            <strong>۰۲۱-۸۸۸۸۴۴۴۴</strong>
                        </div>
                    </div>

                    <div class="info-item">
                        <div class="icon-box">
                            <MapPin :size="20" />
                        </div>
                        <div class="info-text">
                            <span>آدرس مرکزی</span>
                            <strong>تهران، جردن، خیابان ولیعصر، برج تجاری سایه</strong>
                        </div>
                    </div>

                    <div class="info-item">
                        <div class="icon-box">
                            <Mail :size="20" />
                        </div>
                        <div class="info-text">
                            <span>پست الکترونیک</span>
                            <strong>support@carval.ir</strong>
                        </div>
                    </div>

                    <div class="map-box">
                        <iframe
                            src="https://www.google.com/maps?q=Tehran%20Jordan%20Sayeh%20Tower&output=embed"
                            width="100%"
                            height="250"
                            style="border: 0"
                            loading="lazy"
                        >
                        </iframe>
                    </div>
                </div>
            </div>
        </section>

        <section class="social-section">
            <div class="social-inner">
                <p>ما را در شبکه‌های اجتماعی دنبال کنید:</p>
                <div class="social-icons">
                    <a href="#" aria-label="LinkedIn"><Linkedin :size="18" /></a>
                    <a href="#" aria-label="Twitter"><Twitter :size="18" /></a>
                    <a href="#" aria-label="Instagram"><Instagram :size="18" /></a>
                </div>
            </div>
        </section>
    </main>
</template>

<script setup lang="ts">
import { reactive, ref } from "vue";
import { Phone, MapPin, Mail, Linkedin, Twitter, Instagram } from "lucide-vue-next";

const form = reactive({
    name: "",
    email: "",
    subject: "",
    message: "",
});

const submitting = ref(false);
const responseMessage = ref("");
const responseClass = ref("");

const sendMessage = async () => {
    submitting.value = true;
    responseMessage.value = "";
    try {
        await new Promise((resolve) => setTimeout(resolve, 1200));
        responseMessage.value = "پیام شما با موفقیت ارسال شد.";
        responseClass.value = "success";
        Object.assign(form, { name: "", email: "", subject: "", message: "" });
    } catch (err) {
        responseMessage.value = "خطا در ارسال پیام.";
        responseClass.value = "error";
    } finally {
        submitting.value = false;
    }
};
</script>

<style scoped lang="scss">
@import "../assets/styles/variables";

.contact-page {
    background: #f4f7fb;
    min-height: 100vh;
    padding-top: 85px;
    direction: rtl;
}

/* Hero */
.hero {
    position: relative;
    min-height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 60px 20px;
    background: #cbd5e1;
    overflow: hidden;
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background: rgba(255, 255, 255, 0.4);
}

.hero-content {
    position: relative;
    z-index: 1;
    max-width: 900px;
    width: 100%;
}

.hero h1 {
    font-size: 2.8rem;
    font-weight: 900;
    color: #1e293b;
    margin-bottom: 15px;

    span {
        color: $secondary;
    }
}

.hero p {
    color: #475569;
    font-size: 1.1rem;
    line-height: 1.8;
    max-width: 700px;
    margin: 0 auto;
}

.contact-section {
    margin-top: -50px;
    padding: 0 20px 60px;
    position: relative;
    z-index: 2;
}

.contact-card {
    max-width: 1100px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 25px;
}

.contact-info,
.contact-form-wrap {
    background: #fff;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08);
}

.contact-info {
    padding: 25px;
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.info-item {
    display: flex;
    align-items: center;
    gap: 15px;
    padding: 15px;
    border: 1px solid #f1f5f9;
    border-radius: 15px;
    background: #fff;
}

.icon-box {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: rgba($secondary, 0.1);
    color: $secondary;
    display: grid;
    place-items: center;
    flex-shrink: 0;
}

.info-text {
    display: flex;
    flex-direction: column;
    span {
        color: #64748b;
        font-size: 0.85rem;
    }
    strong {
        color: #1e293b;
        font-size: 0.95rem;
        font-weight: 800;
        margin-top: 2px;
    }
}

.map-box {
    border-radius: 15px;
    overflow: hidden;
    border: 1px solid #f1f5f9;
    margin-top: 10px;
}

.contact-form-wrap {
    padding: 40px;
    h2 {
        font-size: 1.8rem;
        font-weight: 900;
        color: #1e293b;
        margin-bottom: 25px;
    }
}

.contact-form {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.field {
    display: flex;
    flex-direction: column;
    gap: 8px;
    label {
        font-size: 0.9rem;
        font-weight: 700;
        color: #475569;
    }
    input,
    select,
    textarea {
        padding: 14px;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background: #f8fafc;
        font-family: inherit;
        font-size: 0.95rem;
        &:focus {
            border-color: $secondary;
            background: #fff;
            outline: none;
            box-shadow: 0 0 0 4px rgba($secondary, 0.05);
        }
    }
}

.submit-btn {
    width: 100%;
    padding: 16px;
    border: none;
    border-radius: 12px;
    background: $secondary;
    color: #fff;
    font-weight: 800;
    font-size: 1rem;
    cursor: pointer;
    transition: 0.3s;
    &:hover {
        background: darken($secondary, 8%);
        transform: translateY(-2px);
    }
    &:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }
}

.social-section {
    padding-bottom: 50px;
    text-align: center;
}
.social-inner {
    display: inline-flex;
    align-items: center;
    gap: 15px;
    background: #fff;
    padding: 12px 30px;
    border-radius: 50px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.03);
    p {
        margin: 0;
        font-size: 0.9rem;
        color: #64748b;
    }
}
.social-icons {
    display: flex;
    gap: 12px;
    a {
        color: #94a3b8;
        transition: 0.2s;
        &:hover {
            color: $secondary;
        }
    }
}

@media (max-width: 950px) {
    .contact-card {
        grid-template-columns: 1fr;
    }
    .form-grid {
        grid-template-columns: 1fr;
    }
    .hero h1 {
        font-size: 2rem;
    }
    .contact-form-wrap {
        padding: 25px;
    }
}
</style>
