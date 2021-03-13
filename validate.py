

def validate_float(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if value_if_allowed:
        try:
            float(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return True


def validate_int(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if value_if_allowed:
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    else:
        return True
