#!/usr/bin/python3
# Classe représentant un Checkbook
class Checkbook:
    # Constructeur : initialise un solde à zéro
    def __init__(self):
        self.balance = 0.0  # Solde initial

    # Méthode pour effectuer un dépôt
    def deposit(self, amount):
        # Ajouter le montant au solde
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))  # Confirmation du dépôt
        print("Current Balance: ${:.2f}".format(self.balance))  # Afficher le solde actuel

    # Méthode pour effectuer un retrait
    def withdraw(self, amount):
        # Vérification : est-ce que le solde est suffisant ?
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")  # Erreur si fonds insuffisants
        else:
            # Déduction du montant du solde
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))  # Confirmation du retrait
            print("Current Balance: ${:.2f}".format(self.balance))  # Afficher le solde actuel

    # Méthode pour afficher le solde actuel
    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))  # Affichage du solde

# Fonction principale du programme
def main():
    # Création d'une instance de Checkbook
    cb = Checkbook()

    # Boucle principale : interagir avec l'utilisateur
    while True:
        # Demande à l'utilisateur ce qu'il souhaite faire
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        
        # Option de sortie
        if action == 'exit':
            print("Thank you for using Checkbook. Goodbye!")
            break
        # Option pour effectuer un dépôt
        elif action == 'deposit':
            try:
                # Saisie et validation du montant à déposer
                amount = float(input("Enter the amount to deposit: $"))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        # Option pour effectuer un retrait
        elif action == 'withdraw':
            try:
                # Saisie et validation du montant à retirer
                amount = float(input("Enter the amount to withdraw: $"))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        # Option pour afficher le solde
        elif action == 'balance':
            cb.get_balance()
        # Commande invalide
        else:
            print("Invalid command. Please try again.")

# Point d'entrée du programme
if __name__ == "__main__":
    main()