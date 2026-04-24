# Learning Path: Python Animations and Content Videos

## Goal

Build confidence to create short animated content videos in Python and publish repeatable workflows.

## Stage 1: Core Motion Basics (1-2 days)

Run:

```bash
python src/simple_animation.py
```

Practice tasks:

- Change duration from 10s to 6s
- Change subtitle messages and timing
- Change particle count and speed
- Try a horizontal frame (1920x1080)

Concepts:

- Time value per frame: `t = frame / fps`
- Smooth looping with `sin` and `cos`
- Rendering text and shapes every frame

## Stage 2: Compositing Mindset (1 day)

Run:

```bash
python src/python_video_test.py
```

Practice tasks:

- Add more text clips and stagger timing
- Change typography and font size
- Add a second background color segment

Concepts:

- Clips as timeline objects
- Layer compositing
- Fast export loop for iteration

## Stage 3: Scene Systems (2-3 days)

Run:

```bash
python src/advanced_video.py
```

Practice tasks:

- Add Scene 5 with your own effect
- Move from 4 scenes to 6 scenes
- Create smooth scene transitions

Concepts:

- Scene-based architecture
- Reusable scene functions
- Structured render loop control

## Stage 4: Audio + Delivery (1 day)

Practice tasks:

- Swap generated audio with your own soundtrack
- Try AAC bitrates and check file size/quality
- Add outro card for branding

Concepts:

- Audio/video muxing with FFmpeg
- Render pipeline reliability
- Final output checks before upload

## Stage 5: Build a Content Template System (ongoing)

Create reusable modules:

- `effects.py` for shared visual effects
- `titles.py` for text presets
- `transitions.py` for scene transitions
- `presets.py` for output formats

Outcome:

- One command per content format
- Faster production with consistent style
