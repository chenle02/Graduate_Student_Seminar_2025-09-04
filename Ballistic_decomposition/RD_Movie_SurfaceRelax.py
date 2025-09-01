#!/usr/bin/env python3
"""Random deposition with surface relaxation movie generator."""

import numpy as np
import matplotlib.pyplot as plt
import imageio


def simulate(width: int = 100, height: int = 50, steps: int = 4000,
             save_movie: bool = True,
             movie_name: str = "RD_Movie_SuraceRelax.mp4"):
    """Run the random deposition with surface relaxation simulation.

    Parameters
    ----------
    width : int
        Width of the substrate.
    height : int
        Height of the substrate.
    steps : int
        Number of particles to drop.
    save_movie : bool
        When ``True`` frames are written to ``movie_name``.
    movie_name : str
        Name of the generated movie file.

    Returns
    -------
    list[np.ndarray]
        List of RGB frames captured during the simulation.
    """

    frames = []
    substrate = np.zeros((height, width))

    for step in range(steps):
        position = np.random.randint(0, width)

        if np.any(substrate[:, position] == 1):
            landing_row_mid = np.argmax(substrate[:, position] == 1) - 1
        else:
            landing_row_mid = height - 1

        left_position = max(position - 1, 0)
        if np.any(substrate[:, left_position] == 1):
            landing_row_left = np.argmax(substrate[:, left_position] == 1) - 1
        else:
            landing_row_left = height - 1

        right_position = min(position + 1, width - 1)
        if np.any(substrate[:, right_position] == 1):
            landing_row_right = np.argmax(substrate[:, right_position] == 1) - 1
        else:
            landing_row_right = height - 1

        if landing_row_right > max(landing_row_mid, landing_row_left):
            if position < width - 1:
                substrate[landing_row_right, position + 1] = 1
        else:
            if landing_row_left > landing_row_mid and position > 1:
                substrate[landing_row_left, position - 1] = 1
            else:
                substrate[landing_row_mid, position] = 1

        fig, ax = plt.subplots()
        ax.imshow(substrate, cmap="gray_r", aspect="auto")
        ax.set_title(
            f"Random Deposition with surface relaxation - Particle No. {step}")

        top_envelope = np.zeros(width)
        for pos in range(width):
            if np.any(substrate[:, pos] == 1):
                top_envelope[pos] = np.argmax(substrate[:, pos] == 1) - 2
            else:
                top_envelope[pos] = height - 1

        ax.plot(range(width), top_envelope, color="red", linewidth=2)
        ax.set_yticks(np.arange(0, height, max(1, height // 5)))
        ax.set_yticklabels(np.arange(height, 0, -max(1, height // 5)))
        ax.set_ylabel("Height", rotation=90, labelpad=20,
                     verticalalignment="center")
        ax.set_xticks(np.arange(0, width + 1, max(1, width // 5)))

        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.buffer_rgba(), dtype="uint8")
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (4,))[:, :, :3]
        frames.append(image)
        plt.close(fig)

        topmost = np.min(np.where(substrate == 1)[0])
        if topmost < height * 0.10:
            break

        if (step + 1) % 200 == 0:
            print(f"Step: {step + 1}/{steps}, Level at {height - topmost}/{height}")

    if save_movie:
        imageio.mimsave(movie_name, frames, fps=20)

    return frames


if __name__ == "__main__":
    simulate()
