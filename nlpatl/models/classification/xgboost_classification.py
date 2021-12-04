try:
	from xgboost import XGBClassifier
except ImportError:
	# No installation required if not using this function
	pass

from nlpatl.models.classification import SkLearnClassification


class XGBoostClassification(SkLearnClassification):
	"""
		:param str model_name: xgboost classification model name
		:param dict model_config: Custom model paramateters
		:param str name: Name of this classification

		>>> import nlpatl.models.classification as nmcla
		>>> model = nmcla.XGBoostClassification()
    """

	def __init__(self, model_name: str = 'xgboost', model_config: dict = {}, 
		name: str = 'sklearn'):

		super().__init__(name=name)

		self.model_name = model_name
		self.model_config = model_config

		self.model = XGBClassifier(**model_config)

	@staticmethod
	def get_mapping() -> dict:
		return MODEL_FOR_SKLEARN_CLASSIFICATION_MAPPING_NAMES