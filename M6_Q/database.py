'''using list'''
data_list = [
    [1001,"python",2019,1,"Heraizen"],
    [1002,"web",2018,1,"Spaneos"],
    [1003,"java",2017,1,"Heraizen"]
]

try:
    with open("ws.txt","w") as file:
        for d in data_list:
            line = f"{d[0]},{d[1]},{d[2]},{d[3]},{d[4]} \n"
            file.write(line)

except Exception as e:
    print(str(e))