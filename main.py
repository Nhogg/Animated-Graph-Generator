# main.py
from graph_gen import generate_video_from_data

# Generate the video and keep the animation object in scope
anim = generate_video_from_data('C:/Users/natha/OneDrive/Desktop/graph-gen/graph_gen/data.csv', 'Time', 'Value', 'output.mp4')
