import pprint


def introspection_info(obj):
    type_info = type(obj).__name__
    attributes_info = dir(obj)
    methods_info = [attr for attr in attributes_info if callable(getattr(obj, attr))]
    module_info = obj.__module__ if hasattr(obj, '__module__') else None
    info = {
        'type': str(type_info),
        'attributes': attributes_info,
        'methods': methods_info,
        'module': module_info
    }
    return info


number_info = introspection_info(42)
print(number_info)
