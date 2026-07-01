# line notice robot
line notice robot is a semi-automatic bot that will auto notify you
base on the text you given on LINE.

## pre install
1.clone this repository into your familer folder

```bash
git clone https://github.com/Naynkaon/line-notify-bot.git
```

2. install [ngrok](https://ngrok.com/download/windows) in your computer

run this code in your terminal, replace <YOUR_AUTHTOKEN> into your ngrok Token
```bash
ngrok config add-authtoken "<YOUR_AUTHTOKEN>"   
```
3. creating a **.env** file under the project folder, and copy and paste this text into it
```.env
#replace <YOUR_LINE_BOT_TOKEN> and <YOUR_LINE_BOT_SECRET> into your real line bot token and secret

MY_TOKEN = <YOUR_LINE_BOT_TOKEN>
MY_SECRET = <YOUR_LINE_BOT_SECRET>
```

4. run ngrok tunnel in your project cmd first
```cmd
ngrok https 5000
```
5. open another cmd to run the main python program
```cmd
python app.py
```
and then you have it, a notify bot in your line, enjoy!

credit:
    my friend -- 
    Recommend me some coding ideas, and find some logic bugs