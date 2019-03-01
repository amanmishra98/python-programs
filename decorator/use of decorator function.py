def decor_result(result_function):#decorator function
    def distinction(marks):
        for m in marks:
            if m>=75:
                print("congrats")
        else:
            result_function(marks)
    return distinction

@decor_result

def result(marks):
    for x in marks:
        if x>=33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")
result([90,60,32,75])        
