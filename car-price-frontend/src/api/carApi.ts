import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_BASE_URL;

const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const carApi = {
  async getBrands(): Promise<string[]> {
    const res = await api.get("/brands");
    return res.data.brands;
  },

  async getModelsByBrand(brand: string): Promise<string[]> {
    const res = await api.get(`/models/${encodeURIComponent(brand)}`);
    return res.data.models;
  },

  async getModelDetails(brand: string, model: string): Promise<any> {
    const res = await api.get(
      `/details/${encodeURIComponent(brand)}/${encodeURIComponent(model)}`
    );
    return res.data;
  },

  async predictPrice(carData: any) {
    const res = await api.post("/predict", carData);
    return res.data;
  },
};
