

def main()->None:
    print('******************** 1.房貸 ********************')
    mortgage_calculator()
    print('******************** 1.房貸 end ********************')
    
    print('******************** 2.找質數 ********************')
    find_prime_number()
    print('******************** 2.找質數 end ********************')
    
    print('******************** 3.複利計息 ********************')
    compound_interest_calculator()
    print('******************** 3.複利計息 end ********************')

    
def mortgage_calculator():
    P = input("請輸入貸款總金額：")
    Y = input("請輸入貸款年限(年)：")
    G = input("請輸入寬限期(年)：")
    R = input("請輸入年利率(%)：")
    
    _P0 = float(P)
    _r = float(year_to_month_rate(R))
    _g = float(payment_periods(G))
    _y = float(payment_periods(Y)) - _g
    
    monthly_payment_interest = round(_P0 * _r)
    monthly_payment = round((_r / (1 - (1 + _r)**(-_y))) * _P0)
    
    if _g > 0:
        print(f"寬限期月繳：{monthly_payment_interest:,.0f}")
    print(f"本息攤月繳：{monthly_payment:,.0f}")
    print("-----------------------")
    
    for i in range(1, int(_g + _y) + 1, 1):
        if i <= _g:
            print(f"第{("0"+str(i))[-2:]}期：{monthly_payment_interest:,.0f}")
        else:
            print(f"第{("0"+str(i))[-2:]}期：{monthly_payment:,.0f}")
            

def year_to_month_rate(R):
    return float(R) / 100 / 12


def payment_periods(_N):
    return float(_N) * 12


def find_prime_number():
    l = 1000
    prime = [1] * (l + 1)
    prime[0] = 0
    prime[1] = 0

    for i in range(2, int(l**0.5) + 1):
        if prime[i]: # 是質數
            for j in range(i * i, l + 1, i): # 從i平方開始看
                prime[j] = 0

    for i in range(l + 1):
        if prime[i]:
            print(i)
            

def compound_interest_calculator():
    """各頻率複利計息"""
    print("-----------3.1. 各頻率複利計息------------")
    
    P = 1_000_000 # 本金
    R = 0.1       # 年息
    n = [1, 2, 4, 12, 52, 365]
    freq = ['年', '半年', '季', '月', '週', '日']
    
    for i, j in zip(n, freq):
        interest_rate = R / i
        interest = P * interest_rate
        total_interest = P * (1 + interest_rate)**i - P
        
        print(f'每{j}利息：{interest:,.0f}')
        print(f'總利息：{total_interest:,.0f}')
        print('-----------------------')
    
    """分鐘複利計息"""
    print("-----------3.2. 分鐘複利計息------------")
    
    P = 1_000_000
    ep = 0.51 * 0.05 + 0.49 * (-0.05)
    print((1 + ep)**(270 * 252) * P)
    
    
if __name__ == "__main__":
    main()