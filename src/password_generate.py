import random
import secrets
import string


def generator(length:int = 8, special_chars:str = "", include_numbers:bool = True, allow_start_with_special:bool = True):
    """
    密码生成器
    
    :param length: 长度
    :type length: int
    :param special_chars: 特殊字符无需区分
    :type special_chars: str
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
        first_char = secrets.choice(string.ascii_letters)
        password.append(first_char)
        remaining_length = length - 1
    else:
        # 首字符可以是任意字符
        first_char = secrets.choice(chars)
        password.append(first_char)
        remaining_length = length - 1
    
    # 生成剩余字符
    for _ in range(remaining_length):
        password.append(secrets.choice(chars))
    
    # 打乱除首字符外的其他字符顺序，确保安全性
    if length > 1:
        remaining_part = password[1:]
        random.shuffle(remaining_part)
        password = [password[0]] + remaining_part
    
    password = legitimationPassword(''.join(password), length, special_chars, include_numbers)

    return password

def legitimationPassword(password:str, length:int, special_chars:str = "", include_numbers:bool = True) -> str:
    if length < 4:
        return password
    
    def checkIsIn(text:str, judge:str) -> bool:
        '''
        判断字符串中是否包含指定字符
        :param text: 待判断的字符串
        :type text: str
        :param judge: 判断的字符串
        :type judge: str
        :return: 是否包含指定字符
        :rtype: bool
        '''
        result = any(char in text for char in judge)
        return result
    
    def insertCharIntoString(text:str, insert:str, index:int) -> str:
        '''
        将字符替换字符串中某一位置
        :param text: 待插入的字符串
        :type text: str
        :param insert: 插入的字符
        :type insert: str
        :param index: 插入的位置
        :type index: int
        :return: 插入后的字符串
        :rtype: str
        '''
        return text[:index] + insert + text[(index + 1):]
    
    for _ in range(2):
        if not checkIsIn(password, string.ascii_uppercase):
            password = insertCharIntoString(password, secrets.choice(string.ascii_uppercase), length - 4)

        if not checkIsIn(password, string.ascii_lowercase):
            password = insertCharIntoString(password, secrets.choice(string.ascii_lowercase), length - 3)
        
        if include_numbers and not checkIsIn(password, string.digits):
            password = insertCharIntoString(password, secrets.choice(string.digits), length - 2)

        if special_chars != "" and not checkIsIn(password, special_chars):
            password = insertCharIntoString(password, secrets.choice(special_chars), length - 1)

    return password
    
    

