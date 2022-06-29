import time
import shlex
import argparse
import traceback
import subprocess


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="token", help="your ngrok authtoken. see https://dashboard.ngrok.com/get-started/your-authtoken")
    args = parser.parse_args()
    
    subprocess.Popen(shlex.split(f"ngrok authtoken {args.token}")).wait()
    java_process = subprocess.Popen(shlex.split("/root/jdk-17/bin/java -jar server.jar nogui"), cwd="/root/minecraft")
    ngrok_process = subprocess.Popen(shlex.split("ngrok tcp 25565 --log stdout --region ap"))

    try:
        while True:
            time.sleep(1)
    except:
        java_process.kill()
        java_process.wait()
        ngrok_process.kill()
        ngrok_process.wait()
        traceback.print_exc()