# graph_gen/video_generator.py
import matplotlib.pyplot as plt
from graph_gen.data_loader import load_data
from graph_gen.chart_animator import create_animation, save_animation

def generate_video_from_data(file_path, x_col, y_col, output_file, title_template):
    """
    Generate a video of an animated chart from a data file.
    
    Args:
    file_path (str): Path to the data file.
    x_col (str): Column name for the x-axis.
    y_col (str): Column name for the y-axis.
    output_file (str): Path to save the output video.
    title_template (str): Template for the title.
    """
    data = load_data(file_path)
    anim, fig = create_animation(data, x_col, y_col, title_template)
    save_animation(anim, output_file)
    plt.close(fig)
    return anim
