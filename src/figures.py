import matplotlib.pyplot as plt
import random

def bar_chart(values, labels, title, ylabel, output_path=None):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, 100)

    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()

    plt.close(fig)

def pirate_plot(data, labels, title, ylabel, output_path=None):
    fig, ax = plt.subplots()

    ax.violinplot(data, positions=range(1, len(labels) + 1),
                  showmeans=False, showmedians=False, showextrema=False)
    ax.boxplot(data, tick_labels=labels)

    for i, scores in enumerate(data):
        jitter = 0.05
        x = [i + 1 + random.uniform(-jitter, jitter) for _ in scores]
        ax.scatter(x, scores, color='black', s=4, alpha=0.6, zorder=2)

    ax.set_title(title)
    ax.set_ylabel(ylabel)

    if output_path:
        plt.savefig(output_path, bbox_inches='tight')
    else:
        plt.show()

    plt.close(fig)

def violin_plot(data, labels, title, ylabel, output_path=None):
    fig, ax = plt.subplots()
    ax.violinplot(data, positions=range(len(labels)))

    # overlay individual data points with jitter
    for i, scores in enumerate(data):
        jitter = 0.05  # controls how far points spread horizontally
        x = [i + random.uniform(-jitter, jitter) for _ in scores]
        ax.scatter(x, scores, color='black', s=4, alpha=0.6, zorder=2)

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_title(title)
    ax.set_ylabel(ylabel)

    if output_path:
        plt.savefig(output_path, bbox_inches='tight')
    else:
        plt.show()

    plt.close(fig)