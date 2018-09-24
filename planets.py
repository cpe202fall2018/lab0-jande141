def weight_on_planets():
    # write your code here Justin A
    eweight = int(input("What do you weigh on earth? "))
    mweight = eweight *.38
    jweight = eweight *2.34
    print("\nOn Mars you would weigh {0:.2f} pounds.\nOn Jupiter you would weigh {1:.2f} pounds.".format(mweight, jweight))
    return
   
   
if __name__ == '__main__':
    weight_on_planets()