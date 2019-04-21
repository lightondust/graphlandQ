from models.min_vertex_cover import min_vertex_cover
from models.maximum_cut import maximum_cut
from models.maximum_independent_set import maximum_independent_set

model_map = {
    'min_vertex_cover': min_vertex_cover,
    'maximum_cut': maximum_cut,
    'maximum_independent_set': maximum_independent_set
}


def get_model(model_name):
    return model_map[model_name]

