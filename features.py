def create_features(df):

    df = df.copy()

    CURRENT_YEAR = 2026

    df["car_age"] = (
        CURRENT_YEAR - df["year"]
    ).clip(lower=0)

    df["mileage_per_year"] = (
        df["mileage"] /
        (df["car_age"] + 1)
    )

    return df