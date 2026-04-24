#!/usr/bin/env python3
"""
Python 10-Second Test Video Generator
Run in terminal: python3 python_video_test.py
"""

from moviepy.editor import TextClip, CompositeVideoClip, ColorClip
from pathlib import Path

def create_test_video():
    print("🎬 Starting Python video generation...")
    
    # Video settings
    duration = 10  # seconds
    width, height = 1920, 1080
    fps = 30
    
    # Create black background
    background = ColorClip(size=(width, height), color=(0, 0, 0), duration=duration)
    
    # Create animated text that changes every 2 seconds
    texts = [
        "Python Video Test",
        "10 Second Demo",
        "Easy to Code!",
        "Fast to Learn",
        "Ready for YouTube!"
    ]
    
    clips = [background]
    
    for i, text in enumerate(texts):
        start_time = i * 2
        
        # Create text clip
        txt_clip = TextClip(
            text,
            fontsize=80,
            color='white',
            font='Arial-Bold',
            size=(width, height),
            method='caption',
            align='center'
        ).set_position('center').set_start(start_time).set_duration(2)
        
        clips.append(txt_clip)
    
    # Composite all clips
    final_video = CompositeVideoClip(clips, size=(width, height))
    
    # Export
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "python_test_video.mp4"
    print(f"📹 Rendering video to {output_file}...")
    
    final_video.write_videofile(
        str(output_file),
        fps=fps,
        codec='libx264',
        audio=False,
        preset='ultrafast'  # Faster rendering
    )
    
    print(f"✅ Python video created: {output_file}")
    print(f"   Duration: {duration} seconds")
    print(f"   Resolution: {width}x{height}")

if __name__ == "__main__":
    create_test_video()
