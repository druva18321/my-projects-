print("===TERMINAL TRADE LEDGER===")
ticker = input("Enter the ticker or the pair(e.g TATA)")
asset_type= input("Is this a (1) Stock or (2) crypto/forex? Type 1 OR 2")
buy_price= float(input("Enter the price you brought at"))
sell_price= float(input("Enter the price you sold at"))
qnt = float(input("Enter the Quantity"))
gross_p_l = (sell_price-buy_price)*qnt

if gross_p_l > 0:
    if asset_type == "1":
       tax=gross_p_l*0.20
       print("\n Stock Trade! slicing off 20% STCG Tax...")
    elif asset_type == "2":
       tax=gross_p_l*0.30
       print("\n Crypto/Forex Trade! slicing off 30% Flat Tax...")
    net_p_l=gross_p_l-tax
else:
    tax=0.0
    net_p_l=gross_p_l
    print("\n Tough Luck, Hey no Tax on a loss")
print("="*20)
print("Gross P&L=",gross_p_l)
print("Net P&L=",net_p_l)
print("Tax Paid=",tax)
print("="*20)

file = open("ledger.txt", "a")

# Converting numbers back to text (str) so they can be glued together
trade_record = ticker + " | Buy: " + str(buy_price) + " | Sell: " + str(sell_price) + " | Net: " + str(net_p_l) + "\n"

file.write(trade_record)
file.close()

print("Trade securely saved to ledger.txt.") 
