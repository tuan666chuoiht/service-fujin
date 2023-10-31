from typing import Union


class ConditionalCheck:
    @staticmethod
    def is_null(input_check: Union[str, None]) -> bool:
        """Checks whether the argument is either None or zero-length

        Args:
            input (Union[str, None]): The input to be null-checked

        Returns:
            null_check: A boolean value representing if the object is null.
        """
        return input is None or len(input_check) == 0 or input == "None"


conditional_check = ConditionalCheck()
