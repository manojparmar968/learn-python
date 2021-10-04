def week(i): ## You can control the flow of program.
    switcher={
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }  
    return switcher.get(i,"Invalid day of week")
    
print(week(0))