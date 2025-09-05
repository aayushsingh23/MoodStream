
# 🎵 MoodStream

<div align="center">

![MoodStream](https://img.shields.io/badge/MoodStream-AI%20Music%20Recommendation-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/aayushsingh23/MoodStream?style=for-the-badge)

**An AI-powered emotion detection system that curates personalized Spotify playlists based on your current mood**

[🚀 Quick Start](#quick-start) • [🌟 Features](#features) • [🛠️ Installation](#installation) • [📖 Usage](#usage) • [🎯 Demo](#demo) • [🤝 Contributing](#contributing) • [📄 License](#license)

</div>

---

## 🌟 Overview

MoodStream is an intelligent music recommendation platform that combines **computer vision**, **machine learning**, and the **Spotify Web API** to deliver personalized music experiences. Using your webcam, it detects your current emotional state and curates a perfect playlist to match your mood.

### 🎯 What MoodStream Does

- **🎭 Emotion Detection**: Uses computer vision and deep learning to analyze facial expressions
- **🎵 Smart Recommendations**: Curates 10 songs instantly + 50+ songs via email
- **🔗 Spotify Integration**: Direct links to Spotify tracks and discovery playlists
- **📧 Email Delivery**: Beautiful HTML emails with personalized playlist links
- **🎨 Modern UI**: Spotify-inspired black and green theme

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/aayushsingh23/MoodStream.git
cd MoodStream

# 2. Set up environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure Spotify API (see Installation section)
# Create .env file with your Spotify credentials

# 5. Run the application
python app.py

# 6. Open in browser
# Visit http://localhost:5000
```

---

## ✨ Features

### 🎭 **Dual Emotion Detection**
- **Auto-Detect**: Real-time emotion detection using your webcam
- **Manual Selection**: Choose from 7 emotions (Happy, Sad, Angry, Relaxed, Anxious, Surprise, Disgust)

### 🎵 **Smart Music Curation**
- **Multi-dimensional Search**: Combines genres, moods, and descriptors
- **Enhanced Profiles**: 7 detailed emotion profiles with 50+ search terms each
- **Popularity Filtering**: Balances popular hits with hidden gems

### 📧 **Email Integration**
- **Spotify Discovery Links**: One-click access to curated music exploration
- **Beautiful HTML Emails**: Professional Spotify-themed design
- **Song Previews**: Top 5 recommendations with artist information
- **Responsive Design**: Works perfectly on all devices

### 🎨 **Modern Interface**
- **Spotify Theme**: Authentic black and green color scheme
- **Responsive Design**: Mobile-friendly interface
- **Smooth Animations**: Professional hover effects and transitions
- **Intuitive UX**: Clean, user-friendly design

---

## 🛠️ Installation

### Prerequisites

- **Python 3.8+**
- **Webcam** (for emotion detection)
- **Spotify Developer Account**
- **Gmail Account** (for email functionality)

### 1. Clone the Repository

```bash
git clone https://github.com/aayushsingh23/MoodStream.git
cd MoodStream
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Spotify API

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Copy `Client ID` and `Client Secret`

### 5. Set Up Gmail (Optional - for email feature)

1. Create a Gmail account for MoodStream
2. Enable 2-factor authentication
3. Generate an App Password
4. See [EMAIL_SETUP_GUIDE.md](EMAIL_SETUP_GUIDE.md) for detailed instructions

### 6. Configure Environment Variables

Create a `.env` file in the project root:

```env
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret

# Email Configuration (Optional)
EMAIL_ADDRESS=your_moodstream_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### 7. Run the Application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser! 🎉

### 8. Test with Demo Script (Optional)

```bash
python demo.py
```

This will test the core functionality without the web interface.

---

## 📖 Usage

### 🎭 **Emotion Detection**

1. **Auto-Detect Mode**:
   - Click "🎭 Detect My Emotion"
   - Allow camera access
   - Look at the camera for emotion detection
   - Get instant song recommendations

2. **Manual Selection**:
   - Choose from 7 emotion buttons
   - Get curated recommendations immediately

### 🎵 **Music Recommendations**

- **Instant Results**: Get 10 songs displayed immediately
- **Spotify Links**: Click any song to open in Spotify
- **Email Option**: Click "📧 Email Spotify Discovery Link" for extended playlist

### 📧 **Email Playlists**

1. Click the email button next to "Recommended Songs for You"
2. Enter your email address
3. Receive a beautiful email with:
   - Smart Spotify discovery link
   - Top 5 song previews
   - Professional HTML design

---

## 🎯 Demo

### 🖥️ **Web Interface**

```
┌─────────────────────────────────────────┐
│               MoodStream                │
├─────────────────────────────────────────┤
│                                         │
│   ┌─────────────┐  ┌─────────────────┐  │
│   │   Detect    │  │                 │  │
│   │ My Emotion  │  │   Choose Your   │  │
│   │             │  │    Emotion      │  │
│   └─────────────┘  └─────────────────┘  │
│                                         │
│              ──── or ────               │
│                                         │
│   Recommended Songs for You  [Email]    │
│                                         │
│   Song 1 - Artist 1                     │
│   Song 2 - Artist 2                     │
│   Song 3 - Artist 3                     │
│  ...                                    │
│                                         │
└─────────────────────────────────────────┘
```

### 📧 **Email Preview**

```
┌─────────────────────────────────────┐
│         MoodStream Email            │
├─────────────────────────────────────┤
│                                     │
│     Your Happy Playlist             │
│   Generated on Sep 6, 2025          │
│                                     │
│  [ Discover Similar Music]          │
│                                     │
│  Preview of Your Songs:             │
│  1. Song Name - Artist Name         │
│  2. Song Name - Artist Name         │
│  3. Song Name - Artist Name         │
│  + 45 more amazing songs!           │
│                                     │
└─────────────────────────────────────┘
```

---

## 🏗️ Project Structure

```
MoodStream/
├── 📄 app.py                 # Main Flask application
├── 🎭 emotion_detector.py    # Computer vision emotion detection
├── 🎨 static/
│   ├── styles.css           # Spotify-themed CSS
│   └── scripts.js           # Frontend JavaScript
├── 📱 templates/
│   └── index.html           # Main HTML template
├── 🤖 emotion_model.json    # Trained emotion detection model
├── ⚙️ emotion_model.weights.h5
├── 📋 requirements.txt      # Python dependencies
├── 🧪 demo.py               # Demo script for testing
├── 📧 EMAIL_SETUP_GUIDE.md  # Email configuration guide
├── 🤝 CONTRIBUTING.md       # Contribution guidelines
├── 📄 CHANGELOG.md          # Version history
├── ⚖️ LICENSE              # MIT license
├── 🔐 .env                  # Environment variables
└── 📖 README.md            # Project documentation
```

---

## 🎛️ API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application page |
| `/detect-emotion-and-recommend` | POST | Auto-detect emotion and get songs |
| `/select-emotion-and-recommend` | POST | Manual emotion selection |
| `/send-email-playlist` | POST | Send email with playlist link |

---

## 🧠 Emotion Profiles

MoodStream uses sophisticated emotion profiles with multiple dimensions:

| Emotion | Genres | Moods | Example Descriptors |
|---------|--------|-------|-------------------|
| **😊 Happy** | Pop, Dance, Funk | Upbeat, Joyful, Energetic | Bright, Optimistic, Vibrant |
| **😢 Sad** | Ballad, Acoustic, Blues | Melancholy, Emotional | Slow, Gentle, Tender |
| **😠 Angry** | Rock, Metal, Punk | Intense, Powerful | Loud, Heavy, Driving |
| **😌 Relaxed** | Ambient, Chill, Jazz | Calm, Peaceful | Smooth, Flowing, Warm |
| **😯 Surprise** | Experimental, Fusion | Exciting, Dynamic | Unexpected, Creative |
| **😰 Anxious** | Soothing, Calming | Peaceful, Tranquil | Gentle, Reassuring |
| **🤢 Disgust** | Alternative, Indie | Unique, Different | Unconventional, Edgy |

---

## 🔧 Technical Architecture

### 🎭 **Emotion Detection**
- **Framework**: TensorFlow/Keras
- **Model**: Pre-trained facial expression recognition
- **Input**: Webcam feed via OpenCV
- **Output**: 7 emotion classifications

### 🎵 **Music Recommendation**
- **API**: Spotify Web API
- **Search Strategy**: Multi-dimensional keyword matching
- **Algorithms**: Popularity-based filtering + diversity optimization
- **Output**: 10 display songs + 50+ email songs

### 📧 **Email System**
- **SMTP**: Gmail integration
- **Security**: App passwords + TLS encryption
- **Design**: Responsive HTML templates
- **Features**: One-click Spotify discovery links

### 🎨 **Frontend**
- **Framework**: Flask + Jinja2
- **Styling**: Custom CSS (Spotify theme)
- **JavaScript**: jQuery for AJAX interactions
- **Responsive**: Mobile-first design

---

## 🚀 Deployment

### 🌐 **Local Development**
```bash
python app.py
# Access at http://localhost:5000
```

### ☁️ **Production Deployment**

**Recommended Platforms:**
- **Heroku**: Easy Python deployment
- **Vercel**: Serverless Flask applications
- **AWS EC2**: Full control and scalability
- **DigitalOcean**: Simple cloud deployment

**Environment Variables for Production:**
```env
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
EMAIL_ADDRESS=your_email@domain.com
EMAIL_PASSWORD=your_app_password
FLASK_ENV=production
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 **Bug Reports**
- Use GitHub Issues
- Include error logs and screenshots
- Describe steps to reproduce

### ✨ **Feature Requests**
- Open a GitHub Issue
- Describe the feature and use case
- Include mockups if applicable

### 🔧 **Pull Requests**
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### 📝 **Areas for Contribution**
- **New Emotion Models**: Improve detection accuracy
- **Music Sources**: Integrate additional streaming platforms
- **UI/UX**: Enhance user interface design
- **Performance**: Optimize recommendation algorithms
- **Documentation**: Improve guides and examples

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Spotify Web API** for music data access
- **TensorFlow/Keras** for machine learning capabilities
- **OpenCV** for computer vision functionality
- **Flask** for web framework
- **Bootstrap** for responsive design inspiration

---

## 📞 Support

- **📧 Email**: [Support Email](mailto:moodstream.playlists@gmail.com)
- **🐛 Issues**: [GitHub Issues](https://github.com/aayushsingh23/MoodStream/issues)
- **📖 Docs**: [EMAIL_SETUP_GUIDE.md](EMAIL_SETUP_GUIDE.md)
- **🤝 Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **📄 Changelog**: [CHANGELOG.md](CHANGELOG.md)

---

<div align="center">

**Made with ❤️ by [Aayush Singh](https://github.com/aayushsingh23)**

⭐ **Star this repo if you found it helpful!** ⭐

</div>oodStream
It’s a platform that recommends a playlist of 10 songs tailored to your current emotion. It identifies whether you’re feeling sad, angry, anxious, surprised, worried, or happy, and curates a selection of songs to match your mood.
