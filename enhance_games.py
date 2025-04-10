import pandas as pd # Imports the pandas library for data manipulation, like reading and writing CSV files.
import google.generativeai as genai # Imports the google-generativeai library to interact with Gemini models.
import os # Imports the os library for interacting with the operating system, including environment variables.
import time # Imports the time library to add delays in execution.
from tqdm import tqdm # Imports the tqdm library for displaying progress bars in notebooks.

# Try to get the Google API key from the environment variable
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Check if the API key was successfully retrieved
if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY environment variable not found.") # Prints an error message if the environment variable is not set.
    print("Please set the GOOGLE_API_KEY environment variable before running the script.") # Provides instructions on how to set the variable.
    exit() # Stops the program execution if the API key is not found.

# Configure the Generative AI model
genai.configure(api_key=GOOGLE_API_KEY) # Configures the genai library with the API key from the environment variable.
model = genai.GenerativeModel('gemini-2.0-flash-lite')  # Creates an instance of the Gemini model 'gemini-2.0-flash-lite'.

def classify_genre(game_title, delay=2):  # Defines a function to classify the genre of a game with a default delay of 2 seconds.
    """Classifies the genre of a game title using the Gemini Pro model.""" # Docstring explaining the function.
    try:
        prompt = f"What is the primary single-word genre of the video game: '{game_title}'? Answer with only one word." # Creates a prompt to request the game genre.
        response = model.generate_content([prompt]) # Sends the prompt to the Gemini model and gets the response.
        if response.text: # Checks if the response contains text.
            time.sleep(delay) # Waits for the specified time (to avoid rate limits).
            return response.text.strip() # Removes leading and trailing whitespace from the response text and returns it.
        else: # If there is no text in the response.
            return None # Returns None.
    except Exception as e: # Catches any potential errors during the process.
        print(f"Error classifying genre for '{game_title}': {e}") # Prints an error message.
        return None # Returns None.

def generate_short_description(game_title, delay=2): # Defines a function to generate a short description of a game with a default delay of 2 seconds.
    """Generates a short description (under 30 words) for a game title.""" # Docstring explaining the function.
    try:
        prompt = f"Generate a very short description (under 30 words) for the video game: '{game_title}'." # Creates a prompt to request a short description.
        response = model.generate_content([prompt]) # Sends the prompt to the Gemini model and gets the response.
        if response.text: # Checks if the response contains text.
            time.sleep(delay) # Waits for the specified time (to avoid rate limits).
            return response.text.strip() # Removes leading and trailing whitespace from the response text and returns it.
        else: # If there is no text in the response.
            return None # Returns None.
    except Exception as e: # Catches any potential errors during the process.
        print(f"Error generating description for '{game_title}': {e}") # Prints an error message.
        return None # Returns None.

def determine_player_mode(game_title, delay=2): # Defines a function to determine the player mode of a game with a default delay of 2 seconds.
    """Determines the player mode (Singleplayer, Multiplayer, or Both) for a game title.""" # Docstring explaining the function.
    try:
        prompt = f"For the video game '{game_title}', is it primarily 'Singleplayer', 'Multiplayer', or 'Both'? Answer with only one of these three options." # Creates a prompt to request the player mode.
        response = model.generate_content([prompt]) # Sends the prompt to the Gemini model and gets the response.
        if response.text: # Checks if the response contains text.
            cleaned_response = response.text.strip().title() # Removes whitespace and capitalizes the first letter of each word.
            time.sleep(delay) # Waits for the specified time (to avoid rate limits).
            if cleaned_response in ["Singleplayer", "Multiplayer", "Both"]: # Checks if the cleaned response is one of the valid options.
                return cleaned_response # Returns the valid player mode.
            else: # If the response is not valid.
                return None # Returns None.
        else: # If there is no text in the response.
            return None # Returns None.
    except Exception as e: # Catches any potential errors during the process.
        print(f"Error determining player mode for '{game_title}': {e}") # Prints an error message.
        return None # Returns None.

def enhance_game_data(csv_filepath, output_filepath="enhanced_games.csv", delay_between_calls=2):
    """
    Loads game data from a CSV, enhances it with genre, description, and player mode
    using the Google AI Studio API, and saves the enhanced data to a new CSV with progress bars.
    """
    try:
        df = pd.read_csv(csv_filepath) # Reads the CSV file into a pandas DataFrame.
        print(f"Loaded data from: {csv_filepath}") # Prints a message indicating the data has been loaded.

        df['genre'] = [classify_genre(title, delay=delay_between_calls) for title in tqdm(df['game_title'], desc="Classifying Genres")] # Applies the classify_genre function with a progress bar.
        print("Genre classification complete.") # Prints a message indicating genre classification is complete.

        df['short_description'] = [generate_short_description(title, delay=delay_between_calls) for title in tqdm(df['game_title'], desc="Generating Descriptions")] # Applies the generate_short_description function with a progress bar.
        print("Short description generation complete.") # Prints a message indicating short description generation is complete.

        df['player_mode'] = [determine_player_mode(title, delay=delay_between_calls) for title in tqdm(df['game_title'], desc="Determining Player Modes")] # Applies the determine_player_mode function with a progress bar.
        print("Player mode determination complete.") # Prints a message indicating player mode determination is complete.

        df.to_csv(output_filepath, index=False) # Saves the enhanced DataFrame to a new CSV file without including the index.
        print(f"Enhanced data saved to: {output_filepath}") # Prints a message indicating the enhanced data has been saved.

    except FileNotFoundError: # Catches the error if the CSV file is not found.
        print(f"Error: CSV file not found at {csv_filepath}") # Prints an error message if the file is not found.
    except Exception as e: # Catches any unexpected errors during the process.
        print(f"An unexpected error occurred: {e}") # Prints an unexpected error message.

if __name__ == "__main__":
    csv_link = "Game Thumbnail.csv" # Defines the name of the CSV file to be processed.
    enhance_game_data(csv_link, delay_between_calls=2) # Calls the main function to enhance the game data with a delay between API calls.