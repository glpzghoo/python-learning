sudo apt update
sudo apt install python3-venv pkg-config libdbus-1-dev libglib2.0-dev
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
