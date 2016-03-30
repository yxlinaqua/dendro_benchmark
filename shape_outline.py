from scipy.weave import inline, converters

_code = open("outline.c", "r").read()

def outline(data, every):
    width, height = data.shape
    return inline(_code, ['data', 'width', 'height', 'every'], type_converters=converters.blitz)
