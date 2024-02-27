def choose_category(categories):
    print(categories)
    chosen_category = input("Choose a category: ")
    if chosen_category in categories:
        print(chosen_category)
    else:
        print("Invalid category")
        return choose_category(categories)
categories=["category1", "category2", "category3", "category4"]
choose_category(categories)        