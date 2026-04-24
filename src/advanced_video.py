#!/usr/bin/env python3
"""
ADVANCED 30-Second Video with Sound
Creates a multi-scene animated video with generated music!
Run: python advanced_video.py

First install: pip install numpy opencv-python scipy
"""

import cv2
import numpy as np
import math
from pathlib import Path
from scipy.io import wavfile

def generate_music(duration=30, sample_rate=44100, output_path=None):
    """Generate a simple electronic music track"""
    print("🎵 Generating music...")
    
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    # Bass line (low frequency)
    bass_freq = 110  # A2 note
    bass = 0.3 * np.sin(2 * np.pi * bass_freq * t)
    
    # Melody (changes every 2 seconds)
    melody = np.zeros_like(t)
    notes = [220, 247, 262, 294, 330, 349, 392, 440]  # A3 to A4 scale
    
    for i, freq in enumerate(notes):
        start = int(i * len(t) / len(notes))
        end = int((i + 1) * len(t) / len(notes))
        melody[start:end] = 0.2 * np.sin(2 * np.pi * freq * t[start:end])
    
    # Hi-hat (percussion) - short clicks every beat
    hihat = np.zeros_like(t)
    beat_interval = sample_rate // 2  # 2 beats per second
    for i in range(0, len(t), beat_interval):
        if i + 1000 < len(t):
            hihat[i:i+1000] = 0.1 * np.random.randn(1000)
    
    # Mix all tracks
    audio = bass + melody + hihat
    
    # Normalize
    audio = audio / np.max(np.abs(audio))
    audio = (audio * 32767).astype(np.int16)
    
    # Save as WAV
    if output_path is None:
        output_path = Path("temp_audio.wav")

    wavfile.write(str(output_path), sample_rate, audio)
    print("✅ Music generated!")
    return str(output_path)

def ease_in_out(t):
    """Smooth easing function"""
    return t * t * (3 - 2 * t)

def create_scene_1(frame_num, width, height, fps):
    """Scene 1: Particles explosion (0-6 seconds)"""
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    time = frame_num / fps
    
    # Dark blue gradient background
    for y in range(height):
        intensity = int(20 + (y / height) * 30)
        frame[y, :] = (intensity * 2, intensity, intensity // 2)
    
    # Exploding particles
    num_particles = 100
    for i in range(num_particles):
        angle = (i / num_particles) * 2 * math.pi
        speed = 50 + i * 3
        distance = speed * time * ease_in_out(min(time / 3, 1))
        
        x = int(width // 2 + distance * math.cos(angle))
        y = int(height // 2 + distance * math.sin(angle))
        
        if 0 <= x < width and 0 <= y < height:
            size = int(10 - time)
            if size > 0:
                color_val = int(255 * (1 - time / 6))
                cv2.circle(frame, (x, y), size, 
                          (color_val, color_val // 2, 255), -1)
    
    # Title appears
    if time > 1:
        alpha = min(1, (time - 1) / 1)
        text = "ADVANCED"
        font_scale = 3 + math.sin(time * 5) * 0.3
        color = (int(255 * alpha), int(200 * alpha), int(255 * alpha))
        
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, 6)[0]
        text_x = (width - text_size[0]) // 2
        text_y = height // 2
        
        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX,
                   font_scale, color, 6, cv2.LINE_AA)
    
    return frame

def create_scene_2(frame_num, width, height, fps, scene_start):
    """Scene 2: Wave patterns (6-12 seconds)"""
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    time = (frame_num - scene_start) / fps
    
    # Create wave pattern
    for y in range(height):
        for x in range(0, width, 5):
            wave = math.sin(x * 0.02 + time * 3) * 50
            wave += math.sin(y * 0.02 + time * 2) * 50
            
            intensity = int(127 + wave)
            intensity = max(0, min(255, intensity))
            
            frame[y, x:x+5] = (intensity // 3, intensity // 2, intensity)
    
    # Text
    text = "PYTHON POWER"
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 2.5, 5)[0]
    text_x = (width - text_size[0]) // 2
    text_y = height // 2
    
    cv2.putText(frame, text, (text_x + 3, text_y + 3), cv2.FONT_HERSHEY_SIMPLEX,
               2.5, (0, 0, 0), 8, cv2.LINE_AA)
    cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX,
               2.5, (255, 255, 255), 5, cv2.LINE_AA)
    
    return frame

def create_scene_3(frame_num, width, height, fps, scene_start):
    """Scene 3: Rotating 3D-like cube (12-18 seconds)"""
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    time = (frame_num - scene_start) / fps
    
    # Black background with subtle gradient
    for y in range(height):
        intensity = int(10 + (y / height) * 20)
        frame[y, :] = (intensity, intensity, intensity)
    
    # Rotating cube wireframe
    center_x, center_y = width // 2, height // 2
    size = 300
    
    # 3D rotation
    angle = time * 1.5
    
    # Define cube vertices
    vertices = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Back
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # Front
    ]
    
    # Rotate and project
    rotated = []
    for v in vertices:
        # Rotate around Y axis
        x = v[0] * math.cos(angle) - v[2] * math.sin(angle)
        z = v[0] * math.sin(angle) + v[2] * math.cos(angle)
        y = v[1]
        
        # Rotate around X axis
        y2 = y * math.cos(angle * 0.7) - z * math.sin(angle * 0.7)
        z2 = y * math.sin(angle * 0.7) + z * math.cos(angle * 0.7)
        
        # Project to 2D
        scale = 200 / (3 + z2)
        x2d = int(center_x + x * scale)
        y2d = int(center_y + y2 * scale)
        rotated.append((x2d, y2d))
    
    # Draw cube edges
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # Back face
        (4, 5), (5, 6), (6, 7), (7, 4),  # Front face
        (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
    ]
    
    for edge in edges:
        cv2.line(frame, rotated[edge[0]], rotated[edge[1]], 
                (255, 100, 200), 3, cv2.LINE_AA)
    
    # Draw vertices
    for point in rotated:
        cv2.circle(frame, point, 8, (255, 255, 0), -1)
    
    return frame

def create_scene_4(frame_num, width, height, fps, scene_start):
    """Scene 4: Finale with text (18-30 seconds)"""
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    time = (frame_num - scene_start) / fps
    
    # Colorful gradient
    for y in range(height):
        r = int(127 + 127 * math.sin(time + y * 0.01))
        g = int(127 + 127 * math.sin(time + y * 0.01 + 2))
        b = int(127 + 127 * math.sin(time + y * 0.01 + 4))
        frame[y, :] = (b, g, r)
    
    # Multiple text lines
    messages = [
        "CREATED WITH",
        "PYTHON + OPENCV",
        "30 SECONDS",
        "WITH MUSIC!",
        "🚀"
    ]
    
    for i, msg in enumerate(messages):
        y_pos = 200 + i * 150
        
        # Wavy animation
        offset_x = int(50 * math.sin(time * 2 + i))
        
        text_size = cv2.getTextSize(msg, cv2.FONT_HERSHEY_SIMPLEX, 2, 4)[0]
        text_x = (width - text_size[0]) // 2 + offset_x
        
        # Shadow
        cv2.putText(frame, msg, (text_x + 4, y_pos + 4), 
                   cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 6, cv2.LINE_AA)
        # Main text
        cv2.putText(frame, msg, (text_x, y_pos), 
                   cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 4, cv2.LINE_AA)
    
    return frame

def create_advanced_video():
    print("🎬 Creating ADVANCED 30-second video with music!")
    
    # Settings
    width, height = 1080, 1920  # Vertical
    fps = 30
    duration = 30
    total_frames = fps * duration

    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    temp_audio_file = output_dir / "temp_audio.wav"
    temp_video_file = output_dir / "temp_video.mp4"
    final_output_file = output_dir / "advanced_video_with_sound.mp4"
    
    # Generate music first
    audio_file = generate_music(duration, output_path=temp_audio_file)
    
    # Create video
    output_video = str(temp_video_file)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
    
    print(f"📹 Rendering {total_frames} frames with 4 scenes...")
    
    # Scene timings (in frames)
    scene_1_end = fps * 6
    scene_2_end = fps * 12
    scene_3_end = fps * 18
    
    for frame_num in range(total_frames):
        if frame_num < scene_1_end:
            frame = create_scene_1(frame_num, width, height, fps)
        elif frame_num < scene_2_end:
            frame = create_scene_2(frame_num, width, height, fps, scene_1_end)
        elif frame_num < scene_3_end:
            frame = create_scene_3(frame_num, width, height, fps, scene_2_end)
        else:
            frame = create_scene_4(frame_num, width, height, fps, scene_3_end)
        
        out.write(frame)
        
        if (frame_num + 1) % 30 == 0:
            progress = ((frame_num + 1) * 100) // total_frames
            print(f"  Scene {(frame_num // (fps * 6)) + 1}/4 - {progress}% complete")
    
    out.release()
    print("✅ Video rendered!")
    
    # Combine video and audio using ffmpeg
    print("🎵 Adding music to video...")
    import subprocess
    
    final_output = str(final_output_file)
    
    try:
        subprocess.run([
            'ffmpeg', '-y',
            '-i', output_video,
            '-i', audio_file,
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-shortest',
            final_output
        ], check=True, capture_output=True)
        
        print(f"\n🎉 SUCCESS! Advanced video created: {final_output}")
        print(f"📱 Vertical 1080x1920 (TikTok/Instagram ready)")
        print(f"⏱️  30 seconds")
        print(f"🎵 With music!")
        print(f"🎨 4 different animated scenes")
        print(f"\n✨ Features:")
        print(f"   - Particle explosion")
        print(f"   - Wave patterns")
        print(f"   - 3D rotating cube")
        print(f"   - Colorful finale")
        
        # Clean up temp files
        import os
        os.remove(output_video)
        os.remove(audio_file)
        
    except subprocess.CalledProcessError:
        print("⚠️  FFmpeg not found - video created but no audio")
        print(f"📹 Video saved as: {output_video} (no sound)")
        print("💡 Install FFmpeg to add sound: https://ffmpeg.org/download.html")
    except FileNotFoundError:
        print("⚠️  FFmpeg not installed")
        print(f"📹 Video saved as: {output_video} (no sound)")
        print("💡 Install FFmpeg: https://ffmpeg.org/download.html")

if __name__ == "__main__":
    create_advanced_video()
