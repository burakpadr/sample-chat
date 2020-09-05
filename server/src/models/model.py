from src.database.mongodb import MongoDB


class Model:

    def __init__(self, model, attrs):
        self.__model = model
        self.__attrs = attrs

        self.__collectionConnection = MongoDB(model.__class__.__name__)

    def create(self):
        fields = self.__model.Meta.fields

        for field in fields:
            if not self.__attrs.__contains__(field):
                raise AttributeError(
                    f"There properties -> {fields} must be in the {self.__model.__class__.__name__} model!")

        self.__collectionConnection.create(self.__attrs)

    def read(self):
        return self.__collectionConnection.read(self.__attrs)

    def update(self, **kwargs):
        return self.__collectionConnection.update(self.__attrs, kwargs)

    def delete(self):
        return self.__collectionConnection.delete(self.__attrs)

    def isExistModel(self):
        return len(self.read()) > 0

    def readFirst(self):
        return self.read()[0]
