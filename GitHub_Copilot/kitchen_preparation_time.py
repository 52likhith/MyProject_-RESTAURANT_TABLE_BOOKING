def estimate_preparation_time(selected_items: list[dict]) -> int:
	"""Return the total estimated preparation time in minutes.

	Each selected item must include a ``preparation_time`` value in minutes.
	The estimate assumes the items are prepared one after another.
	"""
	return sum(item["preparation_time"] for item in selected_items)
