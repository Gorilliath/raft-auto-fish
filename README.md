## Prerequisites

- Python
- `pip install -r requirements.txt`

## Usage

- Start the program in a terminal with `py main.py`
- Cast the fishing line
- The program will then catch and re-cast the line forever
- Hold the `esc` key to stop the program

## Note

- The portion of the game where the target image is displayed needs to be visible

- `pyautogui.locateOnScreen` will not handle disparate target and source images; If you're rendering the game with different resolutions you will need to update the target image accordingly
