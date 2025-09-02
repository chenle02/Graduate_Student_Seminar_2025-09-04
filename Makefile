# Makefile for project animations

.PHONY: all clean lis lis-gemini

# Default target
all: lis lis-gemini

lis-gemini:
	@echo "Rendering Gemini LIS animation..."
	manim -pqh Longest_increasing_subsequence/lis_manim_gemini.py LisDPSceneGemini
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_manim_gemini/1080p60/LisDPSceneGemini.mp4 videos/LIS_DP_VdC_gemini.mp4

clean:
	@echo "Cleaning up Manim media files..."
	@rm -rf media
