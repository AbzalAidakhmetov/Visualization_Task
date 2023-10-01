import pandas as pd
import matplotlib.pyplot as plt
import os

class Plotter:
    def __init__(self, data_folder='/home/theballer/Desktop/DS_Learning/Pandas_Task/plots'):
        self.data_folder = data_folder
        os.makedirs(self.data_folder, exist_ok=True)

    def draw_plots(self, df):
        # Comparison between Ground Truth and Model Predicted Corners
        plt.figure(figsize=(8, 6))
        plt.scatter(df['gt_corners'], df['rb_corners'])
        plt.xlabel('Ground Truth Corners')
        plt.ylabel('Model Predicted Corners')
        plt.title('Comparison of Ground Truth vs. Model Predicted Corners')
        plt.savefig(os.path.join(self.data_folder, 'gt_vs_rb_corners.png'))
        plt.close()

        # Histograms of Deviation Columns
        deviation_columns = ['mean', 'max', 'min', 'floor_mean', 'floor_max', 'floor_min', 'ceiling_mean', 'ceiling_max', 'ceiling_min']
        for col in deviation_columns:
            plt.figure(figsize=(8, 6))
            plt.hist(df[col], bins=20, alpha=0.5)
            plt.xlabel(f'Deviation {col}')
            plt.ylabel('Frequency')
            plt.title(f'Histogram of Deviation {col}')
            plt.savefig(os.path.join(self.data_folder, f'histogram_{col}.png'))
            plt.close()

    def list_plot_paths(self):
        return [os.path.join(self.data_folder, file) for file in os.listdir(self.data_folder)]

