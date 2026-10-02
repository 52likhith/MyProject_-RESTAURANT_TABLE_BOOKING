def is_table_available(
	requested_date: str,
	requested_time: str,
	party_size: int,
	tables: list[dict],
	bookings: list[dict],
) -> bool:
	"""Return whether a suitable table is free for the requested time.

	Each table needs an ``id`` and ``capacity``. Each booking needs a
	``table_id``, ``date``, and ``time``. Dates and times are matched exactly.
	"""
	if party_size <= 0:
		return False

	for table in tables:
		if table["capacity"] < party_size:
			continue

		already_booked = any(
			booking["table_id"] == table["id"]
			and booking["date"] == requested_date
			and booking["time"] == requested_time
			for booking in bookings
		)
		if not already_booked:
			return True

	return False
