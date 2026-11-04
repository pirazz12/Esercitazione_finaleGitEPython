class Studente:
    def __init__(self, matricola: str, cognome: str, eta: int, media_voti: float) -> None:
        self.matricola: str = matricola
        self.cognome: str = cognome
        self.eta: int = eta
        self.media_voti: float = media_voti
        
    def esito(self) -> str:
        if self.media_voti >= 6.0:
            return "PROMOSSO"
        else:
            return "RISERVA"
    
    def __str__(self) -> str:
        return f"[{self.matricola}] {self.cognome} - {self.eta} anni | Media: {self.media_voti} ({self.esito()})"


class Scuola:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.studenti: dict[str, Studente] = {}
    
    def aggiungi_studente(self, studente: Studente) -> None:
        if studente.matricola in self.studenti:
            raise ValueError(f"Matricola {studente.matricola} già esistente!")
        else:
            self.studenti[studente.matricola] = studente
    
    def cerca_per_cognome(self, cognome: str) -> list[Studente]:
        risultati = [s for s in self.studenti.values() if s.cognome.lower() == cognome.lower()]
        return risultati
        
    def recuperi(self) -> list[Studente]:
        return [s for s in self.studenti.values() if s.esito() == "RISERVA"]


def menu() -> None:
    scuola = Scuola("ITIS Volta")

    while True:
        print("\n--- GESTIONE REGISTRO SCUOLA ---")
        print("1. Aggiungi studente")
        print("2. Cerca per cognome")
        print("3. Mostra studenti in recupero")
        print("0. Esci")
        
        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            mat = input("Matricola: ")
            cognome = input("Cognome: ")
            eta = int(input("Età: "))
            media = float(input("Media voti: "))
            
            try:
                scuola.aggiungi_studente(Studente(mat, cognome, eta, media))
                print(f"-> Studente '{cognome}' aggiunto con successo!")
            except ValueError as e:
                print(f"ERRORE: {e}")

        elif scelta == "2":
            cognome_cercato = input("Inserisci il cognome da cercare: ")
            trovati = scuola.cerca_per_cognome(cognome_cercato)
            if trovati:
                print(f"Studenti trovati per '{cognome_cercato}':")
                for s in trovati:
                    print(f"  * {s}")
            else:
                print("Nessun studente trovato con questo cognome.")

        elif scelta == "3":
            in_recupero = scuola.recuperi()
            if in_recupero:
                print("Studenti con esito RISERVA:")
                for s in in_recupero:
                    print(f"  * {s}")
            else:
                print("Nessun studente a rischio recupero!")

        elif scelta == "0":
            print("Chiusura del programma...")
            break
            
        else:
            print("Opzione non valida, riprova.")


if __name__ == "__main__":
    menu()