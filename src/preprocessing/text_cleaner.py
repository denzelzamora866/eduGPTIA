class TextCleaner:

    def clean(self, text):
        """
        proceso de limpieza.
        """
        text = self.normalize(text)
        text = self.remove_symbols(text)
        return text

    def normalize(self, text):
        """
        minúsculas.
        """
        return text.lower()

    def remove_symbols(self, text):
        """
        Elimina signos de puntuación.
        """
        symbols = ",.;:¡!¿?()[]{}\"'"

        for symbol in symbols:
            text = text.replace(symbol, "")

        return text