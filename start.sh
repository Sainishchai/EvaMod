if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/GouthamSER/EvaMod.git /EvaMod
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMod
fi
cd /EvaMod
pip3 install -U -r requirements.txt
echo "Starting Bot..🤞.."
python3 bot.py
