from tokenize import Double


class Matrix:

    def __init__(self, row, colum):
        self.row = row
        self.column = colum
        self.L = []
        self.U = []
        self.matrix = []
        self.__ID = None

    def getRows(self) -> int:
        return self.row

    def getColumns(self) -> int:
        return self.column

    def getElement(self, row, column) -> Double:
        return self.matrix[row][column]

    """
        Returns the specified matrix
    """

    def getMatrix(self) -> list:
        return self.matrix

    def addElement(self, row, column, element) -> None:
        self.matrix[row][column] = element

    def showMatrix(self) -> None:
        for i in self.matrix:
            for j in i:
                print(j, end=" ")
            print()
