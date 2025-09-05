#!/usr/bin/env python3
"""
MoodStream Demo Script

This script demonstrates the core functionality of MoodStream
without requiring the full web interface.

Usage: python demo.py
"""

import os
import sys
from dotenv import load_dotenv

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app import get_songs_for_emotion, emotion_dict
    print("✅ MoodStream modules loaded successfully!")
except ImportError as e:
    print(f"❌ Error importing MoodStream modules: {e}")
    print("📝 Make sure you've installed all requirements: pip install -r requirements.txt")
    sys.exit(1)

def demo_emotion_recommendations():
    """Demo the emotion-based music recommendation system."""
    print("\n🎵 MoodStream Demo - Music Recommendation System")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Check if Spotify credentials are configured
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    
    if not client_id or not client_secret:
        print("❌ Spotify credentials not found!")
        print("📝 Please add CLIENT_ID and CLIENT_SECRET to your .env file")
        print("📖 See README.md for setup instructions")
        return
    
    print("✅ Spotify credentials found!")
    print("\n🎭 Available Emotions:")
    
    # Display available emotions
    emotions = list(emotion_dict.values())
    for i, emotion in enumerate(emotions, 1):
        print(f"  {i}. {emotion}")
    
    print("\n🎯 Testing recommendation system...")
    
    # Test each emotion
    for emotion in ["Happy", "Sad", "Relaxed"]:
        print(f"\n🎵 Testing {emotion} emotion:")
        print("-" * 30)
        
        try:
            # Get song recommendations
            songs = get_songs_for_emotion(emotion)
            
            if songs:
                print(f"✅ Found {len(songs)} songs for {emotion} mood:")
                for i, song in enumerate(songs[:5], 1):  # Show first 5
                    song_name = song[0]
                    print(f"  {i}. {song_name}")
                
                if len(songs) > 5:
                    print(f"  ... and {len(songs) - 5} more!")
            else:
                print(f"❌ No songs found for {emotion} emotion")
                
        except Exception as e:
            print(f"❌ Error getting recommendations for {emotion}: {e}")
    
    print("\n🎉 Demo completed!")
    print("\n🚀 To use the full web interface:")
    print("   1. Run: python app.py")
    print("   2. Open: http://localhost:5000")
    print("   3. Enjoy your personalized music experience!")

def check_dependencies():
    """Check if all required dependencies are installed."""
    print("🔍 Checking dependencies...")
    
    dependencies = [
        ("flask", "Flask web framework"),
        ("spotipy", "Spotify Web API"),
        ("numpy", "Numerical computing"),
        ("cv2", "OpenCV computer vision"),
        ("tensorflow", "Machine learning"),
        ("dotenv", "Environment variables")
    ]
    
    missing_deps = []
    
    for dep_name, description in dependencies:
        try:
            if dep_name == "cv2":
                import cv2
            elif dep_name == "dotenv":
                from dotenv import load_dotenv
            else:
                __import__(dep_name)
            print(f"  ✅ {dep_name} - {description}")
        except ImportError:
            print(f"  ❌ {dep_name} - {description} (MISSING)")
            missing_deps.append(dep_name)
    
    if missing_deps:
        print(f"\n❌ Missing dependencies: {', '.join(missing_deps)}")
        print("📝 Install them with: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All dependencies are installed!")
        return True

def main():
    """Main demo function."""
    print("🎵 Welcome to MoodStream Demo!")
    print("🤖 AI-powered emotion detection and music recommendation")
    print("=" * 60)
    
    # Check dependencies first
    if not check_dependencies():
        return
    
    # Run recommendation demo
    demo_emotion_recommendations()
    
    print("\n📚 Additional Resources:")
    print("  📖 README.md - Complete setup guide")
    print("  📧 EMAIL_SETUP_GUIDE.md - Email configuration")
    print("  🤝 CONTRIBUTING.md - How to contribute")
    print("  📄 CHANGELOG.md - Version history")
    print("\n💫 Thank you for trying MoodStream!")

if __name__ == "__main__":
    main()
