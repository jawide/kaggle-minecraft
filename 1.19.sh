cd /root/minecraft
echo "install server.jar..."
if [ ! -e server.jar ];then wget https://launcher.mojang.com/v1/objects/e00c4052dac1d59a1188b2aa9d5a87113aaf1122/server.jar > /dev/null; fi