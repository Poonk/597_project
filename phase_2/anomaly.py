from config import (
    PACKET_PATH,
    LABEL_COL,
    BENIGN_LABEL,
    IDENTIFIER_KEYWORDS,
    RANDOM_SEED,
)
from helpers import (
    load_csv,
    shuffle_and_segregate,
    feature_cleaner,
    log_and_scale,
)


def prepare_packet_data(path=PACKET_PATH, seed=RANDOM_SEED):
    # Load, sample, preprocess packet-level data (Phase 1 pipeline)
    df_combined_sampled = load_csv(path)
    df_features, labels = shuffle_and_segregate(df_combined_sampled, seed=seed)
    df_numeric, df_identifiers = feature_cleaner(df_features)
    df_preprocessed, fitted_scaler = log_and_scale(df_numeric, df_identifiers, labels)
    return df_preprocessed, fitted_scaler


def get_identifier_columns(df):
    # Find columns that identify a machine or user
    identifier_cols = []
    for col in df.columns:
        words = col.lower().replace(' ', '_').replace('-', '_').split('_')
        if any(keyword in words for keyword in IDENTIFIER_KEYWORDS):
            identifier_cols.append(col)
    return identifier_cols


def split_features_and_labels(df_preprocessed, label_col=LABEL_COL):
    # Keep identifiers aside; train only on scaled numeric behaviour features
    labels = df_preprocessed[label_col].copy()
    identifier_cols = get_identifier_columns(df_preprocessed)
    drop_cols = [label_col] + [c for c in identifier_cols if c in df_preprocessed.columns]
    x_features = df_preprocessed.drop(columns=drop_cols)
    # Binary ground truth for evaluation only (not used in unsupervised training)
    y_true = (labels != BENIGN_LABEL).astype(int)
    return x_features, labels, y_true, identifier_cols
