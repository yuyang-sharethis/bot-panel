echo "Launching instance..."
instance_id=$(aws ec2 run-instances --launch-template LaunchTemplateId=lt-03c44e86240b9f390,Version=1 | jq -r '.Instances[0].InstanceId')
echo "Saving instance config..."
aws ec2 describe-instances --filters Name=instance-id,Values=$instance_id > /tmp/bot.txt
public_dns=$(cat /tmp/bot.txt | grep PublicDnsName | tail -1 | awk -F'"' '{print $4}')
echo "Waiting for instance launching..."
sleep 40
echo "SSH into $instance_id through $public_dns"
ssh -o "StrictHostKeyChecking no" -i "bot_panel.pem" ubuntu@$public_dns