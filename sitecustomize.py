# This script is meant to automatically call conda-unpack whenever the python executable is run
# copy this file to YourCondaEnv/lib/python3.X/site-packages/ (substitute X with the correct python version)
import os
import time

# current dir should be "site-packages"
curr_dir = os.path.dirname(os.path.abspath(__file__))
python_dir = os.path.abspath(os.path.join(curr_dir, os.pardir))
lib_dir = os.path.abspath(os.path.join(python_dir, os.pardir))
env_dir = os.path.abspath(os.path.join(lib_dir, os.pardir))
conda_unpack = os.path.join(os.path.join(env_dir, "bin"), "conda-unpack")

run_file = os.path.join(curr_dir, "conda-unpack.running")
done_file = os.path.join(curr_dir, "conda-unpack.done")
if not os.path.exists(conda_unpack):
    print("conda-unpack does not exists; skipping auto-unpack")
elif os.path.exists(run_file) and not os.path.exists(done_file):
    print("conda-unpack is already running; waiting for it to finish...")
    while not os.path.exists(done_file):
        time.sleep(1)
    print("conda-unpack already done; skipping auto-unpack")
elif os.path.exists(done_file):
    print("conda-unpack already done; skipping auto-unpack")
else:
    print("unpacking with conda-unpack...")
    os.system("chmod +w -R ./././*")
    with open(run_file, 'a'):
        os.utime(run_file, None)
    os.system(conda_unpack)
    with open(done_file, 'a'):
        os.utime(run_file, None)
    print("conda-unpack done")
