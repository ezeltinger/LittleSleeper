source py-env/bin/activate
echo "Starting Little Sleeper audio"
nohup python3 audio_server.py &> audio_server.out &
audio_pid=$!
echo $audio_pid > pid.log
echo "Audio process ID is $audio_pid"
echo "Giving time for audio server to start"
sleep 60
echo "Starting Little Sleeper web server"
nohup python3 web_server.py &> web_server.out &
web_pid=$!
echo $web_pid >> pid.log
echo "Web process ID is $web_pid"
