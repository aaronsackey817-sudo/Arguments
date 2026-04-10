def total_calc(bill_amout,tip_perc):
    total=bill_amout*(1+0.01*tip_perc)
    total=round(total,2)
    print(f"total bill is:{total}")
bill_amout=float(input("enter the amout; "))
tip_perc=float(input("enter tip percentage: "))
total_calc(bill_amout,tip_perc)