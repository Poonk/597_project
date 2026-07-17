.csv files must be in a folder named "flow_based" or "packet_based" respectively.

The folders must be in the project root next to helpers.py and PreprocessingPipeline.py

## Phase 1
- `helpers.py` — load, sample, preprocess
- `PreprocessingPipeline.py` — run Phase 1 on flow or packet data

## Phase 2
All Phase 2 code lives in `phase_2/`:
- `config.py` — paths, seeds
- `anomaly.py` — packet load / preprocess helpers
- `evaluation.py` — shared figure helpers
- `eda.py` — EDA plots
- `main_eda.py` — run EDA
- `main.py` — Phase 2 entry point
- `saved_figs/` — figures

```bash
source .venv/bin/activate
pip install -r requirements.txt
cd phase_2
python main_eda.py
python main.py
```

Or from the project root:

```bash
python phase_2/main_eda.py
python phase_2/main.py
```
