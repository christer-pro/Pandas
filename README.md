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

Scriptet skapar filen `data/processed/scores.csv`.

## Struktur

- `src/` innehaller kod.
- `data/raw/` ar for indata (ignoreras i Git).
- `data/processed/` ar for bearbetad data (ignoreras i Git).
- `notebooks/` ar for Jupyter-notebooks.
