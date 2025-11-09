# This repo holds the files for an offline TTS conversational DadJoke AI.

# This project is a work in progress 🔃

# Folder structure
```
├─ .gitignore
├─ README.md
├─ data
│  ├─ cleaned
│  │  └─ dad_jokes.csv
│  ├─ merged
│  │  └─ dad_jokes.csv
│  └─ raw
│     ├─ test_raw.csv
│     └─ train_raw.csv
├─ db
├─ main.py
├─ requirements.txt
└─ src
   ├─ __init__.py
   ├─ config
   │  └─ paths.py
   ├─ data_utils
   │  ├─ downloader.py
   │  ├─ merger.py
   │  └─ preprocessor.py
   ├─ embedding
   │  └─ embedder.py
   └─ utils
      ├─ dataset_loader.py
      ├─ model_loader.py
      └─ setup_dirs.py
```