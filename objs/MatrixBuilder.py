from typing_extensions import Self
from objs.Matrix import Matrix


class MatrixBuilder:
    def __init__(self) -> Matrix:
        self.matrix = None
        self.row = None
        self.column = None

    def dimensions(self, row, column) -> Self:
        self.matrix = Matrix(row, column)
        self.row = row
        self.column = column
        return self

    def addID(self, id) -> Self:
        self.matrix.__ID = id
        return self

    def addRow(self, *args):
        data = []
        for i in args:
            data.append(i)
        self.matrix.matrix.append(data[:self.row])
        return self

    def build(self):
        matix = self.matrix
        return matix
