from src.models.model import eduGPTIA
from src.datasets.corpus_builder import CorpusBuilder
from src.tokenizer.tokenizer import Tokenizer
from src.training.trainer import Trainer


def main():

    model = eduGPTIA()

    builder = CorpusBuilder()

    tokenizer = Tokenizer()

    trainer = Trainer(
        builder
    )

    while True:

        option = model.show_menu()

        # ---------------------------------
        # 1. Construir corpus
        # ---------------------------------

        if option == "1":

            builder.build_corpus()

        # ---------------------------------
        # 2. Preparar modelo
        # ---------------------------------

        elif option == "2":

            model.train(
                trainer
            )

        # ---------------------------------
        # 3. Información
        # ---------------------------------

        elif option == "3":

            model.show_information()

        # ---------------------------------
        # 4. Tokenizador manual
        # ---------------------------------

        elif option == "4":

            corpus = (
                builder.load_corpus()
            )

            tokenizer.run(
                corpus,
                "manual"
            )

        # ---------------------------------
        # 0. Salir
        # ---------------------------------

        elif option == "0":

            print(
                "Saliendo del programa..."
            )

            break

        # ---------------------------------
        # Opción incorrecta
        # ---------------------------------

        else:

            print(
                "Opción no válida."
            )


if __name__ == "__main__":

    main()