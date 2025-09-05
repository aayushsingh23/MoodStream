from flask import Flask, jsonify, request, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from emotion_detector import detect_emotion
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

load_dotenv()
app = Flask(__name__)
    
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Email configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Your MoodStream email
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Your email app password

emotion_dict = {0: "Angry", 1: "Disgust", 2: "Anxious", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Relaxed"}

def get_songs_for_emotion(emotion, full_list=False):
    """
    Enhanced song recommendation system using multi-dimensional search.
    Returns either 10 songs for display or 50+ songs for email.
    """
    # Enhanced emotion profiles with genres, moods, and descriptors
    emotion_profiles = {
        "happy": {
            "genres": ["pop", "dance", "funk", "disco", "electronic", "reggae"],
            "moods": ["upbeat", "joyful", "celebration", "energetic", "festive", "cheerful"],
            "descriptors": ["bright", "optimistic", "vibrant", "bouncy", "lively"],
            "styles": ["party", "wedding", "festival", "dance", "uplifting"]
        },
        "sad": {
            "genres": ["ballad", "acoustic", "folk", "blues", "indie", "classical"],
            "moods": ["melancholy", "heartbreak", "emotional", "lonely", "nostalgic", "reflective"],
            "descriptors": ["slow", "gentle", "soft", "tender", "mellow"],
            "styles": ["romantic", "soulful", "contemplative", "introspective", "emotional"]
        },
        "angry": {
            "genres": ["rock", "metal", "punk", "hard rock", "alternative", "grunge"],
            "moods": ["intense", "powerful", "aggressive", "fierce", "rebellious", "strong"],
            "descriptors": ["loud", "heavy", "driving", "forceful", "explosive"],
            "styles": ["hardcore", "aggressive", "intense", "powerful", "energetic"]
        },
        "relaxed": {
            "genres": ["ambient", "chill", "lounge", "jazz", "new age", "meditation"],
            "moods": ["calm", "peaceful", "soothing", "tranquil", "serene", "zen"],
            "descriptors": ["smooth", "flowing", "gentle", "warm", "cozy"],
            "styles": ["chillout", "ambient", "peaceful", "relaxing", "meditative"]
        },
        "surprise": {
            "genres": ["experimental", "fusion", "world", "electronic", "avant-garde"],
            "moods": ["exciting", "dynamic", "unexpected", "innovative", "creative", "unique"],
            "descriptors": ["eclectic", "diverse", "unconventional", "fresh", "original"],
            "styles": ["experimental", "unique", "creative", "innovative", "surprising"]
        },
        "disgust": {
            "genres": ["alternative", "indie", "grunge", "post-rock", "experimental"],
            "moods": ["dark", "moody", "brooding", "introspective", "mysterious", "edgy"],
            "descriptors": ["atmospheric", "haunting", "complex", "layered", "abstract"],
            "styles": ["alternative", "indie", "dark", "moody", "atmospheric"]
        },
        "anxious": {
            "genres": ["cinematic", "orchestral", "electronic", "ambient", "post-rock"],
            "moods": ["tense", "dramatic", "suspenseful", "nervous", "uncertain", "restless"],
            "descriptors": ["building", "climactic", "escalating", "urgent", "stirring"],
            "styles": ["dramatic", "cinematic", "suspenseful", "intense", "emotional"]
        }
    }
    
    emotion_lower = emotion.lower()
    profile = emotion_profiles.get(emotion_lower, emotion_profiles["happy"])
    
    all_tracks = []
    
    try:
        # Phase 1: Multi-dimensional keyword search
        search_combinations = []
        
        # Create diverse search combinations
        # Genre-based searches
        for genre in profile["genres"][:3]:
            search_combinations.extend([
                f"{genre} bollywood hindi",
                f"{genre} indian music",
                f"{genre} hindi songs"
            ])
        
        # Mood-based searches
        for mood in profile["moods"][:3]:
            search_combinations.extend([
                f"{mood} hindi songs",
                f"{mood} bollywood music",
                f"{mood} indian cinema"
            ])
        
        # Style-based searches
        for style in profile["styles"][:2]:
            search_combinations.extend([
                f"{style} bollywood",
                f"{style} hindi music"
            ])
        
        # Descriptor-based searches
        for descriptor in profile["descriptors"][:2]:
            search_combinations.append(f"{descriptor} indian music")
        
        print(f"Searching with {len(search_combinations)} different combinations for {emotion}")
        
        # Search with diverse terms (limit to prevent too many API calls)
        used_track_ids = set()
        target_tracks = 50 if full_list else 20  # More tracks for email
        
        search_limit = 20 if full_list else 12  # More searches for email
        for search_term in search_combinations[:search_limit]:
            try:
                limit_per_search = 5 if full_list else 3
                results = sp.search(q=search_term, type='track', limit=limit_per_search, market='IN')
                
                for track in results['tracks']['items']:
                    if track['id'] not in used_track_ids:
                        track_info = {
                            'name': track['name'],
                            'url': track['external_urls']['spotify'],
                            'id': track['id'],
                            'artists': [artist['name'] for artist in track['artists']],
                            'popularity': track['popularity'],
                            'search_term': search_term  # Track which search found this
                        }
                        
                        all_tracks.append(track_info)
                        used_track_ids.add(track['id'])
                        
                if len(all_tracks) >= target_tracks:  # Collect enough for variety
                    break
                    
            except Exception as search_error:
                print(f"Search failed for '{search_term}': {search_error}")
                continue
        
        # Phase 2: Popularity-based filtering and ranking
        if all_tracks:
            # Sort by popularity to get more well-known tracks
            all_tracks.sort(key=lambda x: x['popularity'], reverse=True)
            
            # Add some variety by not taking only the most popular
            selected_tracks = []
            
            # Take top popular tracks
            selected_tracks.extend(all_tracks[:6])
            
            # Add some moderately popular tracks for variety
            if len(all_tracks) > 6:
                mid_popular = all_tracks[6:15]
                selected_tracks.extend(mid_popular[:4])
            
            all_tracks = selected_tracks
        
        # Phase 3: Fallback search if not enough matches
        if len(all_tracks) < 8:
            try:
                fallback_queries = [
                    f"{emotion} bollywood songs",
                    f"{emotion} hindi music",
                    "popular bollywood hits",
                    "trending indian songs",
                    "bollywood chartbusters",
                    "hindi film songs popular"
                ]
                
                for query in fallback_queries:
                    if len(all_tracks) >= 10:
                        break
                        
                    results = sp.search(q=query, type='track', limit=5, market='IN')
                    for track in results['tracks']['items']:
                        if track['id'] not in used_track_ids:
                            track_info = {
                                'name': track['name'],
                                'url': track['external_urls']['spotify'],
                                'id': track['id'],
                                'popularity': track['popularity']
                            }
                            
                            all_tracks.append(track_info)
                            used_track_ids.add(track['id'])
                            
                            if len(all_tracks) >= 10:
                                break
                        
            except Exception as fallback_error:
                print(f"Fallback search failed: {fallback_error}")
        
        # Format output - return track name and URL pairs
        if full_list:
            # Return more tracks for email (up to 50)
            final_tracks = []
            for track in all_tracks[:50]:
                final_tracks.append([track['name'], track['url'], ', '.join(track['artists'])])
            print(f"Found {len(final_tracks)} tracks for {emotion} emotion (full list)")
            return final_tracks
        else:
            # Return 10 tracks for display
            final_tracks = []
            for track in all_tracks[:10]:
                final_tracks.append([track['name'], track['url']])
            print(f"Found {len(final_tracks)} tracks for {emotion} emotion")
            return final_tracks
        
    except Exception as e:
        print(f"Spotify search error: {e}")
        # Return default songs if everything fails
        return [
            ["Tum Hi Ho", "https://open.spotify.com/track/example1"],
            ["Kal Ho Naa Ho", "https://open.spotify.com/track/example2"],
            ["Ae Dil Hai Mushkil", "https://open.spotify.com/track/example3"],
            ["Raabta", "https://open.spotify.com/track/example4"],
            ["Gerua", "https://open.spotify.com/track/example5"]
        ]

def create_playlist_url(songs_list, emotion):
    """
    Create a Spotify search URL that provides the best playlist-like experience.
    We'll create a search query that helps users find similar music.
    """
    try:
        # Get the first few artists and song names to create a smart search
        artists = []
        genres = []
        
        for song in songs_list[:10]:  # Use first 10 songs for search terms
            if len(song) > 2:  # If artist info is available
                artist_name = song[2].split(',')[0].strip()  # Get first artist
                if artist_name and artist_name not in artists:
                    artists.append(artist_name)
        
        # Create emotion-based genre mapping
        emotion_genres = {
            "happy": ["pop", "dance", "upbeat", "cheerful"],
            "sad": ["ballad", "melancholy", "acoustic", "emotional"],
            "angry": ["rock", "metal", "intense", "powerful"],
            "relaxed": ["chill", "ambient", "peaceful", "calm"],
            "surprise": ["experimental", "unique", "creative"],
            "anxious": ["soothing", "calming", "peaceful"],
            "disgust": ["alternative", "indie", "unique"]
        }
        
        # Get relevant genres for the emotion
        relevant_genres = emotion_genres.get(emotion.lower(), ["music"])
        
        # Create search query combining emotion, genres, and top artists
        search_terms = [emotion]
        search_terms.extend(relevant_genres[:2])  # Add 2 genre terms
        if artists:
            search_terms.extend(artists[:3])  # Add top 3 artists
        
        # Create the search URL
        search_query = " ".join(search_terms)
        playlist_url = f"https://open.spotify.com/search/{search_query.replace(' ', '%20')}"
        
        # Alternative: Create a genre-based playlist URL
        genre_playlist_url = f"https://open.spotify.com/genre/{relevant_genres[0] if relevant_genres else 'pop'}"
        
        return playlist_url, search_terms
        
    except Exception as e:
        print(f"Error creating playlist URL: {e}")
        return f"https://open.spotify.com/search/{emotion}%20music", []

def send_email_playlist(user_email, emotion, songs_list):
    """
    Send a beautifully formatted email with the full playlist.
    """
    try:
        # Create playlist URL
        playlist_url, track_ids = create_playlist_url(songs_list, emotion)
        
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f"🎵 Your {emotion.title()} Playlist from MoodStream"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = user_email
        
        # Create HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #000000;
                    color: #FFFFFF;
                    margin: 0;
                    padding: 20px;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #121212;
                    border-radius: 15px;
                    padding: 30px;
                }}
                .header {{
                    text-align: center;
                    background: #1DB954;
                    color: #000000;
                    padding: 20px;
                    border-radius: 10px;
                    margin-bottom: 30px;
                }}
                .playlist-button {{
                    background: #1DB954;
                    color: #000000;
                    padding: 20px 40px;
                    border-radius: 25px;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 1.2rem;
                    display: inline-block;
                    margin: 20px 0;
                    transition: all 0.3s ease;
                }}
                .playlist-button:hover {{
                    background: #1ED760;
                    transform: translateY(-2px);
                }}
                .song-preview {{
                    background: #1a1a1a;
                    border: 1px solid #404040;
                    border-radius: 8px;
                    padding: 15px;
                    margin: 10px 0;
                    color: #FFFFFF;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    color: #B3B3B3;
                    font-size: 0.9rem;
                }}
                .spotify-link {{
                    color: #1DB954;
                    text-decoration: none;
                    font-weight: 500;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🎵 MoodStream</h1>
                    <h2>Your {emotion.title()} Playlist</h2>
                    <p>Generated on {datetime.now().strftime("%B %d, %Y at %I:%M %p")}</p>
                </div>
                
                <p>Hello! 👋</p>
                <p>Based on your <strong>{emotion}</strong> mood, we've curated a special collection with <strong>{len(songs_list)}</strong> handpicked songs to match your vibe!</p>
                
                <div style="text-align: center; margin: 30px 0;">
                    <a href="{playlist_url}" class="playlist-button" target="_blank">
                        🎧 Discover Similar Music on Spotify
                    </a>
                </div>
                
                <p style="text-align: center; color: #B3B3B3;">
                    This link will take you to Spotify where you can explore music similar to your curated selection!
                </p>
                
                <h3 style="color: #1DB954; margin-top: 30px;">Preview of Your Songs:</h3>
                <div class="song-previews">"""
        
        # Add first 5 songs as preview
        for i, song in enumerate(songs_list[:5], 1):
            song_name = song[0]
            artist_name = song[2] if len(song) > 2 else "Various Artists"
            
            html_content += f"""
                    <div class="song-preview">
                        <strong>{i}. {song_name}</strong><br>
                        <span style="color: #B3B3B3;">by {artist_name}</span>
                    </div>
            """
        
        if len(songs_list) > 5:
            html_content += f"""
                    <div class="song-preview" style="text-align: center; font-style: italic; color: #B3B3B3;">
                        + {len(songs_list) - 5} more amazing songs waiting for you!
                    </div>
            """
        
        html_content += """
                </div>
                
                <div class="footer">
                    <p>🎧 Click the Spotify button to discover more music like your curated selection!</p>
                    <p>The songs below are your personalized recommendations - use them to search on Spotify for similar tracks! 🌟</p>
                    <p><em>- Team MoodStream</em></p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Create plain text version
        text_content = f"""
        MoodStream - Your {emotion.title()} Playlist
        Generated on {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
        
        Hello!
        
        Based on your {emotion} mood, we've curated a special collection with {len(songs_list)} handpicked songs to match your vibe!
        
        🎧 Discover Similar Music: {playlist_url}
        
        Your Curated Song Recommendations:
        """
        
        for i, song in enumerate(songs_list[:5], 1):
            song_name = song[0]
            artist_name = song[2] if len(song) > 2 else "Various Artists"
            text_content += f"{i}. {song_name} by {artist_name}\n"
        
        if len(songs_list) > 5:
            text_content += f"+ {len(songs_list) - 5} more amazing songs!\n"
        
        text_content += f"""
        
        Click the Spotify link above to discover more music like your curated selection!
        Use these song recommendations to search for similar tracks on Spotify!
        
        - Team MoodStream
        """
        
        # Attach both versions
        text_part = MIMEText(text_content, 'plain')
        html_part = MIMEText(html_content, 'html')
        
        msg.attach(text_part)
        msg.attach(html_part)
        
        # Send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(EMAIL_ADDRESS, user_email, text)
        
        print(f"Email sent successfully to {user_email}")
        return True
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

# @app.route('/detect-emotion-and-recommend', methods=['GET'])
@app.route('/', methods=['GET'])
@app.route('/detect-emotion-and-recommend', methods=['GET','POST'])
def detect_and_recommend():
    """
    Auto-detect emotion using camera and recommend songs.
    """
    if request.method == 'POST':
        try:
            detected_emotion_index = detect_emotion()
            emotion = emotion_dict[detected_emotion_index]
            
            if not emotion:
                return jsonify({"error": "No face detected. Please try again."}), 400

            songs = get_songs_for_emotion(emotion)
            print(f"Auto-detected emotion: {emotion}, found {len(songs)} songs")
            return jsonify({"emotion": emotion, "songs": songs})
            
        except Exception as e:
            print(f"Error in emotion detection: {e}")
            return jsonify({"error": "Failed to detect emotion. Please try again."}), 500
            
    return render_template('index.html')

@app.route('/select-emotion-and-recommend', methods=['POST'])
def select_and_recommend():
    """
    Get recommendations based on manually selected emotion.
    """
    try:
        data = request.get_json()
        
        if not data or 'emotion' not in data:
            return jsonify({"error": "No emotion provided"}), 400
            
        selected_emotion = data['emotion']
        
        # Validate the emotion
        valid_emotions = list(emotion_dict.values())
        if selected_emotion not in valid_emotions:
            return jsonify({"error": "Invalid emotion selected"}), 400
        
        songs = get_songs_for_emotion(selected_emotion)
        print(f"Manual selection: {selected_emotion}, found {len(songs)} songs")
        return jsonify({"emotion": selected_emotion, "songs": songs})
        
    except Exception as e:
        print(f"Error in manual emotion selection: {e}")
        return jsonify({"error": "Failed to get recommendations. Please try again."}), 500

@app.route('/send-email-playlist', methods=['POST'])
def send_email_playlist_route():
    """
    Send the full playlist via email.
    """
    try:
        data = request.get_json()
        
        if not data or 'email' not in data or 'emotion' not in data:
            return jsonify({"error": "Email and emotion are required"}), 400
            
        user_email = data['email']
        emotion = data['emotion']
        
        # Validate email format (basic check)
        if '@' not in user_email or '.' not in user_email:
            return jsonify({"error": "Please enter a valid email address"}), 400
        
        # Get full playlist (50+ songs)
        full_playlist = get_songs_for_emotion(emotion, full_list=True)
        
        if not full_playlist:
            return jsonify({"error": "Could not generate playlist. Please try again."}), 500
        
        # Send email
        email_sent = send_email_playlist(user_email, emotion, full_playlist)
        
        if email_sent:
            return jsonify({
                "success": True, 
                "message": f"Playlist with {len(full_playlist)} songs sent to {user_email}!"
            })
        else:
            return jsonify({"error": "Failed to send email. Please try again."}), 500
            
    except Exception as e:
        print(f"Error in email playlist: {e}")
        return jsonify({"error": "Failed to send email. Please try again."}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)