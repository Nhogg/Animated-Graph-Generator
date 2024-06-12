# graph_gen/chart_animator.py
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

def create_animation(data, x_col, y_col, title_template):
    """
    Create an animated chart from the data and return the animation object.
    
    Args:
    data (pd.DataFrame): DataFrame containing the data.
    x_col (str): Column name for the x-axis.
    y_col (str): Column name for the y-axis.
    title_template (str): Template for the title.
    
    Returns:
    FuncAnimation: The animation object.
    """
    fig, ax = plt.subplots()
    
    def update(frame):
        ax.clear()
        ax.plot(data[x_col][:frame+1], data[y_col][:frame+1])
        ax.set_xlim(data[x_col].min(), data[x_col].max())
        ax.set_ylim(data[y_col].min(), data[y_col].max())
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        title = title_template.format(time=data[x_col].iloc[frame], value=data[y_col].iloc[frame])
        ax.set_title(title)
    
    anim = FuncAnimation(fig, update, frames=len(data), repeat=False)
    return anim, fig

def save_animation(anim, output_file):
    """
    Save the animation to a file.
    
    Args:
    anim (FuncAnimation): The animation object.
    output_file (str): Path to save the output video.
    """
    writer = FFMpegWriter(fps=10, codec='libx264', extra_args=['-vcodec', 'libx264'])
    anim.save(output_file, writer=writer, savefig_kwargs={'transparent': True})
    print(f"Animation saved successfully to {output_file}")
