import json

import helper


def load_nobel_prizes(filename='prize.json'):
    with open(filename) as f:
        return json.load(f)


def main(year, category):
    data = load_nobel_prizes()
    prizes = data["prizes"]
    if year:
        prizes = filter(lambda p: p["year"] == year, prizes)
    if category:
        prizes = filter(lambda p: p["category"] == category.lower(), prizes)
    for p in prizes:
        print(p)
    # Add more here!


if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)


