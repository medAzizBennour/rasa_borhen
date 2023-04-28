

from typing import Dict, Text, Any, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict

from rasa_sdk.events import SlotSet, EventType


class ValidateStockCompany(FormValidationAction):
    def name(self) -> Text:
        return "validate_buy_stock_form"

    @staticmethod
    def securities_list() -> List[Text]:
        """Database of supported cuisines"""

        return ["tesla", "nvidia", "apple","google"]

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
            return {"stock_company": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return {"stock_company": None}