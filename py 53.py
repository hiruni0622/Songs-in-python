import time
from itertools import cycle


lyrics = [
    "So I'ma love you every night like it's the last night",
    "Like it's the last night",

    "If the world was ending I'd wanna be next to you",
    "If the party was over and our time on Earth was  through",
]


delay_times = [0.3, 0.3,0.3, 0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.9,0.3,0.3,0.3,0.3,0.9,0.3,0.3,0.7,0.7,0.7,0.3,0.3,0.3,0.7,0.3,4.6,0.3,0.3,0.7,0.7,0.7,0.3,0.3,0.3,0.7,0.3,0.3,4.6]  # Example delay times in seconds


def display_lyrics_with_varied_delays(lyrics, delays):
    delay_cycle = cycle(delays)
    for line in lyrics:
        words = line.split()
        for word in words:
            print(word, end=" ", flush=True)
            time.sleep(next(delay_cycle))
        print()


display_lyrics_with_varied_delays(lyrics, delay_times)
