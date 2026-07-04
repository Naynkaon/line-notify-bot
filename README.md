# line notice robot
line notice robot is a semi-automatic bot that will auto notify you
base on the text you given on LINE.

## pre install
1.clone this repository into your familer folder

```bash
git clone https://github.com/Naynkaon/line-notify-bot.git
```

2.install [ngrok](https://ngrok.com/download/windows) in your computer

3.install [ollama](https://ollama.com/download) in your computer, and run this in your CMD so python can use it
```bash
pip install ollama
```

4.install the ai model you want to use as the summary tool
```bash
#use qwen2.5:1.5b as an example, can switch to whatever AI model you want

ollama pull qwen2.5:1.5b
```
you can find more ollama model in [here](https://ollama.com/search).

## setup

run this code in your terminal, replace <YOUR_AUTHTOKEN> into your ngrok Token
```bash
ngrok config add-authtoken "<YOUR_AUTHTOKEN>"   
```
1. Create a .env file in the project folder, then copy and paste this text into it.
```.env
#replace <YOUR_LINE_BOT_TOKEN> and <YOUR_LINE_BOT_SECRET> into your real line bot token and secret
# The YOUR_AI_MODEL needs to be changed with the AI model you downloaded

MY_TOKEN = <YOUR_LINE_BOT_TOKEN>
MY_SECRET = <YOUR_LINE_BOT_SECRET>
MY_AI_MODEL = "YOUR_AI_MODEL"
```

2. run ngrok tunnel in your project cmd first
```cmd
ngrok http 5000
```
3. open another cmd to run the main python program
```cmd
python app.py
```
and then you have it, a notify bot in your line, enjoy!

credit:
    my friend -- 
    Recommend me some coding ideas, and find some logic bugs
