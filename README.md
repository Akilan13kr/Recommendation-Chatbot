# 🔍 Company Recommendation Chatbot  

**A smart chatbot that helps job seekers discover companies matching their skills and domain preferences.**  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey) [![Download Model](https://img.shields.io/badge/Download-Pretrained_Model-ff69b4)](https://drive.google.com/drive/folders/1ogFNxOEqEPh5tZSyPQ94HPTyBVoaXxEU?usp=sharing)  

## 🌟 Features  
- **Instant Setup** - Use our pre-trained model or train your own  
- **Smart Recommendations** - "Show me AI companies in Bengaluru"  
- **Company Insights** - Descriptions, locations, services, specializations  

## 🚀 Quick Start  

### ⚡ Option 1: Fast Start (Pre-Trained Model)  
1. Download model files:  
   - [model.h5](https://drive.google.com/file/d/1xvCsVzdLrp3_sHS8wtzjNOtPZkVgm7BG/view?usp=sharing)  
   - [texts.pkl](https://drive.google.com/file/d/1Lts_6OaTZGuEdJmNnySDGmK8Fmedyk0p/view?usp=sharing)  
   - [labels.pkl](https://drive.google.com/file/d/1q4rmDgl_fcuXTcsjcyNAyQ2v6nSHlP_S/view?usp=sharing)
2. Place files in project root  
3. Install requirements:  
   ```bash
   pip install flask nltk keras numpy
   ```
4. Run:  
   ```bash
   python app.py
   ```

### 🛠️ Option 2: Custom Training  
1. Install requirements:  
   ```bash
   pip install -r requirements.txt
   ```
2. Train your model:  
   ```bash
   python training.py
   ```
3. Run the chatbot:  
   ```bash
   python app.py
   ```

## 📂 Project Structure  
```
.
├── app.py                # Main application
├── data.json             # Company database & training data
├── training.py           # Model training script
├── templates/            # Frontend html file
├── model/                # (Optional) Store pre-trained files here
│   ├── model.h5          
│   ├── texts.pkl         
│   └── labels.pkl        
└── static/               # Frontend assets
```

## 💬 Example Queries  
Try these in the chat interface:  
- "Find me Cloud Computing companies"  
- "What services does Infosys offer?"  
- "Show me companies specializing in AI"  

## 🔧 Customization  
To add more companies or modify responses:  
1. Edit `data.json`:  
   ```json
   {
     "companies": [
       {
         "name": "Your Company",
         "location": "City, Country",
         ...
       }
     ]
   }
   ```
2. Retrain the model (optional):  
   ```bash
   python training.py
   ```

