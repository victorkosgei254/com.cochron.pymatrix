from objs.AnimalBuilder import AnimalBuilder
from objs.MatrixBuilder import MatrixBuilder
"""
Entry point of a python application
"""
if __name__ == '__main__':
    print("Hello python still rem Me :)")
    a = MatrixBuilder().dimensions(3, 3).addID(
        "A").addRow(1, 2, 3, 4, 5).addRow(6, 7, 8, 9, 10).build()
    a.showMatrix()
