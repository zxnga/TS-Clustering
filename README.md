# Time-Series Clustering

This project focuses on clustering time-series data using various techniques, including derivatives, Fourier transformations, and Dynamic Time Warping (DTW).

## Table of Contents

- [Overview](#overview)
- [Techniques Used](#techniques-used)
- [Installation](#installation)
- [Usage](#usage)
- [Citation](#citation)
- [Contributing](#contributing)
- [License](#license)

## Overview

Time-series clustering is a method used to group similar time-series data based on specific characteristics or patterns. This project implements a clustering techniques using derivatives, Fourier transformations, and DTW to analyze and group time-series data effectively.

## Techniques Used

- **Derivative-Based Clustering:** Analyzes the rate of change in time-series data to identify patterns.
- **Fourier Transformation:** Converts time-series data into the frequency domain to detect periodic patterns.
- **Dynamic Time Warping (DTW):** Measures similarity between time-series sequences that may vary in time or speed.

## Installation

To set up the project environment, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/zxnga/TS-Clustering.git
   cd TS-Clustering
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Citation

If this project contributes to your research or work, please cite the following paper:

```bibtex
@article{zangato2025data,
  title={Data-driven policy mapping for safe RL-based energy management systems},
  author={Zangato, Th{\'e}o and Osmani, Aomar and Alizadeh, Pegah},
  journal={Energy Reports},
  volume={13},
  pages={1888--1909},
  year={2025},
  publisher={Elsevier}
}
```