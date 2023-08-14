# copy following line to /.bashrc

sudo snap install aws-cli --classic
sudo apt-get install python-pip -y
sudo apt install python3-pip -y
sudo pip install selenium==4.9.1
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add 
sudo bash -c "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list" 
sudo apt -y update 
sudo apt -y install google-chrome-stable 
rm -rf ./bot-panel
git clone https://github.com/yuyang-sharethis/bot-panel.git
rm -rf ./input
mkdir input
aws s3 cp --recursive s3://sharethis-datascience/bot_panel_input/ ./input/

