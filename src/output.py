import config

def ensure_output_dirs():
    config.FIGURES_PATH.mkdir(parents=True, exist_ok=True)
    config.MARKDOWN_PATH.mkdir(parents=True, exist_ok=True)
    config.LATEX_PATH.mkdir(parents=True, exist_ok=True)

def save_markdown(df, filename, index=False):
    path = config.MARKDOWN_PATH / filename
    with open(path, 'w') as f:
        f.write(df.to_markdown(index=index))
    # print(f"Markdown saved to {path}")

def save_latex(df, filename, caption=None, label=None, index=False):
    path = config.LATEX_PATH / filename
    with open(path, 'w') as f:
        f.write(df.to_latex(
            index=index,
            float_format="%.2f",
            caption=caption,
            label=label
        ))
    # print(f"LaTeX save to {path}")