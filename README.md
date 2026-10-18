## NASA's Astronomy Picture of the Day Data Analysis
Python project analyzing NASA's Astronomy Picture of the Day to analyze astronomy data. 

## Project Overview

This project uses NASA's Astronomy Picture of the Day (APOD) API to retrieve data related to astronomy and analyze it using Python. The goal is to explore the types of astronomical media featured by NASA and identify common keywords in the titles and explanations.

## Objectives

- Retrieve astronomy data from NASA's APOD API for a date range.
- Organize the retrieved data into a structured dataset using pandas.
- Count occurrences of selected astronomy-related keywords in titles and explanations.
- Visualize the results using charts.


## Repository Contents

- `nasaproject_analysis.py` will be used to retrieve, and analyze the data.  
- `requirements.txt` contains the packages required to run the code. 
- `output/` will contain the generated charts and graphs. 

## Installation

1. Clone or download this repository.
2. Install Python 3 if it is not already installed.
3. Install the required packages:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

## How to Run

From the project directory, run:

```bash
python3 nasaproject_analysis.py
```

The script retrieves data from the API, performs the analysis, displays summary statistics, and saves the resulting dataset and visualizations in the `output/` directory.

## Data Source

NASA Astronomy Picture of the Day (APOD):  
https://apod.nasa.gov/apod/astropix.html


## Expected Outputs

- A CSV file containing the retrieved astronomy records.
- A bar chart showing the distribution of media types.
- Printed summary statistics in the terminal.
