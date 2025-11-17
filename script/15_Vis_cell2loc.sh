#!/bin/bash -l
#SBATCH --job-name=cell2loc01_job
#SBATCH --qos=g-a100-2
#SBATCH --partition=a100
#SBATCH --gres=gpu:a100:1
#SBATCH --time=3-00:00:00
#SBATCH --output=cell2loc01_job.out
#SBATCH --error=cell2loc01_job.err


source "$(conda info --base)/etc/profile.d/conda.sh"

conda activate cell2loc

export LD_LIBRARY_PATH="$CONDA_PREFIX/lib:$CONDA_PREFIX/lib64:${LD_LIBRARY_PATH}"
export LD_PRELOAD="$CONDA_PREFIX/lib/libstdc++.so.6${LD_PRELOAD:+:$LD_PRELOAD}"

echo "PYTHON=$(which python)"
echo "CONDA_PREFIX=$CONDA_PREFIX"
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH"
strings "$CONDA_PREFIX/lib/libstdc++.so.6" | grep -E 'GLIBCXX_3\.4\.29' || echo "!! conda libstdc++에 GLIBCXX_3.4.29 없음"

python - <<'PY'
import importlib, subprocess, sys
print("Python:", sys.executable)
import pandas._libs.window.aggregations as m
print("agg so:", m.__file__)
subprocess.run(["ldd", m.__file__], check=False)
PY

python spatial_cell2loc_model_post.py

