from flask import request, jsonify
from src.security.filterStructure.filter import Filter


class Controller:

    def __init__(self, controller):
        self.__controller = controller

    def requestHandler(self):
        method = request.method

        if method == "GET":
            return self.__get()
        elif method == "POST":
            return self.__post()

    def __get(self):
        return self.__controller.Get().handler()

    def __post(self):
        if not Filter.postRequestCompatibility(self.__controller):
            return jsonify(None)
            
        return self.__controller.Post().handler()
