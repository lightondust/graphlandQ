from model import min_vertex_cover

def get_model(request_dict):
    if request_dict == 'min_vertex_cover':
        model = min_vertex_cover
    return model


def get_sampler(sampler_name):
    pass