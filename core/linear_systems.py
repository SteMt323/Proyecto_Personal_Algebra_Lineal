import numpy as np
from sympy import symbols, Eq, solve

class LinearSystems:
    @staticmethod
    def solve_system(coefficients: np.ndarray, constants: np.ndarray) -> np.ndarray:
        # Resolver sistema se ecuaciones linealaes #
        return np.linalg.solve(coefficients, constants)
    
    @staticmethod
    def symbolic_solution(variables: int):
        # Generar solución simbólica para un sistema de ecuaciones #
        sym_vars = symbols(f"x:{variables}")
        equations = []
        
        for i in range(variables):
            eq = sum(sym_vars) - (i + 1)*3
            equations.append(Eq(eq, 0))
            
        return solve(equations, sym_vars)