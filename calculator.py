"""
간단한 계산기 모듈
"""

def add(a, b):
    """두 숫자를 더합니다."""
    return a + b

def subtract(a, b):
    """두 숫자를 뺍니다."""
    return a - b

def multiply(a, b):
    """두 숫자를 곱합니다."""
    return a * b

def divide(a, b):
    """두 숫자를 나눕니다. 0으로 나누는 경우 예외를 발생시킵니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b

def power(a, b):
    """a의 b제곱을 계산합니다."""
    return a ** b

if __name__ == "__main__":
    print("계산기 테스트")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"6 / 2 = {divide(6, 2)}")
    print(f"2^3 = {power(2, 3)}")
