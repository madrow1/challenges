from collections import Counter

def main():
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    sales = Counter(STA001=5, SAL002=3, ENT004=3)
    made = Counter(STA001=9, ENT004=1)
    inventory = inventory - sales
    inventory.update(made)
    inventory.most_common()
    #sell 5 starters, 3 salads, and 3 entrees
    #make 9 more starters and 1 more entree
    print(inventory)

if __name__ == "__main__":
    main()