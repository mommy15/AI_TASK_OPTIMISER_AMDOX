def recommend_tasks(emotion):
    # Normalize emotion input
    emotion = emotion.lower()

    if emotion in ["happy", "positive"]:
        return [
            "Critical tasks",
            "Creative work",
            "Team meetings"
        ]

    elif emotion in ["neutral"]:
        return [
            "Routine tasks",
            "Documentation",
            "Code review"
        ]

    elif emotion in ["sad", "angry", "fear", "stressed"]:
        return [
            "Light tasks",
            "Training or learning",
            "Take a short break"
        ]

    else:
        return [
            "General tasks",
            "Self-paced work"
        ]


def stress_alert(emotion):
    # Normalize emotion input
    emotion = emotion.lower()

    stress_emotions = ["sad", "angry", "fear", "stressed"]
    return emotion in stress_emotions

