#!/usr/bin/env python3
#
# By Le Chen and Chatgpt
# chenle02@gmail.com / le.chen@auburn.edu
# Created at Wed 18 Oct 2023 12:11:25 PM EDT
#
import numpy as np
import matplotlib.pyplot as plt
import imageio

# Parameters
width = 100  # Width of the substrate
height = 100  # Maximum height of the substrate
steps = 4000  # Maximum number of particles to add
frames = []  # List to store frames for the movie

# Initialize 2D substrate
substrate = np.zeros((height, width))

for _ in range(steps):
    # Choose a random position to drop a particle
    position = np.random.randint(0, width)
    # print(f"Position: {position}")

    # For the middle column
    if np.any(substrate[:, position] == 1):  # If there's any nonzero value in the column
        landing_row_mid = np.argmax(substrate[:, position] == 1) - 1
    else:
        landing_row_mid = height - 1

    # print(f"Mid Column: {landing_row_mid}")

    # For the left column
    left_position = max(position - 1, 0)
    if np.any(substrate[:, left_position] == 1):  # If there's any nonzero value in the column
        landing_row_left = np.argmax(substrate[:, left_position] == 1) - 1
    else:
        landing_row_left = height - 1

    # print(f"Left Column: {landing_row_left}")

    # For the right column
    right_position = min(position + 1, width - 1)
    if np.any(substrate[:, right_position] == 1):  # If there's any nonzero value in the column
        landing_row_right = np.argmax(substrate[:, right_position] == 1) - 1
    else:
        landing_row_right = height - 1

    # print(f"Left Column: {landing_row_right}")

    landing_row = min(landing_row_left + 1, landing_row_mid, landing_row_right + 1)

    if landing_row < 10:
        break

    # print(f"Landing on: {landing_row}")
    substrate[landing_row, position] = 1
    # print(substrate)

    # Visualization for each step
    fig, ax = plt.subplots()
    ax.imshow(substrate, cmap='gray_r', aspect='auto')
    ax.set_title('Ballistic Deposition - Particle No.' + str(_))

    # Compute and plot the top envelope
    top_envelope = np.zeros(width)
    for pos in range(width):
        if np.any(substrate[:, pos] == 1):  # If there's any nonzero value in the column
            top_envelope[pos] = np.argmax(substrate[:, pos] == 1) - 2
        else:
            top_envelope[pos] = height - 1

    # top_envelope = height - 1 - np.argmax(substrate[::-1, :] == 1, axis=0)
    ax.plot(range(width), top_envelope, color='red', linewidth=2)

    # Relabel the y-axis
    ax.set_yticks(np.arange(0, height, height // 5))
    ax.set_yticklabels(np.arange(height, 0, -height // 5))

    ax.set_ylabel("Height", rotation=90, labelpad=20, verticalalignment='center')
    ax.set_xticks(np.arange(0, width + 1, 20))

    # Convert the plot to an image and append to frames
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    frames.append(image)

    plt.close(fig)

    # print the progress
    if (_ + 1) % 200 == 0:
        print(f"Step: {_ + 1}/{steps}, Maximum height: {height - np.min(top_envelope)}/{height}")


# print("Done")
# print(np.argmax(substrate[:, 0] == 1))
# Save frames as a movie
imageio.mimsave('BD_Movie.mp4', frames, fps=20)
