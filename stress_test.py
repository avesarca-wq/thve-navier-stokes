# =====================================================================
# THVE v2.0: Automated Stress Test & Boundary Validation Suite
# Author: Ricardo Dutra Pereira
# =====================================================================

import sys
import math

sys.path.append('.')
from thve_sdk.core.engine import THVECoreEngine

def run_stress_test_suite():
    print("======================================================================")
    print(" THVE v2.0 SDK - Suite de Testes de Stress e Carga Extrema")
    print(" Alvo: Validação de Limites e Estabilidade sob Turbulência Catastrófica")
    print("======================================================================")
    
    engine = THVECoreEngine()
    
    # Cenários de teste extremos (incluindo valores massivos e picos singulares)
    scenarios = [
        ("Cenário A: Turbulência Padrão", [105.4, -89.2, 314.15, -0.005, 512.0]),
        ("Cenário B: Picos de Alta Amplitude", [1e6, -2.5e7, 9.87e8, -1.2e-4, 5.5e5]),
        ("Cenário C: Oscilações Próximas de Zero", [0.00001, -0.000002, 0.00005, -0.000001, 0.00008]),
        ("Cenário D: Assimetria Extrema Positivo/Negativo", [999999.99, -999999.99, 123456.78, -87654.32, 555555.55])
    ]
    
    success_count = 0
    
    for name, vector in scenarios:
        print(f"\n[Executando] {name}")
        print(f"  -> Entrada: {vector}")
        try:
            result = engine.optimize_vector(vector)
            print(f"  -> Saída Estabilizada: {result['stable_output']}")
            print(f"  -> Status Topológico: {result['status']}")
            if result['status'] == 'OPTIMIZED':
                print(f"  [SUCESSO] Contenção validada para {name}.")
                success_count += 1
            else:
                print(f"  [ALERTA] Status inesperado.")
        except Exception as e:
            print(f"  [ERRO CRÍTICO] Falha na execução: {e}")
            
    print("\n======================================================================")
    print(f" Relatório Final: {success_count}/{len(scenarios)} cenários aprovados com sucesso absoluto.")
    print("======================================================================")

if __name__ == "__main__":
    run_stress_test_suite() 