# Makefile for project animations

.PHONY: all clean lis lis-gemini lis-random-small lis-random-large

# Default target
all: lis lis-gemini lis-random-small lis-random-large

lis:
	@echo "Rendering original LIS animation..."
	manim -pqh Longest_increasing_subsequence/lis_manim.py LisDPScene
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_manim/1080p60/LisDPScene.mp4 videos/LIS_DP_VdC.mp4

lis-gemini:
	@echo "Rendering Gemini LIS animation..."
	manim -pqh Longest_increasing_subsequence/lis_manim_gemini.py LisDPSceneGemini
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_manim_gemini/1080p60/LisDPSceneGemini.mp4 videos/LIS_DP_VdC_gemini.mp4

lis-random-small:
	@echo "Rendering LIS random permutations (small)..."
	manim -pqh Longest_increasing_subsequence/lis_random_permutations.py LisPermutationsSmall
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_random_permutations/1080p60/LisPermutationsSmall.mp4 videos/LIS_Random_Small.mp4

lis-random-large:
	@echo "Rendering LIS random permutations (large)..."
	manim -pqh Longest_increasing_subsequence/lis_random_permutations.py LisPermutationsLarge
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_random_permutations/1080p60/LisPermutationsLarge.mp4 videos/LIS_Random_Large.mp4

clean:
	@echo "Cleaning up Manim media files..."
	@rm -rf media