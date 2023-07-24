snap install aws-cli --classic
apt-get install python-pip -y
apt install python3-pip -y

web_driver_path=$(pwd)/chromedriver
CHROME_USER_DATA_PATH=$(pwd)/chrome_user_data

python3 bot.py $web_driver_path $CHROME_USER_DATA_PATH