Kurs: Programmering och systemering.
Vald slutuppgift: "Mataffären"
Datum: 2022-10-05

Programmet kräver följande filer för att köras: 
    - main.py
    - cart.py
    - products.py
    - import_products.py
  
Programmet skapar följande filer under körning:
    - products.db
    - orders.csv

main.py
Programmet körs från denna fil samt innehåller vissa funktioner som ej tillhör klasser, men som krävs för programmets funktionalitet.

Vid körning presenteras anvädaren för en meny med följande sju val: 
1. Load items to database.
2. List available items.
3. Add item to cart.
4. View items in cart.
5. Remove item from cart.
6. Save order.
7. Quit shopping.

Beskrivning av menyval:
1. Load items to database.
   - Användare kan här lägga till produkter till databas via en korrekt formaterad CSV-fil.
   via detta menyval skapas även databasen "products.db" samt "orders.csv" som används för att lagra ordrar.
2. List available items.
    - Listar valbara produkter i sortimentet.
3. Add item to cart.
    - Adderar produkter till varukorgen. Varukorgen presenteras grafiskt samt visar produktens enskilda kostnad och totala beloppet för valda produkter.
4. View items in cart.
    - Snabbväg för att visa varukorgen direkt från huvudmeny.
5. Remove item from cart.
    - Ger användaren möjlighet att ta bort ej önskvärda produkter från sin varukorg. Varukorgen uppdateras samt visas grafiskt för användaren. 
6. Save order.
    - Presenterar användaren med aktuell varukorg och ger denne möjlighet att lägga sin order.
    Lagda ordrar sparas i "orders.csv" med kommaseparerade värden. 
7. Quit shopping.
    - Avslutar programmet direkt om varukorgen är tom. Om det finns produkter i varukorgen frågas användaren om han vill gå avsluta programmet eller fortsätta.

cart.py
Används av klassen "Cart" som håller alla produkter i användarens varukorg samt följande klassmetoder för att hantera varukorgen:
- Funktion "add_item"
    - Funktionen hämtar samtliga produkter från databasen och jämför detta med kundens val för att garantera korrekta val. 
      Hjälp till funktionen har hämtats från: https://stackoverflow.com/questions/14835852/convert-sql-result-to-list-python

- Funktion "view_cart"
    - Funktionen hämtar information om produkterna i kundens varukorg från databasen samt presenterar dessa grafiskt och räknar ut totalsumma.
      Hjälp till funktionen har hämtats från: https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

- Funktion "remove_item"
    - Funktionen låter användaren ta bort produkter ur varukorgen.
      Viss inspiration har hämtats från: https://stackoverflow.com/questions/52565505/simplest-way-to-delete-object-from-list-of-objects 

products.py

Innehåller klassen "Product" samt dess instansvariabler:
- articleNumber
- name
- price

import_products.py

Innehåller funktioner för att hantera skapande av databas, import av produkter samt skapande av fil för lagring av ordrar.

Funktioner:
- connection_to_DB
    - För att minska skrivning av kod vid uppkoppling till databas.
    - Kod tagen från: https://stackoverflow.com/questions/29246118/python-database-connection-in-function

- import_products.py
    - Hanterar skapande av databas, import av produkter från csv-fil samt skapande av fil för lagring av ordrar.


Databaser / filer för lagring

- products.db
    - lagrar information om samtliga produkter som importeras via CSV-filer. Databasen innehåller fält "articleNumber", "name", "price". Databasen är konstruerad på så sätt att inga produkter med samma artikelnummer skall kunna sparas. 

- orders.csv
  - Innehåller lagrad information om orders. 
  Formatet ser ut på följande vis:
    Time for order,      Order ID,  articleNumbers...
    2022/10/05/ 12:38:51,OrderId: 1,5,6




