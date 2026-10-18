# =====================================================================
# THVE v2.0 SDK - Script de Empacotamento e Distribuição Protegida
# Author: Ricardo Dutra Pereira
# =====================================================================

import os
import subprocess
import sys

def build_distribution_package():
    print("======================================================================")
    print(" THVE v2.0 SDK - Compilação de Pacote de Distribuição (.whl)")
    print("======================================================================")

    setup_content = """from setuptools import setup, find_packages

setup(
    name='thve_sdk',
    version='2.0.0',
    packages=find_packages(),
    description='Topological High-Dimensional Vector Engine SDK',
    author='Ricardo Dutra Pereira',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
"""

    sdk_setup_path = os.path.join('thve_sdk', 'setup.py')
    if not os.path.exists(sdk_setup_path):
        with open(sdk_setup_path, 'w', encoding='utf-8') as f:
            f.write(setup_content)
        print("[+] Ficheiro setup.py gerado automaticamente no thve_sdk.")

    print("\n[+] A executar o empacotamento Wheel via setuptools...")

    os.chdir('thve_sdk')
    result = subprocess.run([sys.executable, 'setup.py', 'bdist_wheel'], capture_output=True, text=True)

    if result.returncode == 0:
        print("\n[SUCESSO] Pacote de distribuição Wheel compilado com sucesso!")
        print(result.stdout)
    else:
        print("\n[AVISO] Erro na compilação direta. Verifique se o setuptools está instalado:")
        print(result.stderr)

    os.chdir('..')
    print("======================================================================")

if __name__ == '__main__':
    build_distribution_package()