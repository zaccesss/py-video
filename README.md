# Python Animation Video Lab

Learn Python animation and content-video production from first render to social-ready exports.

This repository is designed as a practical learning lab:

- Beginner foundation with OpenCV frame-by-frame animation
- Intermediate timeline compositing with MoviePy
- Advanced scene system with generated audio and FFmpeg muxing

## Quick Navigation

<p align="center">
	🔎 <b>Quick navigation:</b>
	<a href="#overview">Overview</a> •
	<a href="#why-this-project">Why This Project</a> •
	<a href="#features">Features</a> •
	<a href="#tech-stack">Tech Stack</a> •
	<a href="#project-structure">Project Structure</a> •
	<a href="#quickstart">Quickstart</a> •
	<a href="#script-breakdown">Script Breakdown</a> •
	<a href="#render-pipeline-notes">Render Pipeline Notes</a> •
	<a href="#learning-path">Learning Path</a> •
	<a href="#troubleshooting">Troubleshooting</a> •
	<a href="#roadmap">Roadmap</a> •
	<a href="#contributing">Contributing</a> •
	<a href="#license">License</a>
</p>

## Overview

Python Animation Video Lab is a creator-focused starter project for building short-form animated content with code.
It helps you move from one-file scripts to reusable scene systems while still shipping real videos quickly.

Target outcomes:

- Understand time-based animation math with Python
- Build scene-driven video structure for longer content
- Generate and sync audio with video
- Produce reusable workflow patterns for TikTok, Reels, Shorts, and long-form edits

## Why This Project

Many creative coding examples show visuals only. This project focuses on end-to-end content production:

- Render loop design
- Text and shape animation techniques
- Scene transitions and pacing
- Audio generation and muxing
- Practical output handling for publish workflows

## Features

- Vertical video rendering (1080x1920) for short-form platforms
- Procedural gradients, particles, wave fields, and wireframe motion
- Dynamic text overlays and timed message changes
- Scene-based architecture for advanced projects
- Procedural music generation using NumPy + SciPy
- FFmpeg integration for audio/video merge
- Clean output directory for generated assets

## Tech Stack

<div align="center">

| <img src="https://techstack-generator.vercel.app/python-icon.svg" width="65" /> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" width="65" /> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="65" /> | <img src="https://upload.wikimedia.org/wikipedia/commons/b/b2/SCIPY_2.svg" width="65" /> | <img src="https://raw.githubusercontent.com/Zulko/moviepy/master/docs/_static/logo_small.jpeg" width="65" /> | <img src="https://cdn.simpleicons.org/ffmpeg/007808" width="65" /> |
| :-----------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------: |
|                                   **Python**                                    |                                               **OpenCV**                                               |                                              **NumPy**                                               |                                        **SciPy**                                         |                                                 **MoviePy**                                                  |                             **FFmpeg**                             |

</div>

- Python 3.10+
- FFmpeg installed on system PATH is recommended for audio muxing in the advanced pipeline

## Project Structure

```text
py-video/
|-- src/                     # Source scripts for video generation
|   |-- simple_animation.py  # Beginner OpenCV animation example
|   |-- python_video_test.py # MoviePy timeline-based text video example
|   `-- advanced_video.py    # Multi-scene OpenCV + generated audio pipeline
|-- docs/                    # Learning and documentation assets
|   |-- learning_path.md     # Step-by-step learning roadmap
|   `-- previews/            # Short preview clips embedded in README/project pages
|       |-- simple_preview.mp4
|       `-- advanced_preview.mp4
|-- scripts/                 # Utility scripts for local workflow
|   `-- run_all.ps1          # PowerShell helper to run all three demos
|-- output/                  # Generated render outputs (ignored by git)
|   |-- my_first_animation.mp4
|   |-- temp_video.mp4
|   `-- temp_audio.wav
|-- .editorconfig            # Editor consistency rules (indentation/newlines)
|-- .gitattributes           # Git line-ending and binary file handling rules
|-- requirements.txt
|-- .gitignore
|-- CHANGELOG.md
|-- CONTRIBUTING.md
|-- LICENSE
`-- README.md
```

### Structure Details

| Path | Type | Purpose |
| --- | --- | --- |
| src/ | Folder | Core Python scripts that generate videos and audio. |
| src/simple_animation.py | File | Beginner script for frame-by-frame OpenCV animation in vertical format. |
| src/python_video_test.py | File | Intermediate MoviePy example for timeline/text compositing. |
| src/advanced_video.py | File | Advanced scene-based renderer with procedural soundtrack and FFmpeg muxing. |
| docs/ | Folder | Documentation and visual learning resources. |
| docs/learning_path.md | File | Learning progression and practice tasks for building animation skills. |
| docs/previews/ | Folder | Short preview clips used for showcasing output quickly. |
| scripts/ | Folder | Workflow helpers for local execution. |
| scripts/run_all.ps1 | File | Runs all demo scripts in sequence from PowerShell. |
| output/ | Folder | Rendered assets created by scripts (video/audio outputs). |
| requirements.txt | File | Python dependency list required for all scripts. |
| .gitignore | File | Prevents generated outputs and cache files from polluting commits. |
| .editorconfig | File | Standardizes editor behavior across environments. |
| .gitattributes | File | Enforces line ending strategy and binary handling in git. |
| CHANGELOG.md | File | Versioned log of notable project changes. |
| CONTRIBUTING.md | File | Contribution process and commit style guidance. |
| LICENSE | File | MIT license terms for project use and distribution. |
| README.md | File | Main project overview, setup, usage, and roadmap. |

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

### 4. Run scripts

```bash
python src/simple_animation.py
python src/python_video_test.py
python src/advanced_video.py
```

PowerShell helper:

```bash
./scripts/run_all.ps1
```

All generated media is saved to output.

## Script Breakdown

### 1) Beginner: OpenCV Motion Basics

Script: src/simple_animation.py

What it does:

- Creates a 10-second vertical animation
- Uses color-shifting gradients and bouncing title text
- Adds subtitle timing and circular particle motion

What you learn:

- Frame loop fundamentals
- Sine-based motion control
- OpenCV text rendering with shadows
- Basic visual layering

Output:

- output/my_first_animation.mp4

### 2) Intermediate: MoviePy Timeline Composition

Script: src/python_video_test.py

What it does:

- Builds a 10-second 1080p text sequence
- Composites timed clips over a background layer

What you learn:

- Timeline-driven composition
- Clip start and duration control
- Fast iteration export settings

Output:

- output/python_test_video.mp4

### 3) Advanced: Multi-Scene Animation + Audio

Script: src/advanced_video.py

What it does:

- Builds a 30-second, four-scene vertical animation
- Generates a WAV soundtrack procedurally
- Muxes audio/video to final MP4 using FFmpeg

Scene set:

- Scene 1: particle explosion intro
- Scene 2: wave field motion
- Scene 3: rotating wireframe cube
- Scene 4: animated text finale

What you learn:

- Scene architecture and timeline segmentation
- Reusable animation function design
- Procedural audio basics
- FFmpeg-based production pipeline

Outputs:

- output/advanced_video_with_sound.mp4 when FFmpeg is available
- output/temp_video.mp4 and output/temp_audio.wav as fallback artifacts if FFmpeg is missing

## Render Pipeline Notes

Pipeline order in advanced workflow:

1. Generate audio waveform and write WAV
2. Render frames to temporary MP4
3. Mux temporary MP4 + WAV into final MP4 with AAC audio
4. Remove temporary files when mux succeeds

Why this structure matters:

- Keeps visual generation independent from audio generation
- Makes debugging easier when one stage fails
- Scales better when you add transitions or post effects

## Learning Path

Detailed progression and practice tasks are in docs/learning_path.md.

Suggested flow:

1. Start with simple_animation.py and modify timing/colors/text
2. Move to python_video_test.py for timeline mindset
3. Extend advanced_video.py with a new custom scene
4. Build your own reusable effect modules under src

## Troubleshooting

### FFmpeg not found

Symptoms:

- Advanced script finishes frame rendering but warns about missing FFmpeg

Fix:

- Install FFmpeg and ensure it is in system PATH
- Re-run advanced script

### MoviePy text rendering issues

Symptoms:

- Text clip creation errors or missing font rendering

Fix:

- Confirm MoviePy installation and available local fonts
- Try replacing font name in src/python_video_test.py

### Slow renders on laptop hardware

Practical options:

- Lower fps from 30 to 24
- Shorten duration while iterating
- Reduce resolution during draft runs

## Roadmap

- Add subtitle/caption style presets
- Add transition utilities (slide, wipe, blur, zoom)
- Add beat-synced and audio-reactive effects
- Add export presets for Shorts, Reels, TikTok, and 16:9 YouTube
- Add reusable module layout: effects.py, titles.py, transitions.py, presets.py

## Project Status

Active learning project with production-oriented examples.

Best use case:

- Developers and creators who want to learn animation engineering while building publishable video content.

## Contributing

Contributions are welcome.

- Contributor guide: CONTRIBUTING.md
- Suggested first tasks: transition presets, CLI flags, and reusable effect modules

## License

MIT License. See LICENSE.
