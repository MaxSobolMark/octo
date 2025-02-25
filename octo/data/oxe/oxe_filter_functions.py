from typing import Any, Dict


def roboturk_filter_function(trajectory: Dict[str, Any]) -> bool:
    return (
        trajectory["observation"]["natural_language_instruction"][0] == "layout laundry"
    )


OXE_FILTER_FUNCTIONS = {"roboturk": roboturk_filter_function}
