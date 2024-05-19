# string_operations.py
# 文字列を操作する簡単な関数を定義

def reverse_string(s):
    """与えられた文字列を逆順にする"""
    return s[::-1]

def count_vowels(s):
    """文字列内の母音の数をカウント"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# string_operations.py
# 文字列を操作する簡単な関数を定義

def reverse_string(s):
    """与えられた文字列を逆順にする"""
    return s[::-1]

def count_vowels(s):
    """文字列内の母音の数をカウント"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)