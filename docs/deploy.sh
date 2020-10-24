set -eu
source ~/venv_sec/bin/activate
python generate.py
git add *
git commit
git push

