"""
NO MORE DOUBTS - Digital CLI Version
Gra w wersji tekstowej dla pojedynczego gracza
"""

import random
import json
import os
from typing import Dict, List, Tuple
from datetime import datetime

class Card:
    def __init__(self, card_id: int, category: str, text: str, tags: List[str]):
        self.card_id = card_id
        self.category = category  # "no", "more", "doubts"
        self.text = text
        self.tags = tags  # identyfikatory tematyczne do sprawdzania logiki
    
    def __str__(self):
        return f"[{self.category.upper()}] {self.text}"

class GameDatabase:
    """Baza danych z kartami i systemem tagowania"""
    
    def __init__(self):
        self.cards = {
            "doubts": [],
            "more": [],
            "no": []
        }
        self._initialize_cards()
    
    def _initialize_cards(self):
        """Inicjalizacja bazy kart z tagami tematycznymi"""
        
        # DOUBTS - sytuacje wymagające wyjaśnienia
        doubts_data = [
            ("Dlaczego wszyscy mieszkańcy małego miasteczka noszą tylko czerwone buty?", 
             ["city", "people", "clothes", "mystery", "color"]),
            ("Co się stało z wszystkimi lewymi skarpetkami na świecie?", 
             ["clothes", "mystery", "home", "lost"]),
            ("Dlaczego koty zawsze patrzą na pusty róg pokoju?", 
             ["animals", "home", "supernatural", "mystery"]),
            ("Czemu w parku każdego dnia o 15:00 zbierają się tłumy ludzi?", 
             ["park", "people", "time", "routine", "mystery"]),
            ("Dlaczego wszystkie zegary w mieście spieszczą się o 3 minuty?", 
             ["time", "city", "technology", "mystery"]),
            ("Co oznaczają dziwne symbole pojawiające się na murach?", 
             ["city", "symbols", "mystery", "communication"]),
            ("Dlaczego ptaki unikają lądowania w centrum miasta?", 
             ["animals", "city", "nature", "mystery"]),
            ("Czemu wszyscy sąsiedzi wychodzą z domu dokładnie o tej samej porze?", 
             ["people", "routine", "mystery", "home"]),
        ]
        
        # MORE - szczegóły uzupełniające
        more_data = [
            ("Pojawia się dziwny zapach wanilii", ["smell", "mystery", "supernatural"]),
            ("Wszyscy mówią szeptem", ["people", "communication", "mystery"]),
            ("Wydarzenie powtarza się co pełnię księżyca", ["time", "routine", "supernatural"]),
            ("Słychać dźwięki kroków na poddaszu", ["home", "mystery", "supernatural"]),
            ("Temperatura zawsze spada o 5 stopni", ["weather", "mystery", "supernatural"]),
            ("Pojawiają się ślady dziwnych stóp", ["mystery", "animals", "supernatural"]),
            ("Wszystkie aparaty fotograficzne się psują", ["technology", "mystery", "supernatural"]),
            ("Dzieci zaczynają śpiewać tę samą piosenkę", ["people", "mystery", "communication"]),
            ("Elektryczność migocze w całej okolicy", ["technology", "mystery", "city"]),
            ("Pojawiają się nieznane wcześniej rośliny", ["nature", "mystery", "supernatural"]),
        ]
        
        # NO - pewne odpowiedzi/wyjaśnienia
        no_data = [
            ("To międzynarodowy spisek sprzedawców obuwia", ["conspiracy", "commercial", "people"]),
            ("Istnieje portal do krainy zaginionych rzeczy", ["supernatural", "mystery", "lost"]),
            ("Widzą duchy poprzednich mieszkańców", ["supernatural", "mystery", "home"]),
            ("To efekt lokalnego pola magnetycznego", ["science", "technology", "mystery"]),
            ("Ukryty nadajnik kontroluje ich zachowanie", ["technology", "conspiracy", "people"]),
            ("To sekretny eksperyment rządowy", ["conspiracy", "government", "science"]),
            ("Miejscowy artysta tworzy instalację miejską", ["art", "city", "people"]),
            ("To tradycja przekazywana z pokolenia na pokolenie", ["culture", "people", "routine"]),
            ("Badacze testują nową teorię naukową", ["science", "people", "mystery"]),
            ("To skutek działania nowego leku na alergię", ["medicine", "science", "people"]),
        ]
        
        # Tworzenie obiektów Card
        for i, (text, tags) in enumerate(doubts_data):
            self.cards["doubts"].append(Card(i, "doubts", text, tags))
        
        for i, (text, tags) in enumerate(more_data):
            self.cards["more"].append(Card(i, "more", text, tags))
        
        for i, (text, tags) in enumerate(no_data):
            self.cards["no"].append(Card(i, "no", text, tags))

class LogicAnalyzer:
    """System analizy logiki historii oparty na tagach"""
    
    @staticmethod
    def calculate_story_score(doubts_card: Card, more_card: Card, no_card: Card) -> Tuple[int, str]:
        """
        Oblicza punkty za spójność logiczną historii
        Zwraca (punkty, uzasadnienie)
        """
        all_tags = doubts_card.tags + more_card.tags + no_card.tags
        common_tags = set(doubts_card.tags) & set(more_card.tags) & set(no_card.tags)
        pair_matches = (
            len(set(doubts_card.tags) & set(more_card.tags)) +
            len(set(doubts_card.tags) & set(no_card.tags)) +
            len(set(more_card.tags) & set(no_card.tags))
        )
        
        # Obliczanie punktów
        score = 0
        justification = []
        
        # Punkty za wspólne tagi wszystkich kart
        if len(common_tags) >= 2:
            score += 5
            justification.append(f"Doskonała spójność tematyczna ({', '.join(common_tags)})")
        elif len(common_tags) == 1:
            score += 3
            justification.append(f"Dobra spójność tematyczna ({list(common_tags)[0]})")
        
        # Punkty za pary kart
        if pair_matches >= 4:
            score += 3
            justification.append("Świetne połączenia między kartami")
        elif pair_matches >= 2:
            score += 2
            justification.append("Dobre połączenia między kartami")
        elif pair_matches >= 1:
            score += 1
            justification.append("Podstawowe połączenia między kartami")
        
        # Bonus za specjalne kombinacje
        if "mystery" in doubts_card.tags and "supernatural" in more_card.tags and "science" in no_card.tags:
            score += 2
            justification.append("Bonus: Rozwiązanie naukowe zagadki supernatural")
        
        if "people" in all_tags and "routine" in all_tags:
            score += 1
            justification.append("Bonus: Historia o ludzkich zachowaniach")
        
        # Minimalne punkty
        if score == 0:
            score = 1
            justification.append("Podstawowe punkty za próbę")
        
        return score, " | ".join(justification)

class PlayerStats:
    """System statystyk gracza"""
    
    def __init__(self):
        self.total_games = 0
        self.total_score = 0
        self.best_score = 0
        self.best_story = ""
        self.favorite_tags = {}
        self.history = []
    
    def update(self, score: int, story: str, tags: List[str]):
        """Aktualizacja statystyk po grze"""
        self.total_games += 1
        self.total_score += score
        
        if score > self.best_score:
            self.best_score = score
            self.best_story = story
        
        # Śledzenie ulubionych tagów
        for tag in tags:
            self.favorite_tags[tag] = self.favorite_tags.get(tag, 0) + 1
        
        # Historia gier
        self.history.append({
            'date': datetime.now().isoformat(),
            'score': score,
            'story': story
        })
        
        # Zachowaj tylko ostatnie 20 gier
        if len(self.history) > 20:
            self.history = self.history[-20:]
    
    def get_average_score(self) -> float:
        """Średni wynik"""
        return self.total_score / max(1, self.total_games)
    
    def get_top_tags(self, limit=5) -> List[Tuple[str, int]]:
        """Najpopularniejsze tagi gracza"""
        return sorted(self.favorite_tags.items(), key=lambda x: x[1], reverse=True)[:limit]

class NoMoreDoubtsGame:
    """Główna klasa gry"""
    
    def __init__(self):
        self.db = GameDatabase()
        self.analyzer = LogicAnalyzer()
        self.stats_file = "nmd_stats.json"
        self.stats = self._load_stats()
    
    def _load_stats(self) -> PlayerStats:
        """Wczytywanie statystyk gracza"""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    stats = PlayerStats()
                    stats.__dict__.update(data)
                    return stats
            except:
                pass
        return PlayerStats()
    
    def _save_stats(self):
        """Zapisywanie statystyk gracza"""
        try:
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(self.stats.__dict__, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Błąd zapisywania statystyk: {e}")
    
    def display_menu(self):
        """Główne menu gry"""
        print("\n" + "="*60)
        print("🎮 NO MORE DOUBTS - Digital Edition 🎮")
        print("="*60)
        print("1. 🎯 Nowa gra")
        print("2. 📊 Statystyki")
        print("3. 📚 Historia gier")
        print("4. ❓ Zasady gry")
        print("5. 🚪 Wyjście")
        print("="*60)
    
    def display_rules(self):
        """Wyświetlanie zasad gry"""
        print("\n" + "📖 ZASADY GRY" + "="*48)
        print("""
🎯 CEL: Stwórz logiczną historię łącząc karty z trzech kategorii

📋 KATEGORIE KART:
• DOUBTS (niebieskie) - zagadkowe sytuacje wymagające wyjaśnienia
• MORE (żółte) - dodatkowe szczegóły i okoliczności  
• NO (czerwone) - pewne odpowiedzi i wyjaśnienia

🎲 ROZGRYWKA:
1. Otrzymujesz po 3 losowe karty z każdej kategorii
2. Wybierasz po 1 karcie z każdej kategorii
3. Układasz historię w kolejności: DOUBTS → MORE → NO
4. System ocenia logikę Twojej historii (0-10+ punktów)

🏆 PUNKTACJA:
• Wspólne tagi między kartami = więcej punktów
• Spójność tematyczna = bonusowe punkty
• Specjalne kombinacje = dodatkowe bonusy

💾 POSTĘP: Gra zapisuje Twoje statystyki i najlepsze historie!
        """)
        input("\nNaciśnij Enter, aby wrócić do menu...")
    
    def play_game(self):
        """Główna pętla rozgrywki"""
        print("\n" + "🎮 NOWA GRA" + "="*50)
        
        # Losowanie kart
        hand = {
            "doubts": random.sample(self.db.cards["doubts"], 3),
            "more": random.sample(self.db.cards["more"], 3),
            "no": random.sample(self.db.cards["no"], 3)
        }
        
        print("Twoja ręka kart:\n")
        
        # Wyświetlanie kart z numeracją
        for category in ["doubts", "more", "no"]:
            print(f"🔸 {category.upper()}:")
            for i, card in enumerate(hand[category], 1):
                print(f"   {i}. {card.text}")
            print()
        
        # Wybór kart przez gracza
        selected_cards = {}
        for category in ["doubts", "more", "no"]:
            while True:
                try:
                    choice = int(input(f"Wybierz kartę {category.upper()} (1-3): ")) - 1
                    if 0 <= choice < 3:
                        selected_cards[category] = hand[category][choice]
                        break
                    else:
                        print("Wybierz numer od 1 do 3!")
                except ValueError:
                    print("Wpisz poprawny numer!")
        
        # Tworzenie historii
        print("\n" + "📖 TWOJA HISTORIA" + "="*44)
        print(f"❓ ZAGADKA: {selected_cards['doubts'].text}")
        print(f"➕ SZCZEGÓŁY: {selected_cards['more'].text}")
        print(f"✅ ROZWIĄZANIE: {selected_cards['no'].text}")
        
        # Analiza logiki
        score, justification = self.analyzer.calculate_story_score(
            selected_cards['doubts'],
            selected_cards['more'], 
            selected_cards['no']
        )
        
        print(f"\n🏆 WYNIK: {score} punktów")
        print(f"💡 UZASADNIENIE: {justification}")
        
        # Aktualizacja statystyk
        story_text = f"{selected_cards['doubts'].text} | {selected_cards['more'].text} | {selected_cards['no'].text}"
        all_tags = selected_cards['doubts'].tags + selected_cards['more'].tags + selected_cards['no'].tags
        
        self.stats.update(score, story_text, all_tags)
        self._save_stats()
        
        # Motywacyjna wiadomość
        if score >= 8:
            print("\n🌟 Doskonała historia! Jesteś prawdziwym storytellerem!")
        elif score >= 5:
            print("\n👏 Świetna robota! Historia ma sens i jest ciekawa!")
        elif score >= 3:
            print("\n👍 Niezła próba! Następnym razem pójdzie jeszcze lepiej!")
        else:
            print("\n💪 Nie poddawaj się! Każda historia to nauka!")
        
        input("\nNaciśnij Enter, aby wrócić do menu...")
    
    def display_stats(self):
        """Wyświetlanie statystyk gracza"""
        print("\n" + "📊 TWOJE STATYSTYKI" + "="*42)
        print(f"🎮 Rozegrane gry: {self.stats.total_games}")
        print(f"🏆 Najlepszy wynik: {self.stats.best_score}")
        print(f"📈 Średni wynik: {self.stats.get_average_score():.1f}")
        print(f"🎯 Suma punktów: {self.stats.total_score}")
        
        if self.stats.best_story:
            print(f"\n⭐ NAJLEPSZA HISTORIA:")
            print(f"   {self.stats.best_story}")
        
        top_tags = self.stats.get_top_tags()
        if top_tags:
            print(f"\n🏷️  ULUBIONE TEMATY:")
            for tag, count in top_tags:
                print(f"   • {tag}: {count} razy")
        
        input("\nNaciśnij Enter, aby wrócić do menu...")
    
    def display_history(self):
        """Wyświetlanie historii gier"""
        print("\n" + "📚 HISTORIA GIER" + "="*45)
        
        if not self.stats.history:
            print("Nie rozegrałeś jeszcze żadnej gry!")
        else:
            for i, game in enumerate(reversed(self.stats.history[-10:]), 1):
                date = game['date'][:19].replace('T', ' ')
                print(f"{i:2}. [{date}] {game['score']} pkt: {game['story'][:80]}...")
        
        input("\nNaciśnij Enter, aby wrócić do menu...")
    
    ## TUTAJ
    while True:
        self.display_menu()
        choice = input("Wybierz opcję (1-5): ")
        
        if choice == "1":
            self.play_game()
        elif choice == "2":
            self.display_stats()
        elif choice == "3":
            self.display_history()
        elif choice == "4":
            self.display_rules()
        elif choice == "5":
            print("\n👋 Dzięki za grę! Do zobaczenia!")
            break
        else:
            print("❌ Nieprawidłowy wybór! Wybierz opcję 1-5.")

if __name__ == "__main__":
    game = NoMoreDoubtsGame()
    game.run()

