# Python Animation Video Lab

A practical learning lab for building short-form animated content with Python, moving from single-file scripts to a reusable, scene-based render pipeline while still shipping real videos quickly.

## Overview

This project focuses on end-to-end video production, not just visuals:

- Render loop design
- Text and shape animation techniques
- Scene transitions and pacing
- Audio generation and muxing
- Output handling for platforms like TikTok, Reels, Shorts and 16:9 YouTube

## Features

- Vertical video rendering (1080x1920) for short-form platforms
- Procedural gradients, particles, wave fields and wireframe motion
- Dynamic text overlays and timed message changes
- Scene-based architecture for advanced projects
- Procedural music generation with NumPy and SciPy
- FFmpeg integration for audio/video muxing
- Clean output directory for generated assets

## Tech Stack

Python 3.10+, OpenCV, NumPy, SciPy, MoviePy and FFmpeg.

FFmpeg on the system PATH is recommended for audio muxing in the advanced pipeline.

## Project Structure

```text
py-video/
|-- src/                       # Source scripts for video generation
|   |-- simple_animation.py    # Beginner OpenCV animation example
|   |-- content_example.py     # OpenCV facts-card content video example
|   |-- python_video_test.py   # MoviePy timeline-based text video example
|   `-- advanced_video.py      # Multi-scene OpenCV + generated audio pipeline
|-- docs/                      # Learning and documentation assets
|   |-- learning_path.md       # Step-by-step learning roadmap
|   `-- previews/              # Local preview clips (generated, not committed)
|-- scripts/                   # Utility scripts for local workflow
|   `-- run_all.ps1            # PowerShell helper to run all demos
|-- output/                    # Generated render outputs (ignored by git)
|-- .editorconfig              # Editor consistency rules (indentation/newlines)
|-- .gitattributes             # Git line-ending and binary file handling rules
|-- requirements.txt
|-- .gitignore
|-- CHANGELOG.md
|-- CONTRIBUTING.md
|-- LICENSE
`-- README.md
```

## Quickstart

### 1. Create and activate a virtual environment

Windows PowerShell:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg (recommended)

Verify installation:

```bash
ffmpeg -version
```

> [!IMPORTANT]
> If FFmpeg is missing, `src/advanced_video.py` does not fail. It silently falls back to
> separate `output/temp_video.mp4` and `output/temp_audio.wav` files instead of the single
> muxed `output/advanced_video_with_sound.mp4`. Install FFmpeg first to get the real output.

### 4. Run scripts

```bash
python src/simple_animation.py
python src/content_example.py
python src/python_video_test.py
python src/advanced_video.py
```

PowerShell helper for all demos:

```bash
./scripts/run_all.ps1
```

All generated media is saved to `output/`.

## Script Breakdown

### 1) Beginner: OpenCV Motion Basics

Script: `src/simple_animation.py`

What it does:

- Creates a 10-second vertical animation
- Uses color-shifting gradients and bouncing title text
- Adds subtitle timing and circular particle motion

What it teaches:

- Frame loop fundamentals
- Sine-based motion control
- OpenCV text rendering with shadows
- Basic visual layering

Output: `output/my_first_animation.mp4`

### 2) Content Example: Facts-Card Video

Script: `src/content_example.py`

What it does:

- Renders a 15-second vertical facts-card video in the style of educational short-form content
- Animates a rotating set of two-line facts with eased transitions and a progress bar

What it teaches:

- Easing functions for smoother motion
- Timed content pacing across a fixed frame count
- Layout patterns for card-style short-form videos

Output: `output/content_example.mp4`

### 3) Intermediate: MoviePy Timeline Composition

Script: `src/python_video_test.py`

What it does:

- Builds a 10-second 1080p text sequence
- Composites timed clips over a background layer

What it teaches:

- Timeline-driven composition
- Clip start and duration control
- Fast iteration export settings

Output: `output/python_test_video.mp4`

### 4) Advanced: Multi-Scene Animation and Audio

Script: `src/advanced_video.py`

What it does:

- Builds a 30-second, four-scene vertical animation
- Generates a WAV soundtrack procedurally
- Muxes audio and video to a final MP4 using FFmpeg

Scene set:

- Scene 1: particle explosion intro
- Scene 2: wave field motion
- Scene 3: rotating wireframe cube
- Scene 4: animated text finale

What it teaches:

- Scene architecture and timeline segmentation
- Reusable animation function design
- Procedural audio basics
- FFmpeg-based production pipeline

Outputs:

- `output/advanced_video_with_sound.mp4` when FFmpeg is available
- `output/temp_video.mp4` and `output/temp_audio.wav` as fallback artifacts if FFmpeg is missing

## Render Pipeline Notes

Pipeline order in the advanced workflow:

1. Generate audio waveform and write WAV
2. Render frames to a temporary MP4
3. Mux the temporary MP4 and WAV into a final MP4 with AAC audio
4. Remove temporary files once the mux succeeds

This keeps visual generation independent from audio generation, makes debugging easier when one stage fails and scales better when adding transitions or post effects.

## Learning Path

A staged progression with practice tasks for each script lives in `docs/learning_path.md`, moving from core motion basics through compositing, scene systems, audio delivery and a reusable content template system.

## Troubleshooting

### FFmpeg not found

The advanced script finishes frame rendering but warns about missing FFmpeg. Install FFmpeg, make sure it is on the system PATH, then re-run the advanced script.

### MoviePy text rendering issues

Text clip creation errors or missing font rendering usually mean MoviePy or a local font is missing. Confirm the MoviePy installation and try a different font name in `src/python_video_test.py`.

### Slow renders on laptop hardware

Lower the fps from 30 to 24, shorten the duration while iterating or reduce resolution during draft runs.

## Roadmap

- Add subtitle/caption style presets
- Add transition utilities (slide, wipe, blur, zoom)
- Add beat-synced and audio-reactive effects
- Add export presets for Shorts, Reels, TikTok and 16:9 YouTube
- Add reusable module layout: `effects.py`, `titles.py`, `transitions.py`, `presets.py`
- Add CLI flags for duration, fps and resolution

## Contributing

Contributions are welcome. See `CONTRIBUTING.md` for the branch, commit and pull request conventions. Good first tasks include transition presets, CLI flags and reusable effect modules.

## License

MIT License. See `LICENSE`.

## Contact and Support

Open an [issue](https://github.com/zaccesss/py-video/issues) in this repository for questions or bugs, or reach out at [code@isaacadjei.me](mailto:code@isaacadjei.me) or through the [website contact page](https://isaacadjei.me/contact).
