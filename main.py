class FindKaprekarNumber():
    def __init__(self):
        """
        FindKaprekarNumber constructor.
        Args:
        """
    @staticmethod
    def ordenar_digitos(numero):
        digitos = str(numero)
        parte_a = int(''.join(sorted(digitos, reverse=True)))
        parte_b = int(''.join(sorted(digitos)))
        return parte_a, parte_b

    def calcular_diferencia(self, numero):
        iteracion = 1
        diferencia = None
        archivo_resultados = open("resultados.txt", "w")
        archivo_resultados.write("Cálculo;ParteA;ParteB;Diferencia;Observaciones\n")

        while diferencia != 6174:
            parte_a, parte_b = self.ordenar_digitos(numero)
            diferencia = abs(parte_a - parte_b)
            observaciones = f"Iteración {iteracion}"

            archivo_resultados.write(f"{numero};{parte_a};{parte_b};{diferencia};{observaciones}\n")

            if diferencia == 6174:
                observaciones += ", ¡¡¡KAPREKAR Encontrado!!!"
                archivo_resultados.write(f"{numero};{parte_a};{parte_b};{diferencia};{observaciones}\n")
                break

            iteracion += 1
            numero = str(diferencia).zfill(4)

        archivo_resultados.close()
        return iteracion

    def main(self, numero_leido):
        numero_leido = numero_leido.zfill(4)

        if len(set(numero_leido)) == 1:
            print("Los 4 dígitos no pueden ser iguales.")
        else:
            iteraciones = self.calcular_diferencia(numero_leido)
            print("Cálculos realizados. Los resultados se han guardado en 'resultados.txt'.")

        return iteraciones

if __name__ == "__main__":
    find_kaprekar_obj = FindKaprekarNumber()
    numero_leido = '9258'
    find_kaprekar_obj.main(numero_leido)
