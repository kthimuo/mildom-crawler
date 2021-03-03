class InitializerModel:

    def __init__(self, arr=None):
        self._data = {}
#        if props is not None and len(props) > 0:
        self._init(arr)

    def _init(self, arr):
        """
        :param props: props array
        :return: None
        """
#        for key in props.keys():
        self._init_properties_custom(arr)
