#!/usr/bin/env python3
"""
Simple Animated Video - Try Today!
Creates a 10-second video with animated text and colors
Run: python simple_animation.py
"""

import cv2
import numpy as np
import math
from pathlib import Path

def create_animated_video():
    print("🎬 Creating your animated video...")
    
    # Settings
    width, height = 1080, 1920  # Vertical for TikTok/Instagram
    fps = 30
    duration = 10
    total_frames = fps * duration
    
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "my_first_animation.mp4"
    
    # Video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(output_file), fourcc, fps, (width, height))
    
    print(f"📹 Rendering {total_frames} frames...")
    
    for frame_num in range(total_frames):
        # Create gradient background that changes color
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Animated rainbow gradient
        time = frame_num / fps
        r = int(127 + 127 * math.sin(time * 2))
        g = int(127 + 127 * math.sin(time * 2 + 2))
        b = int(127 + 127 * math.sin(time * 2 + 4))
        
        # Create gradient from top to bottom
        for y in range(height):
            color_factor = y / height
            color = (
                int(b * (1 - color_factor)),
                int(g * (1 - color_factor) * 0.5),
                int(r * color_factor)
            )
            frame[y, :] = color
        
        # Bouncing text animation
        bounce_height = 200 * abs(math.sin(time * 3))
        text_y = int(height // 2 - bounce_height)
        
        # Pulsing size
        scale = 2.5 + 0.5 * math.sin(time * 4)
        
        # Main text
        text = "MY FIRST VIDEO!"
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Get text size
        text_size = cv2.getTextSize(text, font, scale, 5)[0]
        text_x = (width - text_size[0]) // 2
        
        # Draw shadow
        cv2.putText(frame, text, (text_x + 5, text_y + 5), font, scale,
                   (0, 0, 0), 8, cv2.LINE_AA)
        
        # Draw white text
        cv2.putText(frame, text, (text_x, text_y), font, scale,
                   (255, 255, 255), 5, cv2.LINE_AA)
        
        # Subtitle that changes
        messages = [
            "Welcome!",
            "This is Python!",
            "Making Videos!",
            "So Easy!",
            "Let's Go!"
        ]
        
        subtitle_index = int(time * 0.5) % len(messages)
        subtitle = messages[subtitle_index]
        
        sub_size = cv2.getTextSize(subtitle, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 3)[0]
        sub_x = (width - sub_size[0]) // 2
        sub_y = height - 300
        
        cv2.putText(frame, subtitle, (sub_x, sub_y), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3, cv2.LINE_AA)
        
        # Animated circle particles
        num_circles = 5
        for i in range(num_circles):
            angle = (time + i) * 2
            radius = 150 + i * 30
            circle_x = int(width // 2 + radius * math.cos(angle))
            circle_y = int(height // 2 + radius * math.sin(angle))
            circle_size = int(20 + 10 * math.sin(time * 3 + i))
            
            cv2.circle(frame, (circle_x, circle_y), circle_size, 
                      (255, 255, 255), -1)
        
        # Write frame
        out.write(frame)
        
        # Progress
        if (frame_num + 1) % 30 == 0:
            progress = ((frame_num + 1) * 100) // total_frames
            print(f"  {progress}% done...")
    
    out.release()
    
    print(f"\n✅ VIDEO CREATED: {output_file}")
    print(f"📱 Vertical format (perfect for TikTok/Instagram)")
    print(f"⏱️  10 seconds long")
    print(f"🎨 Animated colors and bouncing text!")
    print(f"\nGo check it out! 🚀")

if __name__ == "__main__":
    create_animated_video()
