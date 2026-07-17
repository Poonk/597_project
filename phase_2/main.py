from anomaly import prepare_packet_data, split_features_and_labels


def main():
    # Prepare packet-level sample and preprocess
    print('Preparing packet data')
    df_preprocessed, fitted_scaler = prepare_packet_data()

    # Split behaviour features from labels / identifiers
    print('Splitting features and labels')
    x_features, labels, y_true, identifier_cols = split_features_and_labels(df_preprocessed)
    print(f'Feature matrix: {x_features.shape}, identifiers held out: {len(identifier_cols)}')
    return


# Call the main function
if __name__ == '__main__':
    main()
