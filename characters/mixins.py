class SerializeByMethodMixin:
    def get_serializer_class(self, *agrs, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)
