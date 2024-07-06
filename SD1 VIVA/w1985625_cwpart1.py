#referances-python documentory,python for beginers
#uow number-w1985625
#21.04.2023


progress_count, trailer_count, retriever_count, exclude_count = 0, 0, 0, 0
def check_validity(value):
    creditsTOEnter = [0, 20, 40, 60, 80, 100, 120]
    try:
        value = int(value)
        if not value in creditsTOEnter:
            print("Out of range")
            return "error"
        return value
    except ValueError:
        print("Integer required")
        return "error"

while True:
    while True:
        pass_credit = input("Enter Credit at pass: ")
        pass_credit =  check_validity(pass_credit)
        if pass_credit != "error":
            break

    while True:
        defer_credit = input("Enter Credit at defer: ")
        defer_credit = check_validity(defer_credit)
        if defer_credit != "error":
            break

    while True:
        fail_credit = input("Enter Credit at fail: ")
        fail_credit = check_validity(fail_credit)
        if fail_credit != "error":
            break
    Total = pass_credit + defer_credit + fail_credit
    if Total != 120:
            print("Total incorrect")

    else:
     if pass_credit == 120:
        print("Progress")
        progress_count += 1
     elif pass_credit == 100:
        print("Progress (module trailer)")
        trailer_count += 1
     elif fail_credit >= 80:
        print("Exclude")
        exclude_count += 1
     else:
        print("module retriever")
        retriever_count += 1

    print(f"Progress {progress_count} : ", end="")
    print("*" * progress_count)

    print(f"Trailer {trailer_count}  : ", end='')
    print("*" * trailer_count)

    print(f"Retriever {retriever_count}: ", end='')
    print("*" * retriever_count)

    print(f"Exclude {exclude_count}  : ", end='')
    print("*" * exclude_count)

    outcome_count = progress_count + trailer_count + retriever_count + exclude_count
    print(outcome_count, end="")
    print(" outcomes in total.")    
        
