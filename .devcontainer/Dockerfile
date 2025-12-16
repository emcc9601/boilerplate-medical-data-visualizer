FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# use this Dockerfile to install additional tools you might need, e.g.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

sudo apt update
sudo apt install python3 -y
sudo apt install pip -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate