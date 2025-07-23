import os
import platform
import subprocess
import psutil  # Você precisará instalar este módulo: pip install psutil

def fechar_todos_apps():
    sistema = platform.system()
    
    if sistema == 'Windows':
        try:
            # Fecha aplicativos um por um (exceto processos críticos do sistema)
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    nome_processo = proc.info['name'].lower()
                    # Lista de processos do sistema que não devem ser fechados
                    processos_protegidos = {
                        'system', 'svchost.exe', 'wininit.exe', 'winlogon.exe',
                        'csrss.exe', 'services.exe', 'lsass.exe', 'explorer.exe'
                    }
                    
                    if nome_processo not in processos_protegidos and not nome_processo.startswith('python'):
                        proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
            
            print("Todos os aplicativos foram fechados com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao fechar os aplicativos: {e}")
    else:
        print("Este script só funciona no Windows no momento.")

if __name__ == "__main__":
    confirmacao = input("Tem certeza que deseja fechar TODOS os aplicativos? (s/n): ").lower()
    if confirmacao == 's':
        fechar_todos_apps()
    else:
        print("Operação cancelada.")