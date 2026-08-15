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

WUXING_INVESTMENT_ADVICE = {
    "木": {
        "投資性格": "重視成長與長期累積",
        "適合策略": "定期定額、長線布局",
        "可關注資產類型": "寬基指數與成長型資產",
        "行為提醒": "避免追高，定期檢視配置。",
    },
    "火": {
        "投資性格": "行動果斷，對趨勢敏感",
        "適合策略": "核心－衛星策略",
        "可關注資產類型": "趨勢或成長主題資產",
        "行為提醒": "限制單一主題與短線部位。",
    },
    "土": {
        "投資性格": "重視穩定與安全感",
        "適合策略": "穩健分散、重視現金流",
        "可關注資產類型": "債券、股利型與平衡型資產",
        "行為提醒": "避免因過度保守錯失長期成長。",
    },
    "金": {
        "投資性格": "紀律嚴謹，重視分析",
        "適合策略": "依規則配置、重視估值",
        "可關注資產類型": "高品質債券、價值或股利型資產",
        "行為提醒": "避免過度追求完美而延後執行。",
    },
    "水": {
        "投資性格": "彈性高，對資訊敏感",
        "適合策略": "保留流動性、全球分散",
        "可關注資產類型": "現金等價物、債券與全球型資產",
        "行為提醒": "避免因市場訊息頻繁調整部位。",
    },
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


def get_investment_advice(element: str) -> dict[str, str]:
    """取得指定五行的性格導向投資建議。"""
    return WUXING_INVESTMENT_ADVICE[element]


def format_investment_advice(element: str) -> str:
    """將指定五行的投資建議格式化成 terminal 文字。"""
    advice = get_investment_advice(element)
    lines = [f"{label}：{content}" for label, content in advice.items()]
    return "\n".join(lines)


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
    print(f"\n{element}行投資建議：")
    print(format_investment_advice(element))
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
