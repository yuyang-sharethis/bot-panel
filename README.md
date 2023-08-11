0. NEVER TERMINATE A INSTANCE! JUST STOP THE INSTANCE WHENEVER BOT FINISH TASK.

1. for the first time running bot panel, you should download ssh private key from AWS Secret Manager and make a plain text file "bot_panel.pem" under this bot_panel folder. The secret in AWS Secret Manager is call "bot_panel.pem".

2. on local machine, run "bot_init.sh", it will take to the remote instance and kick off the bot automatically

enjoy :)
