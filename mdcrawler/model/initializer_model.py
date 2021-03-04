class InitializerModel:
    def __init__(self, arr=None, prop=None):
        self._init(arr,prop)
    def _init(self, arr, prop):
        """
        :param props: props array
        :return: None
        """
        self._init_properties_custom(arr,prop)
