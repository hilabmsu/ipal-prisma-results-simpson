import matplotlib.pyplot as plt
import random

def pirate_plot(score_series_per_condition, condition_labels, title, ylabel, output_path=None):
    '''
    Creates a pilot plot with a box plot overlay and labeled outliers.
    :param score_series_per_condition:    a dataframe os summary statistics for each observation by category
    :param condition_labels: category labels for the x-axis
    :param title:   the plot title
    :param ylabel:  text label for the y-axis
    :param output_path: Provide a custom path for saving a PNG file of the figure. Leave blank to use default path.
    :return:
    '''
    fig, ax = plt.subplots()

    score_arrays = [series.values for series in score_series_per_condition]

    ax.violinplot(score_arrays, positions=range(1, len(condition_labels) + 1),
                  showmeans=True, showmedians=False, showextrema=False)
    ax.boxplot(score_arrays, tick_labels=condition_labels)

    for i, series in enumerate(score_series_per_condition):
        jitter = 0.05
        jitter_x_positions = [i + 1 + random.uniform(-jitter, jitter) for _ in series]
        ax.scatter(jitter_x_positions, series.values, color='black', s=4, alpha=0.6, zorder=2)

        # Label outliers using the same rule as the boxplot whiskers
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        for jittered_x, (participant_id, score) in zip(jitter_x_positions, series.items()):
            if score < lower_fence or score > upper_fence:
                ax.annotate(f"{participant_id}", (jittered_x, score),
                            xytext=(6,0),
                            textcoords='offset points',
                            fontsize=8,
                            va='center')

    ax.set_title(title)
    ax.set_ylabel(ylabel)

    if output_path:
        plt.savefig(output_path, bbox_inches='tight')

    plt.show()
    plt.close(fig)
