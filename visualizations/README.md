# Visualizations for *The Geometry of Meaning*

Manim-based 3D visualizations of Geometric Algebra concepts.

## Prerequisites

```bash
pip install manim
```

## Rendering

All three scenes:

```bash
manim -qh ch3_ga_visualization.py Scene1_GeometricProduct
manim -qh ch3_ga_visualization.py Scene2_BivectorOrientation
manim -qh ch3_ga_visualization.py Scene3_TrivectorVolume
```

Stitch with ffmpeg:

```bash
cat > concat.txt << 'EOF'
file 'media/videos/ch3_ga_visualization/1080p60/Scene1_GeometricProduct.mp4'
file 'media/videos/ch3_ga_visualization/1080p60/Scene2_BivectorOrientation.mp4'
file 'media/videos/ch3_ga_visualization/1080p60/Scene3_TrivectorVolume.mp4'
EOF
ffmpeg -y -f concat -safe 0 -i concat.txt -c copy final.mp4
```

## Scenes

1. **Scene 1** — The geometric product: two vectors, dot product projection, wedge product parallelogram, formula reveal
2. **Scene 2** — Bivector orientation: a∧b, orientation arc, then flips to show b∧a = -(a∧b)
3. **Scene 3** — Trivector volume: three vectors build a parallelepiped, camera rotates to show 3D structure, grade hierarchy revealed

## Pre-rendered

A pre-rendered version (480p, ~56s) is included as `ch3_ga_visualization.mp4`.
