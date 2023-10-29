def main():
    s=input("What time is it? ")
    r=int(s.replace(":",""))

    if r>=700 and r<=800:
        print("breakfast time")
    elif r>=1200 and r<=1300:
        print("lunch time")
    elif r>=1800 and r<=1900:
        print("dinner time")


def convert(time):

    r=int(time.replace(":",""))
    g=int(r/100)

    d=((r%100)/100)*(10/6)

    e=g+d
    return e


if __name__ == "__main__":
    main()
