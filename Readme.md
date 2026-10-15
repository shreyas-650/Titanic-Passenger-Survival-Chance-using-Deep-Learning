# 🚢 Titanic Passenger Survival Chance Using Deep Learning

## 📌 About the Project

This project predicts the survival chances of Titanic passengers using a Deep Learning model built with TensorFlow and Keras. The application uses Streamlit to provide an interactive interface where users can enter passenger details and receive a survival probability and prediction.

## ✨ Features

- 🖥️ Interactive web interface using Streamlit.
- 👤 Passenger details input, including class, gender, fare, and family information.
- 🔄 Data preprocessing using Label Encoder, One-Hot Encoder, and Standard Scaler.
- 🧠 Survival prediction using a trained neural network.
- 📊 Displays the predicted survival probability and outcome.

## 🛠️ Technologies Used

- 🐍 Python
- 🤖 TensorFlow and Keras
- 🌐 Streamlit
- 🐼 Pandas and NumPy
- 📈 Scikit-learn
- 📉 Matplotlib and TensorBoard

## 📂 Dataset

The project uses the Titanic Huge Dataset containing passenger records.

🔗 **Dataset:** [Titanic Huge Dataset – 1M Passengers (Kaggle)](https://www.kaggle.com/datasets/marcpaulo/titanic-huge-dataset-1m-passengers/data)

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

**1️⃣ Clone the repository**

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

**2️⃣ Create and activate a virtual environment**

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

**3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

**4️⃣ Run the Streamlit application**

```bash
streamlit run app.py
```

## 🔍 How It Works

1. 👤 Users enter passenger details through the Streamlit interface.
2. 🔄 The application encodes categorical features and scales the input data.
3. 🧠 The trained Deep Learning model predicts the survival probability.
4. 📊 The result is classified using a probability threshold of `0.5`.

## 👨‍💻 Author

**Shreyas Singh**

---

⭐ If you find this project interesting, consider giving the repository a star!
