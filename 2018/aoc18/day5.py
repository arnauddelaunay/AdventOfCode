import pandas as pd
import datetime
import numpy as np

from .aoc import AOCDay


def split_phrase(phrase):
    splitted = phrase.split('] ')
    return (
        datetime.datetime.strptime(splitted[0][1:], "%Y-%m-%d %H:%M"),
        splitted[1].strip()
    )


def get_guard_id(event):
    return event.split("#")[-1].split(" ")[0]


class AOCDay5(AOCDay):

    def __init__(self):
        self.day = 5
        self.split_lines = False

    def run1(self, inp):
        dts, events = zip(*map(split_phrase, inp))
        df = pd.DataFrame({"date": dts, "event": events}).sort_values("date")
        guards = {}
        for df_idx, event in df.event.iteritems():
            if "Guard" in event:
                guard_id = get_guard_id(event)
                if guard_id not in guards:
                    guards[guard_id] = np.zeros(60)
            elif "falls" in event:
                start = df.loc[df_idx, "date"].minute
            else:
                stop = df.loc[df_idx, "date"].minute
                guards[guard_id][start:stop] = guards[guard_id][start:stop] + 1
        guard_ids, hours_asleep = zip(*(map(lambda pair: (int(pair[0]), pair[1].sum()), guards.items())))
        my_g_id = guard_ids[np.argmax(hours_asleep)]
        self.guards = guards
        return my_g_id * guards[str(my_g_id)].argmax()

    def run2(self, inp):
        guard_ids, count, minutes_most_asleep = zip(*(map(
            lambda pair: (int(pair[0]), pair[1].max(), pair[1].argmax()),
            self.guards.items()
        )))
        my_g_id = guard_ids[np.argmax(count)]
        return my_g_id * minutes_most_asleep[np.argmax(count)]
