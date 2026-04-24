# Python Animation Video Lab

Create short-form animations and content videos with Python.

This repo is organized for learning in stages:

- Beginner: basic OpenCV animation loop and moving text
- Intermediate: simple MoviePy text-video workflow
- Advanced: multi-scene OpenCV video with generated audio + FFmpeg muxing

## Project Structure

- `src/simple_animation.py` - 10-second vertical animation with gradients, text, and particles
- `src/python_video_test.py` - 10-second 1080p text sequence using MoviePy
- `src/advanced_video.py` - 30-second multi-scene animation with generated WAV music
- `output/` - rendered videos and temporary media files
- `docs/learning_path.md` - step-by-step learning roadmap
- `requirements.txt` - Python dependencies

## Quick Start

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional but recommended) Install FFmpeg and verify:

```bash
ffmpeg -version
```

4. Run a script:

```bash
python src/simple_animation.py
python src/python_video_test.py
python src/advanced_video.py
```

All generated media is saved into `output/`.

## Script Details

### 1) Beginner: Simple OpenCV Animation

Command:

```bash
python src/simple_animation.py
```

What you learn:

- Frame-by-frame rendering with NumPy arrays
- Time-based motion using sine functions
- Drawing text, shadows, and simple particles with OpenCV
- Vertical video setup for TikTok/Reels (1080x1920)

Output:

- `output/my_first_animation.mp4`

### 2) Intermediate: MoviePy Text Video

Command:

```bash
python src/python_video_test.py
```

What you learn:

- Building clips and compositing layers in MoviePy
- Timing text changes using start/duration
- Quick export settings for fast iteration

Output:

- `output/python_test_video.mp4`

### 3) Advanced: Multi-Scene + Music

Command:

```bash
python src/advanced_video.py
```

What you learn:

- Multi-scene animation architecture
- Procedural music generation (NumPy + SciPy)
- Combining video and audio with FFmpeg
- Managing temporary render files

Outputs:

- `output/advanced_video_with_sound.mp4` (if FFmpeg is installed)
- `output/temp_video.mp4` and `output/temp_audio.wav` if FFmpeg is missing

## Publish to GitHub

From the project root:

```bash
git init
git add .
git commit -m "init: organize python animation video lab"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

Suggested repo description:

"Learn Python animation and content-video creation with OpenCV, MoviePy, and procedural audio. Includes beginner-to-advanced examples for short-form vertical video workflows."

Suggested topics:

- `python`
- `opencv`
- `moviepy`
- `video-generation`
- `animation`
- `content-creation`
- `ffmpeg`
- `creative-coding`

## Next Improvements

- Add subtitle templates and caption styles
- Add transition helpers (slide, wipe, blur)
- Add audio-reactive visual effects
- Add export presets for YouTube Shorts, Reels, TikTok, and 16:9
