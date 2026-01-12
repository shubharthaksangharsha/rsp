def solution(arr):
    # your code here
    # naive approach I can think 
    res, i, s, e, counter = "", 0, 0, 1, 1  
    while e < len(arr):
        if arr[e] == arr[i] + 1: 
            counter += 1; i += 1; e += 1; 
            continue
        else:
            if counter >= 3: 
                res += f"{s}-{i}"; 
                c = 1; s = i; 
                continue 
            else: 
                res += f",{s}" 
                res += f",{i}" 
                counter = 1; i += 1; e += 1; s = i; 
                continue
    return res 


if __name__ == "__main__":
    print(solution([-3, -2, -1, 6, 4, 8, 9, 10, 11, 12, 48]))