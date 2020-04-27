def swap_case(s):    
    new_word = ""
    for c in s:
        if c.isupper():
            new_word += c.lower()
        else:
            new_word += c.upper()
    return new_word

if __name__ == '__main__':
    print(swap_case("Hola 1"))