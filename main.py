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

WUXING_ADVICE = {
    "木": {
        "summary": "成長型、重視長期累積與趨勢延伸。",
        "advice": "木屬性適合建立長期投資紀律，可關注具成長性、研發能力或長線需求支撐的產業。操作上宜避免只追短線題材，應重視基本面、定期檢視與分散配置。",
    },
    "火": {
        "summary": "行動型、反應快，容易受市場情緒帶動。",
        "advice": "火屬性適合明確設定進出場規則與風險上限，可研究動能、景氣循環與市場熱度變化。需特別避免過度交易與情緒化加碼，建議用停損、停利與部位控管降低波動風險。",
    },
    "土": {
        "summary": "穩健型、重視安全感與資產配置平衡。",
        "advice": "土屬性適合以資產配置為核心，重視現金流、風險分散與投資組合穩定度。可採取定期定額或核心衛星配置，避免因過度保守而完全錯失長期成長機會。",
    },
    "金": {
        "summary": "紀律型、重視規則、效率與風險報酬比。",
        "advice": "金屬性適合使用量化條件、財務指標與明確篩選規則做投資決策。可重視價值評估、財務體質與風險報酬比，但需避免過度僵化，仍要留意市場環境變化。",
    },
    "水": {
        "summary": "觀察型、擅長資訊整合與等待機會。",
        "advice": "水屬性適合重視研究、資料蒐集與情境推演，可觀察利率、匯率、資金流與總體經濟變化。需避免因資訊過多而猶豫不決，建議事先設定可執行的投資條件。",
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
    advice = WUXING_ADVICE[element]

    print("\n生日五行金融密碼計算器")
    print("=" * 30)
    print(f"出生日期：{birthday.strftime('%Y-%m-%d')}")
    print("\n拆位加總流程：")
    print(format_steps(steps))
    print(f"\n生日數字密碼：{password}")
    print(f"河圖五行屬性：{element}")
    print("\n河圖五行數字對應表：")
    print(format_wuxing_table(password))
    print(f"\n投資風格摘要：{advice['summary']}")
    print(f"金融投資建議：{advice['advice']}")
    print("\n風險提醒：本內容僅供課堂學習與投資風格分析，不構成投資建議、買賣推薦或收益保證。")


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
