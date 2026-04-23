# Pandas

En enkel startmall for dataarbete med Python och Pandas.

## Kom igang

1. Skapa virtuell miljo:

```powershell
python -m venv .venv
```

2. Aktivera miljo i PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Installera paket:

```powershell
pip install -r requirements.txt
```

4. Kor demo-script:

```powershell
python -m src.main
```

5. Starta Jupyter Notebook (valfritt):

```powershell
jupyter notebook
```

Scriptet skapar filen `data/processed/scores.csv`.

## Struktur

- `src/` innehaller kod.
- `data/raw/` ar for indata (ignoreras i Git).
- `data/processed/` ar for bearbetad data (ignoreras i Git).
- `notebooks/` ar for Jupyter-notebooks.

## Notebooks

- `notebooks/01_quickstart.ipynb` for grundflode med import, analys och export.
- `notebooks/02_eda_visualisering.ipynb` for EDA med histogram, boxplot och sammanstallning.
- `notebooks/03_data_cleaning.ipynb` for data cleaning: saknade varden, dubbletter, typkonvertering och outlier-filtrering.
- `notebooks/04_feature_engineering_model.ipynb` for feature engineering, modelltraning och utvardering.
