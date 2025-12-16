FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

RUN sudo apt update
RUN sudo apt install python3 -y
RUN sudo apt install pip -y
RUN python3 -m venv venv
RUN source /venv/bin/activate
RUN pip install -r requirements.txt
RUN deactivate