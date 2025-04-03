def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins_list = [100, 50, 25]
coins_dict = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(*coins_list), "Knuts")
print(total(**coins_dict), "Knuts")
