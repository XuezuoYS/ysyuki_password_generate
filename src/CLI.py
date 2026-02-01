import password_generate

def run():
    while True:
        try:
            length_input = input("请输入密码长度 (默认8): ").strip()
            if length_input == "":
                length = 8
            else:
                length = int(length_input)
            
            if length < 1:
                print("密码长度必须大于0，请重新输入")
                continue
            break
        except ValueError:
            print("请输入有效的数字")
    
    special_chars_input = input("请输入允许的特殊字符 (直接按回车表示无特殊字符): ").strip()
    
    numbers_input = input("是否包含数字? (Y/n, 默认Y): ").strip().lower()
    include_numbers = numbers_input != 'n'
    
    start_input = input("是否允许以数字或特殊字符开头? (Y/n, 默认Y): ").strip().lower()
    allow_start_with_special = start_input != 'n'
    
    return {
        'length': length,
        'special_chars': special_chars_input,
        'include_numbers': include_numbers,
        'allow_start_with_special': allow_start_with_special
    }

if __name__ == '__main__':
    print(password_generate.generator(**run()))
    while True:
        input_continue = input("继续 C / 退出 其余任意键：").lower()
        if input_continue == 'c':
            print(password_generate.generator(**run()))
        else:
            break