# Game Data Enhancement Script Usage Instructions

This document provides step-by-step instructions on how to run the Python script `enhance_games.py` to enrich game data from a CSV file with genre, short description, and player mode information using the Google Gemini API.

## Prerequisites

Before running the script, ensure you have the following prerequisites met:

1.  **Python Installed:** Make sure you have Python 3 installed on your system. You can download and install it from the [official Python website](https://www.python.org/downloads/).

2.  **Access to Google Gemini API:** You will need access to the Google Gemini API and a valid API key. You can obtain an API key through [Google AI Studio](https://aistudio.google.com/).

3.  **`requirements.txt` File (If Present):** If your project repository includes a `requirements.txt` file, it contains a list of Python libraries required by the script.

4.  **`config.ini` File (If Using Local Configuration):** If your script is configured to read the API key from a `config.ini` file, you will need to create this file with the correct format.

5.  **Game Data CSV File:** You need a CSV file containing a list of game titles you want to enrich. By default, the script looks for a file named `Game Thumbnail.csv` in the same directory as the script.

## Usage Steps

Here are the steps to run the `enhance_games.py` script:

### 1. Install Required Libraries (If `requirements.txt` Exists)

If your project includes a `requirements.txt` file, open your terminal or command prompt, navigate to the project directory, and run the following command to install all the necessary libraries:

```bash
pip install -r requirements.txt
```

This command will read the requirements.txt file and install all the listed libraries, including pandas and google-generativeai.
### 2. Configure the API Key

To configure API Key you can set your API key as an environment variable in your operating system.

- **On Linux/macOS**: Open your terminal and run the following command (replace YOUR_ACTUAL_API_KEY with your key):

    ```bash
    export GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY"
    ```

    To make this permanent for future terminal sessions, you can add this line to your shell configuration file (e.g., .bashrc, .zshrc).

- **On Windows (Command Prompt)**: Open Command Prompt and run:

```bash
set GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY"
```

This will only apply to the current Command Prompt session. To make it permanent, use the "Environment Variables" settings in System Properties.

- **On Windows (PowerShell)**: Open PowerShell and run:
```bash
$env:GOOGLE_API_KEY = "YOUR_ACTUAL_API_KEY"
```

To make it permanent, you might need to modify your system's environment settings.

Ensure that your enhance_games.py script is configured to read the API key from environment variables if you choose this method.

### 3. Prepare the Game Data CSV File

Make sure you have a CSV file containing the list of game titles. By default, the script looks for a file named Game Thumbnail.csv in the same directory as the script. If your CSV file has a different name or is located elsewhere, you need to modify the following line in the enhance_games.py script accordingly:
Python

```python
csv_link = "Game Thumbnail.csv" # Replace with the path to your CSV file if different
```

Your CSV file should have at least one column containing the game titles. Ensure that the column name containing the game titles matches how the script accesses it (in this script, it's assumed to be named game_title).

### 4. Run the Script

Once you have installed all the requirements, configured the API key, and ensured your game data CSV file is ready, you can run the enhance_games.py script. Open your terminal or command prompt, navigate to the directory where you saved the script, and run the following command:  

```bash
python enhance_games.py
```

The script will start processing each game title in the CSV file, sending requests to the Google Gemini API to retrieve the genre, short description, and player mode. The script will display a progress bar during the processing.

### 5. Check the Output

After the script finishes running, the enriched game data will be saved in a new CSV file named enhanced_games.csv (or the name you specified in the output_filepath variable within the script) in the same directory as the script. This file will contain the original columns from your input file, along with new columns for genre, short_description, and player_mode.
Important Notes

- Rate Limits: Be mindful of the Google Gemini API rate limits, especially if you are using the free tier. This script includes a delay (time.sleep(delay)) between API calls to help avoid rate limiting. You can adjust the DELAY_BETWEEN_CALLS value in the script if necessary.
- API Usage Costs: Using the Google Gemini API may incur costs depending on your plan and usage. Carefully review the Google AI Studio pricing terms.
- Error Handling: The script includes basic error handling (e.g., if the CSV file is not found or if there's an error calling the API). You might need to enhance the error handling based on your specific needs.
- Internet Connection: The script requires an active internet connection to communicate with the Google Gemini API.
- API Key Security: Keep your API key secure. Never share it publicly or store it directly in source code that is uploaded to public version control systems. Using a config.ini file that is not tracked by Git or environment variables is a more secure approach.

By following these instructions, you should be able to run the enhance_games.py script to enrich your game data using the Google Gemini API.
