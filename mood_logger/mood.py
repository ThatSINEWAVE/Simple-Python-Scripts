import json
from pathlib import Path
from datetime import date
from datetime import datetime



def log_mood():

    while True:
        try:
            score = input("enter your today's mood 5 = very well, 4 = well, 3= not bad, 2 = bad, 1 = very bad ")
            score = int(score)
            if 1<= score <= 5:
                break
            else:
                print("Please enter a number between 1 and 5")

        except ValueError:
            print("Please enter a number between 1 and 5")

    from datetime import date
    today = date.today().isoformat()
    mood_data = {"date": today, "score": score}
    return mood_data

def save_mood(mood_data):

    data_dir = Path("./data")
    data_dir.mkdir(exist_ok=True)
    file_path = data_dir / "moods.json"

    moods = []
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            moods = json.load(f)

    moods = []
    moods.append(mood_data)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(moods, f, indent=4, ensure_ascii=False)

    print(f" {mood_data['date']} with score {mood_data['score']} saved")

def show_history(limit=7):

    data_dir = Path("./data")
    file_path = data_dir / "moods.json"

    if not file_path.exists():
        print("there is no mood saved yet")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        moods = json.load(f)

    if not moods:
        print("there is no mood saved yet")
        return

    last_records = moods[-limit:] if len(moods) > limit else moods

    print(f"\n the last {len(last_records)} day:")
    print("-"*30)

    def score_to_emoji(score):
        emoji_map ={
            1:"😔",
            2:"😒",
            3:"😐",
            4:"😊",
            5:"😍"
        }
        return emoji_map.get(score ,"?")

    for record in last_records:
        date_str = record["date"]
        score = record["score"]
        emoji = score_to_emoji(score)


        try:
            d = datetime.strptime(date_str, "%Y-%m-%d")
            weekdays = ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]
            weekday_name = weekdays[d.weekday()]
        except:
            weekday_name = ""

        print(f"{date_str}({weekday_name}): {emoji}{score}")
    print("-"*30)

def show_report():
    data_dir = Path("./data")
    file_path = data_dir / "moods.json"
    if not file_path.exists():
        print("there is no mood saved yet")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        moods = json.load(f)

    if not moods:
        print("there is no mood saved yet")
        return

    scores = [m["score"] for m in moods]
    avg_score = sum(scores) / len(scores)

    best_score = max(scores)
    worst_score = min(scores)

    best_days = [m["date"] for m in moods if m["score"] == best_score]
    worst_day = [m["date"] for m in moods if m["score"] == worst_score]

    def score_to_emoji(score):
        emoji_map ={
            1:"😔",
            2:"😒",
            3:"😐",
            4:"😊",
            5:"😍"
        }
        return emoji_map.get(score ,"?")

    score_counts = {1:0, 2:0, 3:0, 4:0, 5:0}
    for s in scores:
        score_counts[s] = score_counts.get(s,0) + 1

    print("\n"+"="*40)
    print("mood report:")
    print("="*40)
    print(f"days saved: {len(moods)}")
    print(f"avrage score: {avg_score}")
    print(f"best days ({best_score}{score_to_emoji(best_score)}):")
    for day in best_days:
        print(f" .{day}")

    print("\n distribution of moods:")
    print("-"*40)
    for score in range(1, 6):
        count = score_counts.get(score,0)
        bar = "#" * count
        print(f"{score} {score_to_emoji(score)}: {bar} ({count})")

    sorted_moods = sorted(moods, key=lambda x: x["date"])

    best_streak = 1
    current_streak = 1

    for i in range(1, len(sorted_moods)):
        prev_date = datetime.strptime(sorted_moods[i-1]["date"], "%Y-%m-%d")
        curr_date = datetime.strptime(sorted_moods[i]["date"], "%Y-%m-%d")
        diff = (curr_date - prev_date).days

        if diff ==1:
            current_streak += 1
            best_streak = max(best_streak, current_streak)
        else:
            current_streak = 1

    if len(sorted_moods) > 1:
        print(f"\n longest streak: {best_streak} days")

    print("-"*40)

if __name__ == "__main__":
    pass

