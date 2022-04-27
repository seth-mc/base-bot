# rchop(coin, PAIR_WITH)
#             ^- The coin that you chose for pairing from config.yml (ex: USDT)
#        ^- The coin that the bot needs to buy/sell
# returns the coin name without the 'USDT' at the end

def rchop(s, suffix):
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    return s