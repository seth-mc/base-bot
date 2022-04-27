# Base Bot

Welcome to the Base Bot - which will be the launch pad for our project! Check out the Lucid Chart here:

    [IN PROGRESS]


### To add the repository to your own computer:

#### The manual approach:
1. Click Code > Download ZIP.
2. Open the ZIP file and put it somewhere nice. 
3. Tinker with the code. If you want to make changes and push them back, you will need to folow the cool coding approach. 

#### The cool coding approach:
1. Create a new file for your GitHub documents.
2. Copy the filepath by going Edit > click "Alt" and select 'Copy "GitHub" as Filename'. 
3. open Terminal. Enter the following:
```
cd [paste FILEPATH to GitHub]
```
4. clone the repo on in to your GitHub file:
```
git clone https://github.com/seth-mc/base-bot.git
```


### After making changes to the repository:
1. open Terminal. Enter the following:
```
cd [FILEPATH to GitHub]
```

2. Then, either add the URL (Or set-URL if you get a "fatal: remote origin already exists" error)

```
git remote add origin https://github.com/seth-mc/base-bot.git

git remote set-url origin https://github.com/seth-mc/base-bot.git

```

3. Add the files:
```
git add .
git commit -m "enter description here"
git push origin main
```


## Description
This Binance trading bot analyses the changes in price across all coins on Binance and place trades on the most volatile ones. 
In addition to that, this Binance trading algorithm will also keep track of all the coins bought and sell them according to your specified Stop Loss and Take Profit.

The bot will listen to changes in price accross all coins on Binance. By default, we're only picking USDT pairs. We're excluding Margin (like BTCDOWNUSDT) and Fiat pairs

> Information below is an example and is all configurable

- The bot checks if the any coin has gone up by more than 3% in the last 5 minutes
- The bot will buy 100 USDT of the most volatile coins on Binance
- The bot will sell at 6% profit or 3% stop loss


You can follow the [Binance volatility bot guide](https://www.cryptomaton.org/2021/05/08/how-to-code-a-binance-trading-bot-that-detects-the-most-volatile-coins-on-binance/) for a step-by-step walkthrough of the bot development.

## READ BEFORE USE
1. If you use the `TEST_MODE: False` in your config, you will be using REAL money.
2. To ensure you do not do this, ALWAYS check the `TEST_MODE` configuration item in the config.yml file..
3. This is a framework for users to modify and adapt to their overall strategy and needs, and in no way a turn-key solution.
4. Depending on the current market, the default config might not do much, so you will have to adapt it to your own strategy.

## Usage
Please checkout our wiki pages:

- [Setup Guide](https://github.com/CyberPunkMetalHead/Binance-volatility-trading-bot/wiki/Setup-Guide)
- [Bot Strategy Guide](https://github.com/CyberPunkMetalHead/Binance-volatility-trading-bot/wiki/Bot-Strategy-Guide)
- [Configuration Guide](https://github.com/CyberPunkMetalHead/Binance-volatility-trading-bot/wiki/Configuration)
