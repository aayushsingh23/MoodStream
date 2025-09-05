# 📧 Email Setup Guide for MoodStream

## 🎯 Overview
This guide will help you set up email functionality to send full playlists (50+ songs) to users via email.

## 🚀 Quick Setup Steps

### 1. Create Your MoodStream Email Account
1. Go to [Gmail](https://accounts.google.com/signup) and create a new account
2. Suggested email: `moodstream.playlists@gmail.com` or similar
3. Use a strong password and enable 2-factor authentication

### 2. Generate App Password
1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Navigate to **Security** → **2-Step Verification**
3. Enable 2-Step Verification if not already enabled
4. Go to **App passwords** 
5. Select **Mail** and **Windows Computer** (or Other)
6. Copy the 16-character app password (something like `abcd efgh ijkl mnop`)

### 3. Update Your .env File
```env
CLIENT_ID=e434d22f1e9c4885aad32331c3b8863b
CLIENT_SECRET=3c24870f483542749f60a47a8bdfdbff

# Email Configuration
EMAIL_ADDRESS=your_moodstream_email@gmail.com
EMAIL_PASSWORD=your_16_character_app_password
```

**⚠️ Important:** Use the App Password, NOT your regular Gmail password!

### 4. Test the Functionality
1. Start your Flask app: `python app.py`
2. Open `http://localhost:5000`
3. Detect or select an emotion
4. Click "📧 Email Full Playlist" button
5. Enter your email address to test

## ✨ Features

### What Users Get:
- **Beautiful HTML Email** with Spotify black/green theme
- **Smart Spotify Discovery Link** that opens curated music exploration
- **50+ Song Recommendations** with artist information
- **Preview of Top Songs** (first 5 songs shown in email)
- **Personalized Message** with emotion and timestamp

### Email Content Includes:
- 🎧 **One-Click Spotify Link** - Opens music discovery based on their emotion
- 🎵 **Song Previews** - Top 5-10 recommended songs with artist names
- 🎨 **Professional Spotify-themed design**
- 📅 **Timestamp** of playlist generation
- 💚 **MoodStream branding**

## 🔧 Technical Details

### Email Service: Gmail SMTP
- **Server:** smtp.gmail.com
- **Port:** 587 (TLS)
- **Security:** TLS encryption
- **Daily Limit:** 500 emails/day (Gmail free tier)

### Backup Options (if Gmail hits limits):
1. **SendGrid** - Professional email service ($15/month for 40k emails)
2. **AWS SES** - Pay-per-use ($0.10 per 1000 emails)
3. **Mailgun** - Reliable email API service

## 🎨 Email Design Features
- **Responsive Design** - Works on mobile and desktop
- **Spotify Theme** - Black background with green accents
- **Professional Layout** - Clean, organized song list
- **Interactive Elements** - Hover effects and clickable links

## 🚨 Troubleshooting

### Common Issues:

1. **"Authentication failed"**
   - Make sure you're using the App Password, not regular password
   - Verify 2-factor authentication is enabled

2. **"SMTPAuthenticationError"**
   - Double-check email address and app password in .env
   - Make sure .env file is in the project root

3. **"Connection refused"**
   - Check internet connection
   - Verify Gmail SMTP settings

4. **Emails going to Spam**
   - This is normal for new email addresses
   - Consider upgrading to professional email service for production

### Security Notes:
- ✅ App passwords are safer than regular passwords
- ✅ .env file keeps credentials secure
- ✅ Never commit .env to version control
- ✅ Consider using environment variables in production

## 🎯 Usage Examples

### For Development:
```python
# Test with your own email
user_email = "your.test@gmail.com"
emotion = "happy"
```

### For Production:
- Users enter their email via the web interface
- System validates email format
- Sends personalized playlists automatically

## 🚀 Next Steps
1. Set up your Gmail account and app password
2. Update the .env file with your credentials
3. Test the email functionality
4. Consider upgrading to professional email service for production use

---

**Happy coding! 🎵✨**

*Your MoodStream users will love getting personalized playlists delivered straight to their inbox!*
