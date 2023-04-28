

from typing import Dict, Text, Any, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict

from rasa_sdk.events import SlotSet, EventType


class ValidatePage(FormValidationAction):
    def name(self) -> Text:
        return "validate_page"

    @staticmethod
    def securities_list() -> List[Text]:
        """Database of supported cuisines"""
        pages_list = ["orders", "placements", "dashboard","setting","profile","portfolio"]

        return pages_list

    def validate_stock(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate stock value."""

        if slot_value.lower() in self.securities_list():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"page": slot_value}
        else:
            response_message="Invalid page"
        


            dispatcher.utter_message(text=response_message)
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"page": None}