snap install aws-cli --classic
apt-get install python-pip -y
apt install python3-pip -y
rm -rf ./bot-panel
git clone https://github.com/yuyang-sharethis/bot-panel.git
rm -rf ./input
mkdir input
aws s3 cp --recursive s3://sharethis-datascience/bot_panel_input/ ./input/
