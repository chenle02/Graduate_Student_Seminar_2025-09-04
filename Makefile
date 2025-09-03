# Makefile for project animations

# Default Manim flags. Can be overridden from the command line.
# Example: make lis-random-proto MANIM_FLAGS="-qh"
MANIM_FLAGS ?= -pqh

.PHONY: all clean lis lis-gemini lis-random-small lis-random-large lis-random-proto

# Default target
all: lis lis-gemini lis-random-small lis-random-large lis-random-proto

lis:
	@echo "Rendering original LIS animation..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_manim.py LisDPScene
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_manim/1080p60/LisDPScene.mp4 videos/LIS_DP_VdC.mp4

lis-gemini:
	@echo "Rendering Gemini LIS animation..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_manim_gemini.py LisDPSceneGemini
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_manim_gemini/1080p60/LisDPSceneGemini.mp4 videos/LIS_DP_VdC_gemini.mp4

lis-random-small:
	@echo "Rendering LIS random permutations (small)..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_random_permutations.py LisPermutationsSmall
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_random_permutations/1080p60/LisPermutationsSmall.mp4 videos/LIS_Random_Small.mp4

lis-random-large:
	@echo "Rendering LIS random permutations (large)..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_random_permutations.py LisPermutationsLarge
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_random_permutations/1080p60/LisPermutationsLarge.mp4 videos/LIS_Random_Large.mp4

# Makefile for project animations

# Default Manim flags. Can be overridden from the command line.
# Example: make lis-random-proto MANIM_FLAGS="-qh"
MANIM_FLAGS ?= -pqh

.PHONY: all clean lis lis-gemini lis-random-small lis-random-large lis-random-proto lis-lpp lis-lpp-proto

# Default target
all: lis lis-gemini lis-random-small lis-random-large lis-random-proto lis-lpp

lis:
	@echo "Rendering original LIS animation..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_manim.py LisDPScene
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_manim/1080p60/LisDPScene.mp4 videos/LIS_DP_VdC.mp4

lis-gemini:
	@echo "Rendering Gemini LIS animation..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_manim_gemini.py LisDPSceneGemini
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_manim_gemini/1080p60/LisDPSceneGemini.mp4 videos/LIS_DP_VdC_gemini.mp4

lis-random-small:
	@echo "Rendering LIS random permutations (small)..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_random_permutations.py LisPermutationsSmall
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_random_permutations/1080p60/LisPermutationsSmall.mp4 videos/LIS_Random_Small.mp4

lis-random-large:
	@echo "Rendering LIS random permutations (large)..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_random_permutations.py LisPermutationsLarge
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_random_permutations/1080p60/LisPermutationsLarge.mp4 videos/LIS_Random_Large.mp4

lis-random-proto:
	@echo "Rendering LIS random permutations (prototype)..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_random_permutations.py LisPermutationsPrototype
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_random_permutations/1080p60/LisPermutationsPrototype.mp4 videos/LIS_Random_Proto.mp4

lis-lpp:
	@echo "Rendering LIS-LPP animation..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_lpp_animation.py LisLppScene
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_lpp_animation/1080p60/LisLppScene.mp4 videos/LIS_LPP.mp4

lis-lpp-proto:
	@echo "Rendering LIS-LPP prototype animation..."
	manim $(MANIM_FLAGS) Longest_increasing_subsequence/lis_lpp_animation.py LisLppPrototypeScene
	@echo "Copying video to videos/"
	@mkdir -p videos
	@cp media/videos/lis_lpp_animation/1080p60/LisLppPrototypeScene.mp4 videos/LIS_LPP_Proto.mp4

clean:
	@echo "Cleaning up Manim media files..."
	@rm -rf media


clean:
	@echo "Cleaning up Manim media files..."
	@rm -rf media