from feature_engine.encoding import OneHotEncoder, RareLabelEncoder
from feature_engine.imputation import (
    AddMissingIndicator,
    CategoricalImputer,
    MeanMedianImputer,
)
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from classification_model.config.core import config
from classification_model.processing import features as pp

titanic_pipe = Pipeline(
    [
        # ===== IMPUTATION =====
        # impute categorical variables with string 'missing'
        (
            "categorical_imputation",
            CategoricalImputer(
                imputation_method="missing",
                variables=config.model_config.categorical_vars_with_na_missing,
                fill_value="missing",
                ignore_format=True,
            ),
        ),
        # add missing indicator to numerical variables
        (
            "missing_indicator",
            AddMissingIndicator(variables=config.model_config.numerical_vars_with_na),
        ),
        # impute numerical variables with the median
        (
            "median_imputation",
            MeanMedianImputer(variables=config.model_config.numerical_vars_with_na),
        ),
        # Extract first letter from cabin
        (
            "extract_letter",
            pp.ExtractLetterTransformer(
                variables=config.model_config.cabin_var_imputation
            ),
        ),
        # == CATEGORICAL ENCODING ======
        # remove categories present in less than 5% of the observations (0.05)
        # group them in one category called 'Rare'
        (
            "rare_label_encoder",
            RareLabelEncoder(
                tol=0.05,
                n_categories=1,
                variables=config.model_config.categorical_vars,
                replace_with="Rare",
                ignore_format=True,
            ),
        ),
        # encode categorical variables using one hot encoding into k-1 variables
        (
            "categorical_encoder",
            OneHotEncoder(
                variables=config.model_config.categorical_vars, drop_last=True
            ),
        ),
        # scale using standardization
        ("scaler", StandardScaler()),
        # logistic regression (use C=0.0005 and random_state=0)
        ("Logit", LogisticRegression(C=0.0005, random_state=0)),
    ]
)
