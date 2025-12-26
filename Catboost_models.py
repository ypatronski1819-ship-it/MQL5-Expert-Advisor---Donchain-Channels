from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score

from onnx.helper import get_attribute_value
from skl2onnx import convert_sklearn, update_registered_converter
from sklearn.pipeline import Pipeline
