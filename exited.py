import tensorflow as tf

LABEL_KEY = "Exited"

# Helper untuk ubah nama kolom biar aman (hapus spasi)
def transformed_name(key):
    return key.replace(" ", "_") + "_xf"

NUMERIC_FEATURE_KEYS = [
    "CreditScore", "Age", "Tenure", "Balance", "NumOfProducts",
    "EstimatedSalary", "Satisfaction Score", "Point Earned"
]

BINARY_KEYS = ["HasCrCard", "IsActiveMember", "Complain"]

def preprocessing_fn(inputs):
    outputs = {}

    # Numeric features
    for key in NUMERIC_FEATURE_KEYS:
        safe_key = key.replace(" ", "_")
        outputs[transformed_name(key)] = tf.cast(inputs[key], tf.float32)

    # Binary features
    for key in BINARY_KEYS:
        outputs[transformed_name(key)] = tf.cast(inputs[key], tf.int64)

    # Label
    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)

    return outputs
