Run the minecraft server on kaggle and sync the data to aliyundrive

```bash
# init environment
!curl -fsSL https://raw.githubusercontent.com/jawide/kaggle-minecraft/master/init.sh | sh
```

```bash
# install minecraft 1.19 server.jar (optional)
!curl -fsSL https://raw.githubusercontent.com/jawide/kaggle-minecraft/master/1.19.sh | sh
```

```bash
# download minecraft folder from aliyundrive
!curl -fsSL https://raw.githubusercontent.com/jawide/kaggle-minecraft/master/pull.py | python
```

```bash
# run minecraft server and ngrok
!curl -fsSL https://raw.githubusercontent.com/jawide/kaggle-minecraft/master/run.py | python - your_token
```

```bash
# upload minecraft folder to aliyundrive
!curl -fsSL https://raw.githubusercontent.com/jawide/kaggle-minecraft/master/push.py | python
```

```mermaid
graph LR
	aliyundrive-->kaggle
	kaggle-->aliyundrive
	kaggle-->ngrok
	ngrok-->kaggle
	ngrok-->player1
	player1-->ngrok
	ngrok-->player2
	player2-->ngrok
	ngrok-->player3
	player3-->ngrok
    subgraph player
    player1
    player2
    player3
    end
    subgraph proxy
    ngrok
    end
    subgraph server
    minecraft
    kaggle
    end
    subgraph storage
    aliyundrive
    end
```