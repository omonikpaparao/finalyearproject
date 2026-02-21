# 🚀 HOW TO RUN - Complete Execution Guide

## 📋 Prerequisites

- Python 3.8 or higher installed
- Node.js installed (for server.js)
- Internet connection (for Gemini API)

---

## ⚙️ STEP 1: Install Python Dependencies

Open terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- flask-cors (CORS support)
- pymongo (MongoDB connection)
- textblob (sentiment analysis)
- pandas (data processing)
- nltk (natural language processing)
- google-generativeai (Gemini AI)

---

## 🔑 STEP 2: Gemini API Key Configuration

**API Key:** `AIzaSyBc0Hx7j95RkGJkCJlj3JTW1UE0qUp2tqw`

The API key is already configured in `recommendation_api.py` at line 11:

```python
GEMINI_API_KEY = "AIzaSyBc0Hx7j95RkGJkCJlj3JTW1UE0qUp2tqw"
genai.configure(api_key=GEMINI_API_KEY)
```

**✅ No action needed - API key is already set!**

---

## 🗄️ STEP 3: MongoDB Configuration

The MongoDB connection is already configured in `recommendation_api.py`:

```python
MONGO_URI = "mongodb+srv://v647414:223344vinay@cluster0.lus5rot.mongodb.net/"
```

**✅ No action needed - MongoDB is already configured!**

---

## 🌐 STEP 4: API URL Configuration

The API URL is already set in `recommendation-demo.html` at line 348:

```javascript
const API_URL = 'http://localhost:5001';
```

**✅ No action needed - API URL is already configured!**

---

## 🚀 STEP 5: Start the Recommendation API

Open a terminal and run:

```bash
python recommendation_api.py
```

**Expected Output:**
```
Starting PRUS Recommendation API...
Loaded 95 valid features
 * Serving Flask app 'recommendation_api'
 * Debug mode: on
 * Running on http://0.0.0.0:5001
```

**✅ Keep this terminal open!** The API must be running for recommendations to work.

---

## 🌐 STEP 6: Start the Web Server

Open a **NEW terminal** (keep the API running) and run:

```bash
node server.js
```

**Expected Output:**
```
Server running on http://localhost:3000
```

**✅ Keep this terminal open too!**

---

## 🎯 STEP 7: Access the Application

### Option A: Products Page (Main Entry Point)

1. Open browser: `http://localhost:3000/products`
2. **Login** to your account
3. You'll see the **"🤖 AI-Powered Search"** button
4. Click it to access AI recommendations

### Option B: Direct AI Recommendations

1. Open browser: `http://localhost:3000/recommendation-demo.html`
2. Start using AI search directly

---

## 🌍 STEP 8: Use Multi-Language Support

The recommendation page now supports **4 languages**:

1. **English** - Default
2. **తెలుగు (Telugu)**
3. **தமிழ் (Tamil)**
4. **हिंदी (Hindi)**

**How to use:**
1. Select language from dropdown at top
2. UI updates automatically
3. Type query in any language
4. Get results!

---

## 📝 Example Queries

### English
```
I want a phone with long battery life and good camera
```

### Telugu (తెలుగు)
```
మంచి బ్యాటరీ మరియు కెమెరా ఉన్న ఫోన్ కావాలి
```

### Tamil (தமிழ்)
```
நல்ல பேட்டரி மற்றும் கேமரா கொண்ட தொலைபேசி வேண்டும்
```

### Hindi (हिंदी)
```
अच्छी बैटरी और कैमरा वाला फोन चाहिए
```

---

## 🧪 STEP 9: Test the System

### Test 1: API Health Check

Open browser or use curl:
```bash
curl http://localhost:5001/api/health
```

**Expected Response:**
```json
{
  "success": true,
  "message": "Recommendation API is running",
  "database": "Connected"
}
```

### Test 2: Feature Extraction

Run the test script:
```bash
python test_gemini_features.py
```

**Expected Output:**
```
✓ Loaded 95 valid features
Testing Gemini Feature Extraction
Query: 'I want a phone with long battery life and good screen'
  Gemini response: battery life
✓ Extracted features: ['battery life']
...
```

### Test 3: Complete System Test

```bash
python test_complete_system.py
```

---

## 📂 File Structure & Purpose

### Main Files (DO NOT DELETE)

| File | Purpose |
|------|---------|
| `recommendation_api.py` | Backend API with Gemini integration |
| `recommendation-demo.html` | AI search interface with multi-language |
| `products.html` | Products page with AI button |
| `server.js` | Node.js web server |
| `mobile_features.txt` | Valid features database (95 features) |
| `requirements.txt` | Python dependencies |

### Test Files

| File | Purpose |
|------|---------|
| `test_gemini_features.py` | Test feature extraction |
| `test_complete_system.py` | Test entire system |

### Documentation Files

| File | Purpose |
|------|---------|
| `HOW_TO_RUN.md` | This file - execution guide |
| `GEMINI_INTEGRATION.md` | Technical documentation |
| `QUICKSTART_GEMINI.md` | Quick start guide |
| `VERIFICATION_CHECKLIST.md` | Testing checklist |

---

## 🔧 Troubleshooting

### Problem: "Module not found" error

**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: API not starting

**Solution:**
1. Check if port 5001 is available
2. Try different port in `recommendation_api.py`:
   ```python
   app.run(debug=True, port=5002, host='0.0.0.0')
   ```
3. Update API_URL in `recommendation-demo.html` accordingly

### Problem: "Cannot connect to API" in browser

**Solution:**
1. Make sure `recommendation_api.py` is running
2. Check console for errors
3. Verify API_URL is `http://localhost:5001`

### Problem: No features loaded

**Solution:**
1. Check if `mobile_features.txt` exists in project root
2. File should contain 95 features

### Problem: Gemini API error

**Solution:**
1. Check internet connection
2. Verify API key is correct
3. System has fallback to keyword matching

### Problem: MongoDB connection error

**Solution:**
1. Check internet connection
2. Verify MongoDB URI is correct
3. Check if database has products and comments

### Problem: Language not changing

**Solution:**
1. Clear browser cache
2. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
3. Check browser console for errors

---

## ✅ Success Checklist

- [ ] Python dependencies installed
- [ ] `recommendation_api.py` running on port 5001
- [ ] `server.js` running on port 3000
- [ ] Can access http://localhost:3000/products
- [ ] Can login to account
- [ ] "🤖 AI-Powered Search" button visible
- [ ] Can access recommendation page
- [ ] Language selector works
- [ ] Can enter queries and get results
- [ ] Results show scores and products

---

## 🎉 You're Ready!

If all steps are complete, your AI-powered recommendation system is running!

### Quick Access URLs:

- **Products Page:** http://localhost:3000/products
- **AI Recommendations:** http://localhost:3000/recommendation-demo.html
- **API Health:** http://localhost:5001/api/health

### What You Can Do:

1. ✅ Search products in 4 languages
2. ✅ Get AI-powered recommendations
3. ✅ See sentiment-based scores
4. ✅ Adjust positive/negative weights
5. ✅ Find perfect products based on reviews

---

## 📞 Need Help?

Check these files:
- `GEMINI_INTEGRATION.md` - Technical details
- `VERIFICATION_CHECKLIST.md` - Testing guide
- `QUICK_REFERENCE.txt` - Quick commands

---

**Happy Shopping with AI! 🛍️🤖**
