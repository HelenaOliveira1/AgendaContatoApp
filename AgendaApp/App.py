import json

def main():
    while True:
        try:
            f = open("meses.txt", "r", encoding="utf-8")
            linhas = f.readlines()

            for linha in linhas:
                print(linha.strip())

            break

        except FileNotFoundError:
            print("Arquivo não econtrado!")

        except:
            print("Ocorreu um erro!")

if __name__ == "__main__":
    main()