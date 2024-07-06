creditsTOEnter = [0, 20, 40, 60, 80, 100, 120]
progress_count, trailer_count, retriever_count, exclude_count = 0, 0, 0, 0
progress_list, trailer_list, retriever_list, exclude_list = [], [], [], []

while True:
    while True:
        try:
            pass_credit = int(input("Enter Credit at pass: "))
            if not pass_credit in creditsTOEnter:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")
            
    while True:
        try:
            defer_credit = int(input("Enter Credit at defer: "))
            if not defer_credit in creditsTOEnter:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

        while True:
         try:
            fail_credit = int(input("Enter Credit at fail: "))
            if not fail_credit in creditsTOEnter:
                print("Out of range")
            else:
                break
         except ValueError:
            print("Integer required")

    Total = pass_credit + defer_credit + fail_credit
    if Total != 120:
           print("Total incorrect")
    else:
       # processing code
     if pass_credit == 120:
        print("Progress")
        progress_count += 1
        progress_list.append([pass_credit, defer_credit, fail_credit])

     elif pass_credit == 100:
        print("Progress (module trailer)")
        trailer_list.append([pass_credit, defer_credit, fail_credit])
        trailer_count += 1

     elif fail_credit >= 80:
        print("Exclude")
        exclude_list.append([pass_credit, defer_credit, fail_credit])
        exclude_count += 1

     else:
         print("Module retriever")
         retriever_list.append([pass_credit, defer_credit, fail_credit])
         retriever_count += 1

    progress_list, trailer_list, retriever_list, exclude_list = [], [], [], []
progress_count, trailer_count, retriever_count, exclude_count = 0, 0, 0, 0

#...

if pass_credit == 120:
    #...
    progress_list.append([pass_credit, defer_credit, fail_credit])
elif pass_credit == 100:
    #...
    trailer_list.append([pass_credit, defer_credit, fail_credit])
elif fail_credit >= 80:
    #...
    exclude_list.append([pass_credit, defer_credit, fail_credit])
else:
    #...
    retriever_list.append([pass_credit, defer_credit, fail_credit])

    print("Histogram")
    print(f"Progress {progress_count} : ", end="")
    print("*" * progress_count)
    print(f"Trailer {trailer_count}  : " , end='' )
    print("*" * trailer_count)
    print(f"Retriever {retriever_count}: ", end='')
    print("*" * retriever_count)
    print(f"Exclude {exclude_count}  : ", end='')
    print("*" * exclude_count)

  # Print out the list
    print("Part 2")

for item in progress_list:
    print(f"Progress - {', '.join(str(i) for i in item)}")

for item in trailer_list:
    print(f"Trailer - {', '.join(str(i) for i in item)}")

for item in exclude_list:
    print(f"Exclude - {', '.join(str(i) for i in item)}")

for item in retriever_list:
    print(f"Retriever - {', '.join(str(i) for i in item)}")  
