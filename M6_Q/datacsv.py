import csv
data_list = [
    {"id":1001,"wname":"python","year":2019,"status":1,"company":"Heraizen"},
  {"id":1002,"wname":"web","year":2018,"status":2,"company":"spaneos"}
]

try:
    with open("ws.csv","w",newline='') as file:
        heading = ["id","wname","year","status","company"]
        obj = csv.DictWriter(file,fieldnames=heading)
        obj.writeheader()
        obj.writerows(data_list)
except Exception as e:
    print(str(e))