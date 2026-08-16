import re


class TextCleaner:

    def clean(self, text):

        """
        Limpia el texto antes de tokenizarlo.
        """

        text = text.lower()

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        text = text.strip()

        return text