cd /root
echo "install jdk-17..."
if [ ! -e jdk-17_linux-x64_bin.tar.gz ]; then wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz > /dev/null; fi
echo "extract..."
if [ ! -e jdk-17 ]; then mkdir jdk-17 && tar -zxvf jdk-17_linux-x64_bin.tar.gz -C jdk-17 --strip-components 1 > /dev/null; fi
echo "install ngrok..."
if ! which ngrok; then curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc > /dev/null; fi
if ! which ngrok; then echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list > /dev/null; fi
if ! which ngrok; then sudo apt update > /dev/null; fi
if ! which ngrok; then sudo apt install ngrok > /dev/null; fi
echo "install aligo..."
if ! pip show -qf aligo; then pip install aligo > /dev/null; fi