from __future__ import annotations

import argparse
from datetime import date, datetime


WUXING_BY_DIGIT = {
    1: "木",
    6: "木",
    2: "火",
    7: "火",
    5: "土",
    0: "土",
    4: "金",
    9: "金",
    3: "水",
    8: "水",
}


def split_digits(number: int) -> list[int]:
    """將整數拆成各位數字清單。"""
    return [int(digit) for digit in str(number)]


def calculate_birthday_password(birthday: date) -> tuple[int, list[tuple[list[int], int]]]:
    """計算生日數字密碼並保留每次拆位加總過程。"""
    birthday_digits = [int(digit) for digit in birthday.strftime("%Y%m%d")]
    steps = []
    current_digits = birthday_digits

    while True:
        total = sum(current_digits)
        steps.append((current_digits, total))
        if total < 10:
            return total, steps
        current_digits = split_digits(total)


def format_steps(steps: list[tuple[list[int], int]]) -> str:
    """將生日密碼計算步驟格式化成 terminal 文字。"""
    lines = []
    for index, (digits, total) in enumerate(steps, start=1):
        expression = " + ".join(str(digit) for digit in digits)
        lines.append(f"第 {index} 次：{expression} = {total}")
    return "\n".join(lines)


def format_wuxing_table(selected_digit: int | None = None) -> str:
    """建立文字版河圖五行數字對應表。"""
    rows = []
    for element in ["木", "火", "土", "金", "水"]:
        digits = [
            f"[{digit}]" if digit == selected_digit else str(digit)
            for digit in range(10)
            if WUXING_BY_DIGIT[digit] == element
        ]
        rows.append(f"{element}：{', '.join(digits)}")
    return "\n".join(rows)


def parse_birthday(value: str) -> date:
    """解析支援 YYYY-MM-DD、YYYYMMDD、YYYY/MM/DD 格式的生日。"""
    supported_formats = ("%Y-%m-%d", "%Y%m%d", "%Y/%m/%d")
    for birthday_format in supported_formats:
        try:
            birthday = datetime.strptime(value, birthday_format).date()
            break
        except ValueError:
            continue
    else:
        raise argparse.ArgumentTypeError(
            "請輸入有效日期，格式可為 2000-01-01、20000101 或 2000/01/01。"
        )

    if birthday > date.today():
        raise argparse.ArgumentTypeError("出生日期不可晚於今天。")

    return birthday


def prompt_birthday() -> date:
    """在沒有 CLI 參數時，改由 terminal 互動輸入生日。"""
    while True:
        raw_value = input("請輸入出生日期（YYYY-MM-DD、YYYYMMDD 或 YYYY/MM/DD）：").strip()
        try:
            return parse_birthday(raw_value)
        except argparse.ArgumentTypeError as error:
            print(f"輸入錯誤：{error}")


def print_result(birthday: date) -> None:
    password, steps = calculate_birthday_password(birthday)
    element = WUXING_BY_DIGIT[password]

    print("\n生日五行金融密碼計算器")
    print("=" * 30)
    print(f"出生日期：{birthday.strftime('%Y-%m-%d')}")
    print("\n拆位加總流程：")
    print(format_steps(steps))
    print(f"\n生日數字密碼：{password}")
    print(f"河圖五行屬性：{element}")
    print("\n河圖五行數字對應表：")
    print(format_wuxing_table(password))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="生日五行金融密碼 terminal 計算器")
    parser.add_argument(
        "birthday",
        nargs="?",
        type=parse_birthday,
        help="西元出生日期，格式可為 YYYY-MM-DD、YYYYMMDD 或 YYYY/MM/DD；未提供時會進入互動輸入模式。",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    birthday = args.birthday or prompt_birthday()
    print_result(birthday)


if __name__ == "__main__":
    main()
