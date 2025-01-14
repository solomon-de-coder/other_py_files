# Worker Recruitment project
w = {}  # Store worker details

while True:
    print("Worker Recruitment System")
    print("1. Add Worker")
    print("2. Remove Worker")
    print("3. Show Workers")
    print("4. Search Worker")
    print("5. Quit")

    c = input("Choose: ")
    if c == "1":
        # Add worker
        id = input("Worker ID: ")
        n = input("Name: ")
        r = input("Region: ")
        j = input("Job (Painter, Mason): ")
        a = input("Avail (Full, Part): ")
        p = float(input("Price: "))
        t = input("Contact: ")

        w[id] = {
            "N": n,
            "R": r,
            "J": j,
            "A": a,
            "P": p,
            "T": t
        }
        print("Added!\n")
    elif c == "2":
        # Remove worker
        id = input("Worker ID to Remove: ")
        if id in w:
            del w[id]
            print("Removed!\n")
        else:
            print("Not Found!\n")
    elif c == "3":
        # Show all workers
        if len(w) == 0:
            print("No Workers!\n")
        else:
            print("Workers:")
            for id, d in w.items():
                print("ID:", id, "Info:", d)
            print()
    elif c == "4":
        # Search worker
        j = input("Job: ")
        r = input("Region: ")
        b = float(input("Budget: "))

        f = False
        for id, d in w.items():
            if (d["J"].lower() == j.lower() and d["R"].lower() == r.lower() and d["P"] <= b):
                print("Found: ID:", id, "Info:", d)
                f = True
        if not f:
            print("No Match!\n")
    elif c == "5":
        print("Bye!")
        break
    else:
        print("Invalid! Try again.\n")
