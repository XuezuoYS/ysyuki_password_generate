import random
import string

def generator(length:int = 8, special_chars:string = "", include_numbers:bool = True, allow_start_with_special:bool = True):
    """
    密码生成器
    
    :param length: 长度
    :type length: int
    :param special_chars: 特殊字符无需区分
    :type special_chars: string
    :param include_numbers: 是否加入数字
    :type include_numbers: bool
    :param allow_start_with_special: 是否允许密码开头是特殊字符
    :type allow_start_with_special: bool
    """

    # 构建字符集
    chars = string.ascii_lowercase  # 默认包含小写字母
    chars += string.ascii_uppercase  # 添加大写字母
    
    if include_numbers:
        chars += string.digits
    
    if special_chars:
        chars += special_chars
    
    if not chars:
        raise ValueError("至少需要一种类型的字符才能生成密码")
    
    password = []
    
    # 处理首字符限制
    if not allow_start_with_special:
        # 首字符只能是字母
        first_char = random.choice(string.ascii_letters)
        password.append(first_char)
        remaining_length = length - 1
    else:
        # 首字符可以是任意字符
        first_char = random.choice(chars)
        password.append(first_char)
        remaining_length = length - 1
    
    # 生成剩余字符
    for _ in range(remaining_length):
        password.append(random.choice(chars))
    
    # 打乱除首字符外的其他字符顺序，确保安全性
    if length > 1:
        remaining_part = password[1:]
        random.shuffle(remaining_part)
        password = [password[0]] + remaining_part
    
    return ''.join(password)
