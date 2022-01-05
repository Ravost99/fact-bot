# fact-bot
A simple discord bot that generates facts!

<p align="center">
  <a href="//github.com/ravost99/fact-bot/releases"><img src="https://img.shields.io/github/v/release/ravost99/fact-bot"></a>
  <a href="//github.com/ravost99/fact-bot/commits/main"><img src="https://img.shields.io/github/last-commit/ravost99/fact-bot"></a>
  <a href="//github.com/ravost99/fact-bot/releases"><img src="https://img.shields.io/github/downloads/ravost99/fact-bot/total"></a>
  <a href="//github.com/ravost99/fact-bot/blob/main/LICENSE.md"><img src="https://img.shields.io/github/license/ravost99/fact-bot"></a>
  <a href="//github.com/ravost99/fact-bot"><img src="https://img.shields.io/github/languages/code-size/ravost99/fact-bot"></a>
  <a href="//github.com/ravost99/fact-bot/issues"><img src="https://img.shields.io/github/issues-raw/ravost99/fact-bot"></a>
</p>

-------
## How to make a bot
Go to https://discord.com/developers/applications
Then click on 'New Application'
Enter the name and click 'Create'
Under the Bot section click add bot, then there's your bot!


-------
### How to use `keep_alive.py` to make the bot stay alive.

An example is in keep_alive.py it renders `Online!`
If you want to render html documents just do
```py
@app.route('/example')
def example():
  return render_template('index.html')
```
Then go to [Uptimerobot](https://Uptimerobot.com/) and follow instructions for keeping the bot alive

Default startup if you want. Just change startup to `True` in `main.py`