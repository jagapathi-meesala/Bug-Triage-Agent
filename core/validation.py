def require_dict(payload):
    if not isinstance(payload, dict):
        raise ValueError("Input must be a JSON object")

def require_nonempty_string(payload, key):
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"'{key}' must be a non-empty string")

def optional_string(payload, key):
    value = payload.get(key)
    if value is not None and not isinstance(value, str):
        raise ValueError(f"'{key}' must be a string when provided")
