echo "Launching instance..."
aws ec2 start-instances --instance-ids i-0980565bcf5d16d2e
echo "Saving instance config..."
aws ec2 describe-instances --filters Name=instance-id,Values=i-0980565bcf5d16d2e > /tmp/bot.txt
public_dns=$(cat /tmp/bot.txt | grep PublicDnsName | tail -1 | awk -F'"' '{print $4}')
echo "Waiting for instance launching...(this will take ~60s)"
sleep 60
echo "SSH into bot panel: 'i-0980565bcf5d16d2e' through '$public_dns'"
chmod 400 bot_panel.pem
ssh -o "StrictHostKeyChecking no" -i "bot_panel.pem" ubuntu@$public_dns

