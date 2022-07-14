dpkg -s python3-venv
var="$?"
echo $var
if [ $var != "0" ]; then
    sudo apt install -y python3-venv
fi
python3 -m venv ../py-env
source ../py-env/bin/activate
pip3 install -r ../requirements.txt
pip3 freeze
