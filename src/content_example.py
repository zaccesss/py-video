#!/usr/bin/env python3
"""
Content Example - Python Facts Card Video
A polished 15-second vertical content video in the style of educational short-form content.
Run: python src/content_example.py
"""

import cv2
import numpy as np
import math
from pathlib import Path

# --- Settings ---
WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION = 15
TOTAL_FRAMES = FPS * DURATION

# --- Color palette (BGR) ---
ACCENT       = (0, 180, 255)      # Gold/amber
ACCENT_CYAN  = (255, 200, 60)     # Teal progress bar
WHITE        = (255, 255, 255)
DIM          = (160, 160, 160)
DARK         = (30, 25, 20)       # Near-black warm tone
GRID_DOT     = (55, 50, 45)
DOT_INACTIVE = (70, 70, 70)

# --- Content ---
FACTS = [
    ("Python was", "created in 1991"),
    ("#1 most popular", "language worldwide"),
    ("Make a video", "in 20 lines of code"),
    ("OpenCV powers", "real-time AI vision"),
    ("You're already", "doing it. Keep going."),
]


def ease_in_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def alpha_color(color: tuple, a: float) -> tuple:
    return tuple(int(c * a) for c in color)


def draw_text_centered(frame, text, y, scale, color, thickness, shadow=True):
    font = cv2.FONT_HERSHEY_SIMPLEX
    (tw, _), _ = cv2.getTextSize(text, font, scale, thickness)
    x = (WIDTH - tw) // 2
    if shadow:
        cv2.putText(frame, text, (x + 3, y + 3), font, scale,
                    (0, 0, 0), thickness + 3, cv2.LINE_AA)
    cv2.putText(frame, text, (x, y), font, scale, color, thickness, cv2.LINE_AA)
    return tw, x


def draw_background(frame, t):
    # Warm dark gradient top to bottom
    for y in range(HEIGHT):
        r = int(22 + 10 * (y / HEIGHT))
        g = int(18 + 8 * (y / HEIGHT))
        b = int(28 + 12 * (y / HEIGHT))
        frame[y, :] = [b, g, r]  # BGR

    # Animated subtle dot grid
    spacing = 90
    for gy in range(spacing, HEIGHT, spacing):
        for gx in range(spacing, WIDTH, spacing):
            dist = math.sqrt((gx - WIDTH // 2) ** 2 + (gy - HEIGHT // 2) ** 2)
            phase = dist * 0.006 - t * 1.4
            a = max(0.0, 0.35 + 0.25 * math.sin(phase))
            brightness = int(65 * a)
            cv2.circle(frame, (gx, gy), 2,
                       (brightness + 10, brightness, brightness + 20), -1, cv2.LINE_AA)


def draw_header(frame):
    # Top accent line
    cv2.line(frame, (100, 185), (WIDTH - 100, 185), ACCENT, 2, cv2.LINE_AA)
    # Label
    draw_text_centered(frame, "PYTHON  FACTS", 160, 1.05, ACCENT, 2, shadow=False)


def draw_fact(frame, t, fact_index):
    fact_duration = DURATION / len(FACTS)
    fact_t = (t - fact_index * fact_duration) / fact_duration  # 0-1 within current fact

    # Fade envelope
    if fact_t < 0.18:
        alpha = ease_in_out(fact_t / 0.18)
    elif fact_t > 0.82:
        alpha = ease_in_out((1.0 - fact_t) / 0.18)
    else:
        alpha = 1.0

    # Slide up on entry
    slide = int(40 * (1.0 - ease_in_out(min(fact_t / 0.22, 1.0))))

    line1, line2 = FACTS[fact_index]
    cy = HEIGHT // 2

    # Line 1: dimmer label
    draw_text_centered(frame, line1, cy - 55 + slide, 1.55,
                       alpha_color(DIM, alpha), 2)

    # Line 2: main bold statement
    _, x2 = draw_text_centered(frame, line2, cy + 45 + slide, 2.3,
                                alpha_color(WHITE, alpha), 4)

    # Animated underline beneath line 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    (tw, _), _ = cv2.getTextSize(line2, font, 2.3, 4)
    ux = (WIDTH - tw) // 2
    uy = cy + 90 + slide
    # Draw from left to right based on alpha
    line_end = ux + int(tw * ease_in_out(min(fact_t / 0.35, 1.0)))
    if line_end > ux:
        cv2.line(frame, (ux, uy), (line_end, uy),
                 alpha_color(ACCENT, alpha), 3, cv2.LINE_AA)


def draw_nav_dots(frame, active_index):
    total = len(FACTS)
    gap = 32
    start_x = WIDTH // 2 - (total - 1) * gap // 2
    dot_y = HEIGHT - 240
    for i in range(total):
        dx = start_x + i * gap
        if i == active_index:
            cv2.circle(frame, (dx, dot_y), 9, ACCENT, -1, cv2.LINE_AA)
            cv2.circle(frame, (dx, dot_y), 12, alpha_color(ACCENT, 0.3), 2, cv2.LINE_AA)
        else:
            cv2.circle(frame, (dx, dot_y), 5, DOT_INACTIVE, -1, cv2.LINE_AA)


def draw_progress_bar(frame, progress):
    bar_y = HEIGHT - 90
    margin = 80
    bar_w = WIDTH - margin * 2

    # Track
    cv2.rectangle(frame, (margin, bar_y - 3),
                  (margin + bar_w, bar_y + 3), (50, 45, 40), -1)
    # Fill
    filled = int(bar_w * progress)
    if filled > 0:
        cv2.rectangle(frame, (margin, bar_y - 3),
                      (margin + filled, bar_y + 3), ACCENT_CYAN, -1)
        # Glowing tip
        tip_x = margin + filled
        for r, a in [(10, 0.15), (6, 0.3), (3, 1.0)]:
            cv2.circle(frame, (tip_x, bar_y), r, alpha_color(ACCENT_CYAN, a), -1, cv2.LINE_AA)


def draw_branding(frame):
    draw_text_centered(frame, "py-video  •  github.com/zaccesss",
                       HEIGHT - 130, 0.55, (90, 85, 80), 1, shadow=False)


def render_frame(frame_num):
    t = frame_num / FPS
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    fact_duration = DURATION / len(FACTS)
    fact_index = min(int(t / fact_duration), len(FACTS) - 1)

    draw_background(frame, t)
    draw_header(frame)
    draw_fact(frame, t, fact_index)
    draw_nav_dots(frame, fact_index)
    draw_progress_bar(frame, t / DURATION)
    draw_branding(frame)

    return frame


def create_content_example():
    print("🎬 Rendering content example...")
    print(f"   {WIDTH}x{HEIGHT}  •  {FPS}fps  •  {DURATION}s  •  {TOTAL_FRAMES} frames")

    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "content_example.mp4"

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(str(output_file), fourcc, FPS, (WIDTH, HEIGHT))

    for frame_num in range(TOTAL_FRAMES):
        out.write(render_frame(frame_num))
        if (frame_num + 1) % FPS == 0:
            sec = (frame_num + 1) // FPS
            fact_i = min(int(sec / (DURATION / len(FACTS))), len(FACTS) - 1)
            print(f"  {sec}s/{DURATION}s  —  fact {fact_i + 1}/{len(FACTS)}")

    out.release()
    print(f"\n✅ Saved: {output_file}")
    print("   Open the file in output/ to see it!")


if __name__ == "__main__":
    create_content_example()
