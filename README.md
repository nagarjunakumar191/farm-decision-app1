# Farm Decision Prediction App 🌾

A Streamlit-based machine learning application to help identify farm decisions that are likely to yield **net returns greater than ₹50,000 per hectare per season**.

---

## 🚀 Features

✅ Upload Excel files with farm data  
✅ Choose between Decision Tree, Random Forest, or XGBoost models  
✅ Automatically preprocesses data (label encoding, missing value handling)  
✅ Displays:
- Classification report
- Feature importance chart
- Decision tree rules (if applicable)

✅ Download prediction results  
✅ Custom prediction form for farmers to try their own inputs  

---

## 🧠 Model Inputs

| Feature                       | Description                         |
|------------------------------|-------------------------------------|
| Crop                         | Type of crop (categorical)          |
| Crop Area (Ha.)              | Cultivated area                     |
| Human labour cost per ha     | Cost of human labour per hectare    |
| Animal labour cost per ha    | Cost of animal labour per hectare   |
| Machine cost per ha          | Cost of machinery per hectare       |
| Irrigation cost per ha       | Irrigation expense per hectare      |
| N(Potassium) per ha          | Nutrient input N (kg/ha)            |
| P(Phosphorus) per ha         | Nutrient input P (kg/ha)            |
| K(Potash) per ha             | Nutrient input K (kg/ha)            |
| Variety                      | Seed type (e.g., Local, Hybrid)     |

**Target Variable**:  
`Income level` = `1` if Net Income > ₹50,000/ha, else `0`

---

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 🌐 Deployed on Streamlit Cloud

Visit the live app: [your-username.streamlit.app](https://your-username.streamlit.app)

---

## 📝 Sample Dataset

Ensure your uploaded `.xlsx` file contains these columns (or similar):
- Crop
- Crop Area (Ha.)
- Human labour cost per ha
- Animal labour cost per ha
- Machine cost per ha
- Irrigation cost per ha
- N(Kg) per ha
- P(Kg) per ha
- K(Kg) per ha
- Variety
- Income level (1 or 0)

---

## 🤝 Contributing

Feel free to fork and extend this app for other crops, income thresholds, or use cases.

---

## 📧 Contact

Created by [Your Name] — [your.email@example.com]
