        with open('golf.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        
        print(data)