def count_substring(string, sub_string):    
    count = 0
    for w in range(0,len(string)):        
        if string[w:w+len(sub_string)] == sub_string:
            count += 1
            #print(string[w:w+len(sub_string)])        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)