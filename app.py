import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import io

st.title("Farm Decision Prediction App")
st.write("Identify farm decisions likely to yield net returns > ₹50,000/ha/season")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("### Preview of Dataset", df.head())

    # Fix column names with extra spaces
    df.columns = df.columns.str.strip()

    # Selecting features and target
    features = [
        'Crop', 'Crop Area (Ha.)', 'Human labour cost per ha',
        'Animal labour cost per ha', 'Machine cost per ha',
        'Irrigation cost per ha', 'N(Kg) per ha', 'P(Kg) per ha',
        'K(Kg) per ha', 'Variety'
    ]
    target = 'Income level'

    df = df.dropna(subset=features + [target])

    # Convert to string and encode categorical variables
    label_encoders = {}
    for col in ['Crop', 'Variety']:
        df[col] = df[col].astype(str)
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    X = df[features]
    y = df[target]

    model_choice = st.selectbox("Choose Model", ["Decision Tree", "Random Forest", "XGBoost"])

    if st.button("Train and Predict"):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        if model_choice == "Decision Tree":
            model = DecisionTreeClassifier(max_depth=5)
        elif model_choice == "Random Forest":
            model = RandomForestClassifier(n_estimators=100, max_depth=5)
        else:
            model = XGBClassifier(n_estimators=100, max_depth=5, use_label_encoder=False, eval_metric='logloss')

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        st.write("### Classification Report")
        st.text(classification_report(y_test, y_pred))

        # Feature importance
        importances = pd.Series(model.feature_importances_, index=features).sort_values(ascending=False)
        st.write("### Feature Importance")
        st.bar_chart(importances)

        # Show decision tree rules if model is Decision Tree
        if model_choice == "Decision Tree":
            tree_rules = export_text(model, feature_names=features)
            st.write("### Decision Tree Rules")
            st.text(tree_rules)

        # Downloadable predictions
        predictions_df = X_test.copy()
        predictions_df['Predicted Income Level'] = y_pred
        csv = predictions_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Predictions as CSV", csv, "predictions.csv", "text/csv")

    st.write("---")
    st.write("### Try Your Own Farm Details")
    user_input = {}
    for col in features:
        if col in ['Crop', 'Variety']:
            user_input[col] = st.text_input(f"Enter {col}")
        else:
            user_input[col] = st.number_input(f"Enter {col}", value=0.0)

    if st.button("Predict My Outcome"):
        user_df = pd.DataFrame([user_input])
        for col in ['Crop', 'Variety']:
            if col in user_df:
                user_df[col] = label_encoders[col].transform([user_df[col].astype(str).values[0]])
        prediction = model.predict(user_df)[0]
        st.success(f"Predicted Income Level: {'> ₹50,000/ha' if prediction == 1 else '<= ₹50,000/ha'}")
