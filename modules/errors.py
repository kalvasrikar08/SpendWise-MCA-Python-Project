
import logging

# Logging configuration
logging.basicConfig(
    filename="/content/SpendWise/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom exceptions
class InvalidAmountError(Exception):
    pass

class BudgetExceededError(Exception):
    pass

# Validation function
def validate_amount(amount):

    try:
        if amount <= 0:
            raise InvalidAmountError("Amount must be positive!")

    except InvalidAmountError as error:
        logging.error(str(error))
        print("Error:", error)

    else:
        logging.info("Valid transaction amount")
        print("Amount accepted!")

    finally:
        print("Validation completed.")
