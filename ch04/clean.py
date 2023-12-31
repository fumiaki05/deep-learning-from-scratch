#pip install nbclean
# input_file = "./ch04_note-Copy1.ipynb"
# output_file = "./ch04_note-out.ipynb"

# cleaner = nbclean.clean.NotebookCleaner(input_file)
# cleaner.clear("output")
# cleaner.save(output_file)


import json

def remove_outputs(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    for cell in notebook['cells']:
        if 'outputs' in cell:
            cell['outputs'] = []

    with open(notebook_path, 'w') as f:
        json.dump(notebook, f, indent=4)

# notebook_pathをコピーしたNotebookのパスに置き換えてください。
notebook_path = 'ch04_note-Copy1.ipynb'
remove_outputs(notebook_path)