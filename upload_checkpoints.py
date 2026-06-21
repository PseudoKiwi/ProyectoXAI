from huggingface_hub import HfApi, login
import glob
import os

HF_USERNAME = "Pseudokiwi"
DATASET = "imdb"
REPO_NAME = f"Proyecto_XAI_checkpoints_{DATASET}"
REPO_ID = f"{HF_USERNAME}/{REPO_NAME}"
CHECKPOINTS_DIR = f"../checkpoints/{DATASET}"

login()

api = HfApi()

print(f"Creando repositorio {REPO_ID} ...")
api.create_repo(repo_id=REPO_ID, repo_type="model", private=True, exist_ok=True)

archivos = glob.glob(os.path.join(CHECKPOINTS_DIR, "*.pt"))
if not archivos:
    print("No se encontraron archivos .pt en la carpeta checkpoints.")
    exit(1)

print(f"Se encontraron {len(archivos)} modelos. Iniciando subida...\n")

for path in archivos:
    nombre = os.path.basename(path)
    print(f"Subiendo {nombre} ...")
    api.upload_file(
        path_or_fileobj=path,
        path_in_repo=nombre,
        repo_id=REPO_ID,
        repo_type="model",
    )
    print(f"  OK: {nombre}\n")

print("Todos los modelos fueron subidos exitosamente.")
print(f"Repositorio: https://huggingface.co/{REPO_ID}")
