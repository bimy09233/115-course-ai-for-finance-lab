def main() -> None:
    
    """各頻率複利計息"""
    print('各頻率複利計息：')
    print('*************')
    
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
    print('分鐘複利計息：')
    print('*************')
    
    P = 1_000_000
    ep = 0.51 * 0.05 + 0.49 * (-0.05)
    print((1 + ep)**(270 * 252) * P)

if __name__ == "__main__":
    main()