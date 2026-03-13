# 🎬 IMDB Sentiment Analysis using RNN

A deep learning web application that analyzes movie reviews and predicts whether the sentiment is **Positive** or **Negative** using a **Simple Recurrent Neural Network (RNN)**.  
The model is trained on the **IMDB Movie Review Dataset** and deployed as an interactive web app using **Streamlit**.

---

# 📌 Project Overview

Sentiment analysis is a Natural Language Processing (NLP) task that determines the emotional tone behind text.

This project builds a deep learning model that understands movie reviews and classifies them as **positive or negative**.

Users can input any movie review in the web interface and instantly receive:

- Predicted sentiment
- Confidence score
- Visual result display

---

# 🧠 Model Architecture

The model uses a **Simple Recurrent Neural Network (RNN)** for sequential text processing.

### Architecture

- Embedding Layer  
- Simple RNN Layer  
- Dense Layer  
- Sigmoid Output Layer  

### Model Details

| Component | Description |
|----------|-------------|
| Dataset | IMDB Movie Reviews |
| Task | Binary Sentiment Classification |
| Framework | TensorFlow / Keras |
| Input Length | 500 tokens |
| Output | Positive / Negative |

---

# 🗂 Project Structure

```
imdb-sentiment-analysis-rnn
│
├── main.py
├── simple_rnn_imdb.h5
├── requirements.txt
├── runtime.txt
├── embedding.ipynb
├── simplernn.ipynb
├── prediction.ipynb
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/patelshweta56/imdb-sentiment-analysis-rnn.git
cd imdb-sentiment-analysis-rnn
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Run the Streamlit app

```bash
streamlit run main.py
```

Open the browser

```
http://localhost:8501
```

---

# 🧪 Example Input

Example movie review

```
This movie was absolutely fantastic. The acting was powerful and the story kept me engaged from start to finish.
```

Output

```
Sentiment: Positive
Prediction Score: 0.81
```

---

# 📊 Features

- Interactive Streamlit web interface
- Real-time sentiment prediction
- Deep learning based text classification
- Pre-trained RNN model
- Example review selector
- Confidence score visualization

---

# 🚀 Deployment

The application is deployed using **Streamlit Cloud**.

Deployment Steps:

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Configure Python runtime
4. Deploy the Streamlit application

---

# 🧰 Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Natural Language Processing (NLP)

---

# 📚 Dataset

The model is trained using the **IMDB Movie Review Dataset**, which contains **50,000 movie reviews labeled as positive or negative**.

Dataset Source:

https://ai.stanford.edu/~amaas/data/sentiment/

---

# 👩‍💻 Author

**Shweta Patel**

LinkedIn  
https://www.linkedin.com/in/shwetapatel84/

GitHub  
https://github.com/patelshweta56

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you found this project useful, consider giving it a **star ⭐ on GitHub**.
