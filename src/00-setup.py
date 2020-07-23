import os
import sys
from git import Repo

def get_folder_name(file):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def print_ts(code: int):
    import subprocess
    from datetime import datetime
    codes_dict = {1: "INF", 2: "WRN", 3: "ERR"}
    current_ts = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    user_print = subprocess.check_output(["whoami"]).decode("utf-8").split("\n")[0]
    output_string = "[ {0} - {1} ({2}) ]"
    return output_string.format(codes_dict.get(code), current_ts, user_print)

current_wd = os.getcwd()
new_wd = get_folder_name(__file__)
git_file = os.path.join(new_wd, "data")
git_url = "https://github.com/MinCiencia/Datos-COVID19.git"

if __name__ == "__main__":
    print(print_ts(code = 1), "Configurando el entorno.")
    print(print_ts(code = 1), "Obteniendo data del origen remoto...")
    try:
        print(print_ts(code = 1), "Clonando el repositorio de Git con la data original...")
        Repo.clone_from(git_url, git_file)
    except:
        print(print_ts(code = 3), "El directorio ya existe.")
        print(print_ts(code = 1), "Refrescando los datos...")
        try:
            Repo(git_file).remotes.origin.pull()
        except:
            print(print_ts(code = 3), "Error refrescando los datos.")
            print(print_ts(code = 3), "Saliendo del programa con código de error.")
            sys.exit(1)
print(print_ts(code = 1), "Datos refrescados.")
    