python3 -m venv myproject_env
source myproject_env/bin/activate
deactivate 

pip3 install ipykernel (This lets your Python environment talk to Jupyter)


python3 -m ipykernel install --user --name=myproject_env --display-name "Python (My Project)"


--name=myproject_env → internal kernel name (can match your venv folder name).
--display-name "Python (My Project)" → the friendly name you’ll see in Jupyter’s kernel dropdown.

jupyter notebook
