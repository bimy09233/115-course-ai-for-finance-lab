def year_to_month_rate(R):
    return float(R) / 100 / 12

def payment_periods(_N):
    return float(_N) * 12

def mortgage_calculator(P, Y, G, R):
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

def main() -> None:
    P = input("請輸入貸款總金額：")
    Y = input("請輸入貸款年限(年)：")
    G = input("請輸入寬限期(年)：")
    R = input("請輸入年利率(%)：")
    
    print("-----------------------")
    print(f"貸款總金額：{float(P):,.0f}")
    print(f"貸款年限(年)：{Y}")
    print(f"寬限期(年)：{G}")
    print(f"年利率(%)：{R}")
    print("-----------------------")
    
    mortgage_calculator(P, Y, G, R)

if __name__ == "__main__":
    main()