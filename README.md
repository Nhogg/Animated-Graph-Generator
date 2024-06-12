📊 Animated Chart Video Generator
Create stunning animated chart videos from your data files with ease! 🎥✨

Features
📈 Supports CSV and Excel Files: Load data from both CSV and Excel files.
🎥 Generate Animated Chart Videos: Create smooth animations of your data over time.
🖼️ Customizable Titles: Add dynamic titles to your animations.
💻 Easy-to-Use GUI: Intuitive graphical user interface for seamless operation.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/animated-chart-video-generator.git
cd animated-chart-video-generator
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure ffmpeg is installed and in your PATH:

Download ffmpeg from FFmpeg Download Page
Extract and add the bin folder to your PATH
Usage
Using the GUI
Run the GUI:

bash
Copy code
python gui.py
Use the interface:

Browse and select your input file (CSV or Excel).
Enter the column names for the X and Y axes.
Customize your title template (e.g., {time} - Value: {value}).
Browse and select the output file path.
Click the "Generate" button to create your animated chart video!
Example
python
Copy code
from graph_gen import generate_video_from_data

# Generate video from data
generate_video_from_data(
    'path/to/data.csv',  # Input file
    'Time',              # X column
    'Value',             # Y column
    'output.mp4',        # Output file
    '{time} - Value: {value}'  # Title template
)
Screenshots
