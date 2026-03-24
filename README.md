Python Hangman Game 🪓
Un'implementazione robusta e modulare del classico gioco dell'Impiccato, sviluppata in Python con un'attenzione particolare alla User Experience (UX) e alla pulizia del codice.

Features 🎮
Modular Architecture: Il gioco è strutturato in funzioni indipendenti (get_masked_word, play, main), facilitando la manutenzione e la leggibilità.

Smart Input Validation: Sistema di controllo integrato che utilizza .isalpha() per bloccare numeri e simboli, impedendo all'utente di sprecare vite per errore.

Duplicate Guess Protection: Il programma riconosce se una lettera è già stata inserita (sia tra le corrette che tra le errate) e avvisa l'utente senza applicare penalità.

Persistent Scoring System: Tiene traccia delle vittorie consecutive durante la sessione, mostrando il punteggio totale al momento dell'uscita.

Dynamic Visuals: Integrazione fluida di arte ASCII tramite il modulo hangman_art, sincronizzata con lo stato delle vite del giocatore.

Clean UI Flow: Utilizzo strategico di os.system e time.sleep per una transizione fluida tra i turni e una console sempre ordinata.

Game Rules 📋
Obiettivo: Indovinare la parola segreta una lettera alla volta prima di esaurire i 6 tentativi.

Gameplay:

L'utente inserisce una lettera.

Se la lettera è corretta, viene rivelata nella parola mascherata.

Se la lettera è errata, il "boia" avanza di uno stadio.

È possibile tentare di indovinare la parola intera in qualsiasi momento per una vittoria istantanea.

Game Over: Il gioco termina quando la parola è completa (Vittoria) o quando i tentativi arrivano a zero (Sconfitta).

Project Structure 📁
Plaintext
hangman-project/
├── main.py
├── hangmanworkflow.drawio.pdf
├── algoritmo_hangman.txt
├── hangman_image.py           # Logica principale e Entry Point
├── hangman_art.py             # Asset grafici (Logo e Stages ASCII)
├── hangman_words_real.py      # Database delle parole segrete
└── README.md                  # Questo file
Main Functions Overview:
clear_screen() - Pulisce il terminale e ristampa il logo per un'interfaccia sempre pulita.

get_masked_word() - Genera dinamicamente la stringa con i placeholder (_) basandosi sui progressi dell'utente.

play() - Gestisce l'intera logica di un singolo round (vite, input, controlli).

get_valid_input() - Helper per gestire le scelte di navigazione (Sì/No) con tolleranza agli errori.

main() - Coordina il loop delle partite, la selezione della parola e il punteggio globale.

Requirements ✅
Python 3.x

Nessuna dipendenza esterna (utilizza solo i moduli standard os, random, time).

Installation & Setup 🚀
Clona il repository:

Bash
git clone https://github.com/FrontN/python-hangman.git
cd python-hangman
Esegui il gioco:

Bash
python main.py
Technical Highlights 💡
List Comprehensions: Utilizzate per una gestione efficiente della mascheratura delle parole.

State-to-Index Mapping: La visualizzazione del boia è legata direttamente all'indice delle vite residue: stages[total_lives].

Fail-Safe Input: Ogni inserimento è normalizzato con .lower() e validato per garantire la stabilità del programma.

Author 👨‍💻
FrontN - Sviluppato come esercizio avanzato per l'applicazione di principi di programmazione modulare e Clean Code in Python.

Good luck, and don't let the man hang! 🧗‍♂️
