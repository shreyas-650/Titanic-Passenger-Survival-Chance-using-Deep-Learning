# 🚢 Titanic Passenger Survival Chance Using Deep Learning

## 🔴 Live

**[The Titanic Survival Predictor](https://titanic-survival-chance.streamlit.app/)**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://titanic-survival-chance.streamlit.app/)
## 📌 About the Project

This project predicts the survival chances of Titanic passengers using a Deep Learning model built with TensorFlow and Keras. It features an interactive Streamlit web application where users can enter passenger details and receive a survival probability and prediction.

## ✨ Features

- 🖥️ Interactive web interface using Streamlit.
- 👤 Passenger details input, including class, gender, fare, and family information.
- 🔄 Data preprocessing using Label Encoder, One-Hot Encoder, and Standard Scaler.
- 🧠 Survival prediction using a trained neural network.
- 📊 Displays survival probability and predicted outcome.

## 🛠️ Technologies Used

- 🐍 Python
- 🤖 TensorFlow and Keras
- 🌐 Streamlit
- 🐼 Pandas and NumPy
- 📈 Scikit-learn
- 📉 Matplotlib and TensorBoard

## 📂 Dataset

🔗 [Titanic Huge Dataset – 1M Passengers (Kaggle)](https://www.kaggle.com/datasets/marcpaulo/titanic-huge-dataset-1m-passengers/data)

## 📁 Project Structure

```text
Titanic-Project/
├── app.py
├── huge_1M_titanic.csv
├── model.h5
├── label_encoder.pkl
├── one_hot_encoder.pkl
├── standard_scaler.pkl
├── project.ipynb
├── predict.ipynb
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shreyas-650/Titanic-Passenger-Survival-Chance-using-Deep-Learning.git
cd Titanic-Passenger-Survival-Chance-using-Deep-Learning
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

## 🔍 How It Works

1. 👤 Users enter passenger details through the Streamlit interface.
2. 🔄 Categorical features are encoded and input data is scaled.
3. 🧠 The trained Deep Learning model predicts survival probability.
4. 📊 The result is classified using a probability threshold of `0.5`.

## 👨‍💻 Author

**Shreyas Singh**

🔗 [GitHub Profile](https://github.com/shreyas-650)