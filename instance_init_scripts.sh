# copy following line to /.bashrc

sudo apt-get update
sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4
# aws cli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# python & selenium
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y
sudo apt install python3-selenium

# chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -f
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
sudo dpkg -i google-chrome-stable_current_amd64.deb

# bot-panel & input
sudo apt install git -y
rm -rf ./bot-panel
git clone https://github.com/yuyang-sharethis/bot-panel.git
rm -rf ./input
mkdir input
aws s3 cp --recursive s3://sharethis-datascience/bot_panel_input/ ./input/
cd bot-panel/
