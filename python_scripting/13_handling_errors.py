while True:
    try:
        score = int(input("Enter your score: "))
        break
    except ValueError:
        print("Imput must be integer.")
    except KeyboardInterrupt:
        print("Usr manually terminated programe.")
    finally:
        print("Process completed.")
