from googlesearch import search




print('''  
           .    _  .       _____________
         |\_|/__/|    /                       \ 
       / / \/ \  \   / Telegram          \
      /__|O||O|__ \ \     @OxD3vil  /
     |/_ \_/\_/ _\ | \  ___________/
     | | (____) | ||  |/
     \/\___/\__/  // _/
     (_/         ||
      |          ||\
      \        //_/ 
        \______//
       __|| __||
     (____(____)
    
      ''')
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

while True:
    dork = input("Enter the dork to search for (or type 'exit' to quit): ")
    if dork.lower() == 'exit':
        break

    print_colored("You entered: " + dork, "32")

    num_results = 50

    blacklist = ["exploit-db.com", "github.com", "drupal.org", "stackoverflow.com", "archive.org", "php.net", "facebook.com", "w3schools.com", "instagram.com", "owasp.org","learn.helmo.be","php.id"]

    forum_blacklist = ["exampleforum.com", "anotherforum.org"]

    combined_blacklist = blacklist + forum_blacklist

    search_results = search(dork, num_results=num_results)

    filtered_results = [result for result in search_results if not any(site in result for site in combined_blacklist)]

    print_colored("Websites matching the dork (excluding blacklist):", "36")
    for result in filtered_results:
        print_colored(result, "36")