import numpy as np
from sympy import Matrix

class MatrixOperations:
    @staticmethod
    def add_matrices(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        # Sumar dos matrices numpy #
        return np.add(a, b)
        
    @staticmethod
    def multiply_matrices(a: np.ndarray, b: np.ndarray) -> np.ndarray:
        # Multiplicar dos matrices #
        return np.matmul(a, b)
    
    @staticmethod
    def determinate(matrix: np.ndarray) -> float:
        # Calcula determinante de una matriz #
        return np.linalg.det(matrix)
    
    @staticmethod
    def inverse(matrix: np.ndarray) -> np.ndarray:
        # Calcular inversa de una matiz #
        return np.linalg.inv(matrix)
    
    @staticmethod
    def eigenvalues(matrix: np.ndarray) -> tuple:
        # Calcula valores y vectores propios #
        return np.linalg.eig(matrix)
    
    @staticmethod
    def symbolic_matrix(rows: int, columns: int) -> Matrix:
        # Crar una matriz simbólica #
        return Matrix(rows, columns, lambda i,j: 0)