# 강의실 예약 시스템 — 아래 클래스를 완성하세요. (클래스·메서드 이름은 바꾸지 마세요)

ROOMS = ("A101", "A102", "B201")
DAYS = ("월", "화", "수", "목", "금")
OPEN, CLOSE = 9, 21
MAX_HOURS = 3
MAX_PER_DAY = 2


def _is_int(x):
    # True/False는 정수로 보지 않음 (규칙 2)
    return isinstance(x, int) and not isinstance(x, bool)


class RoomBooking:
    def __init__(self):
        # (room, day) -> [(start, end, name), ...]
        self._data = {}

    def book(self, room, day, start, end, name):
        if room not in ROOMS or day not in DAYS:          # 규칙 1
            return False
        if not isinstance(name, str) or not name.strip(): # 이름 없음 (추가 규칙)
            return False
        if not _is_int(start) or not _is_int(end):        # 규칙 2
            return False
        if start < OPEN or end > CLOSE:                   # 규칙 3
            return False
        if start >= end:                                  # 규칙 4
            return False
        if end - start > MAX_HOURS:                       # 규칙 5
            return False
        for s, e, _ in self._data.get((room, day), []):   # 규칙 6
            if start < e and s < end:
                return False
        count = 0                                         # 규칙 7
        for r in ROOMS:
            for _, _, n in self._data.get((r, day), []):
                if n == name:
                    count += 1
        if count >= MAX_PER_DAY:
            return False
        self._data.setdefault((room, day), []).append((start, end, name))
        return True

    def cancel(self, room, day, start, name):
        if room not in ROOMS or day not in DAYS or not _is_int(start):
            return False
        items = self._data.get((room, day), [])
        for i, (s, e, n) in enumerate(items):
            if s == start:
                if n != name:
                    return False
                del items[i]
                return True
        return False

    def get_schedule(self, room, day):
        if room not in ROOMS or day not in DAYS:
            return []
        items = self._data.get((room, day), [])
        return sorted(items, key=lambda x: x[0])
