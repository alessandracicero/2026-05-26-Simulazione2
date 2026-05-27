import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDsRating(self):
        votiDD= self._model.getAllVoti()
        self._view._ddrating1.options=votiDD
        self._view._ddrating2.options=votiDD

    def handleCreaGrafo(self, e):
        pass

    def handleCammino(self, e):
        pass