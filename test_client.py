import sys
sys.path.append(".")
from thve_sdk.core.engine import THVECoreEngine
engine = THVECoreEngine()
print("Resultado:", engine.optimize_vector([3.14, -4.5, 2.1, 0.0, 5.0]))
