from datetime import timedelta, datetime
from .Upstack import Event, Interviewer


def test_event_end_calculation():
    new_event = Event(datetime(2020, 1, 1, 12, 00, 00, 00), timedelta(minutes=15))
    expected_end = datetime(2020, 1, 1, 12, 15, 00, 00)
    assert new_event.end == expected_end


def test_Interviewer_add_event_simple_positive():
    new_event = Event(datetime(2020, 1, 1, 12, 00, 00, 00), timedelta(minutes=15))
    new_interviewer = Interviewer(datetime(2020, 1, 1, 8, 00, 00, 00), datetime(2020, 1, 1, 16, 00, 00, 00))
    assert new_interviewer.add_event(new_event)
    assert new_event in new_interviewer.booked_events


def test_Interviewer_add_event__simple_negative_work_start():
    new_event = Event(datetime(2020, 1, 1, 7, 00, 00, 00), timedelta(minutes=15))
    new_interviewer = Interviewer(datetime(2020, 1, 1, 8, 00, 00, 00), datetime(2020, 1, 1, 16, 00, 00, 00))
    assert not new_interviewer.add_event(new_event)
    assert new_event not in new_interviewer.booked_events


def test_Interviewer_add_event__simple_negative_work_end():
    new_event = Event(datetime(2020, 1, 1, 17, 00, 00, 00), timedelta(minutes=15))
    new_interviewer = Interviewer(datetime(2020, 1, 1, 8, 00, 00, 00), datetime(2020, 1, 1, 16, 00, 00, 00))
    assert not new_interviewer.add_event(new_event)
    assert new_event not in new_interviewer.booked_events

def test_Interviewer_add_event__simple_negative_start():
    old_event = Event(datetime(2020, 1, 1, 12, 00, 00, 00), timedelta(minutes=60))
    new_event = Event(datetime(2020, 1, 1, 12, 30, 00, 00), timedelta(minutes=60))
    new_interviewer = Interviewer(datetime(2020, 1, 1, 8, 00, 00, 00), datetime(2020, 1, 1, 16, 00, 00, 00))
    new_interviewer.add_event(old_event)
    assert not new_interviewer.add_event(new_event)
    assert new_event not in new_interviewer.booked_events

def test_Interviewer_add_event__simple_negative_end():
    old_event = Event(datetime(2020, 1, 1, 12, 00, 00, 00), timedelta(minutes=60))
    new_event = Event(datetime(2020, 1, 1, 11, 30, 00, 00), timedelta(minutes=60))
    new_interviewer = Interviewer(datetime(2020, 1, 1, 8, 00, 00, 00), datetime(2020, 1, 1, 16, 00, 00, 00))
    new_interviewer.add_event(old_event)
    assert not new_interviewer.add_event(new_event)
    assert new_event not in new_interviewer.booked_events

def test_Interviewer_add_event__simple_negative_full_overlap():
    old_event = Event(datetime(2020, 1, 1, 12, 00, 00, 00), timedelta(minutes=60))
    new_event = Event(datetime(2020, 1, 1, 11, 30, 00, 00), timedelta(minutes=180))
    new_interviewer = Interviewer(datetime(2020, 1, 1, 8, 00, 00, 00), datetime(2020, 1, 1, 16, 00, 00, 00))
    new_interviewer.add_event(old_event)
    assert not new_interviewer.add_event(new_event)
    assert new_event not in new_interviewer.booked_events
