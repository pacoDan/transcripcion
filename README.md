install en linux
```sh
conda create -n whisper -y
conda activate whisper
conda install pip -y
pip install -U openai-whisper
```
sino primero antes:
```sh
conda config --set always_yes true
```
para borrar el entorno y las dependencias:
```sh
conda remove --name whisper --all -y # Eliminar el entorno y sus paquetes asociados
conda clean --all -y # Limpiar el caché de Conda (Crucial para recuperar espacio)

```
https://github.com/openai/whisper#:~:text=pip%20install%20setuptools%2Drust

ver luego:
https://github.com/jhdeov/whisper-to-textgrid-batch/
https://github.com/benmaster82/writher
