<template>
    <main class="page">
        <section class="hero">
            <div class="hero-content">
                <h1>تخمین هوشمند قیمت خودرو</h1>
                <p>
                    با استفاده از مدل‌های یادگیری ماشین و داده‌های بازار، قیمت تقریبی خودروی خود را در چند ثانیه محاسبه
                    کنید.
                </p>
            </div>
        </section>

        <section class="predict-section">
            <div class="predict-card">
                <form @submit.prevent="handlePredict" class="car-form">
                    <div class="form-row">
                        <div class="field">
                            <label>برند</label>
                            <select v-model="form.brand" @change="onBrandChange" required>
                                <option value="" disabled>انتخاب برند...</option>
                                <option v-for="b in brands" :key="b" :value="b">{{ b }}</option>
                            </select>
                        </div>

                        <div class="field">
                            <label>مدل</label>
                            <select v-model="form.model" @change="onModelChange" :disabled="!models.length" required>
                                <option value="" disabled>انتخاب مدل...</option>
                                <option v-for="m in models" :key="m" :value="m">{{ m }}</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="field">
                            <label>سال ساخت</label>
                            <input type="number" v-model.number="form.year" />
                        </div>

                        <div class="field">
                            <label>گیربکس</label>
                            <select v-model="form.transmission">
                                <option v-for="t in details.transmissions" :key="t">{{ t }}</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="field">
                            <label>نوع سوخت</label>
                            <select v-model="form.fuelType">
                                <option v-for="f in details.fuelTypes" :key="f">{{ f }}</option>
                            </select>
                        </div>

                        <div class="field">
                            <label>کارکرد (Miles)</label>
                            <input type="number" v-model.number="form.mileage" />
                        </div>
                    </div>

                    <button class="predict-btn" :disabled="loading">
                        {{ loading ? "در حال تحلیل..." : "تخمین قیمت" }}
                    </button>
                </form>

                <transition name="fade">
                    <div v-if="result !== null" class="result">
                        <h3>قیمت تخمینی</h3>
                        <p class="price">£ {{ result.toLocaleString() }}</p>
                    </div>
                </transition>

                <p v-if="error" class="error">{{ error }}</p>
            </div>
        </section>
    </main>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from "vue";
import { carApi } from "../api/carApi";

const brands = ref<string[]>([]);
const models = ref<string[]>([]);
const loading = ref(false);
const result = ref<number | null>(null);
const error = ref("");

const details = reactive({
    transmissions: [] as string[],
    fuelTypes: [] as string[],
});

const form = reactive({
    brand: "",
    model: "",
    year: 2020,
    transmission: "",
    mileage: 0,
    fuelType: "",
    tax: 0,
    mpg: 0,
    engineSize: 0,
});

onMounted(async () => {
    try {
        brands.value = await carApi.getBrands();
    } catch {
        error.value = "خطا در اتصال به سرور";
    }
});

const onBrandChange = async () => {
    form.model = "";
    models.value = await carApi.getModelsByBrand(form.brand);
};

const onModelChange = async () => {
    const data = await carApi.getModelDetails(form.brand, form.model);

    details.transmissions = data.transmissions || [];
    details.fuelTypes = data.fuelTypes || [];

    if (details.transmissions.length) form.transmission = details.transmissions[0];

    if (details.fuelTypes.length) form.fuelType = details.fuelTypes[0];
};

const handlePredict = async () => {
    loading.value = true;
    error.value = "";

    try {
        const data = await carApi.predictPrice(form);
        result.value = data.estimated_price_gbp;
    } catch {
        error.value = "خطا در دریافت قیمت";
    } finally {
        loading.value = false;
    }
};
</script>

<style scoped lang="scss">
@import "../assets/styles/variables";

.page {
    min-height: 100vh;
}

.hero {
    background: linear-gradient(135deg, #1a202c, #2d3748);
    color: white;
    padding: 80px 20px;
    text-align: center;
}

.hero h1 {
    font-size: 2rem;
    margin-bottom: 10px;
}

.hero p {
    opacity: 0.85;
    max-width: 600px;
    margin: auto;
}


.predict-section {
    margin-top: -60px;
    padding: 20px;
    display: flex;
    justify-content: center;
}

.predict-card {
    background: white;
    width: 100%;
    max-width: 700px;
    border-radius: 16px;
    padding: 35px;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.08);
}


.car-form {
    display: flex;
    flex-direction: column;
    gap: 18px;
}

.form-row {
    display: flex;
    gap: 16px;
}

.field {
    flex: 1;
    display: flex;
    flex-direction: column;
}

label {
    font-size: 13px;
    margin-bottom: 6px;
    color: #64748b;
}

input,
select {
    padding: 11px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    font-family: Estedad;
}

.predict-btn {
    margin-top: 10px;
    background: #3182ce;
    color: white;
    border: none;
    padding: 14px;
    border-radius: 10px;
    font-weight: 600;
    cursor: pointer;
}

.predict-btn:hover {
    opacity: 0.9;
}


.result {
    margin-top: 25px;
    padding: 20px;
    border-radius: 12px;
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    text-align: center;
}

.price {
    font-size: 2rem;
    font-weight: 800;
    color: #166534;
}


.error {
    color: #e11d48;
    margin-top: 15px;
    text-align: center;
}


.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.4s;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}


@media (max-width: 768px) {
    .hero {
        padding: 60px 20px;
    }

    .hero h1 {
        font-size: 1.6rem;
    }

    .form-row {
        flex-direction: column;
    }

    .predict-card {
        padding: 25px;
    }
}
</style>
