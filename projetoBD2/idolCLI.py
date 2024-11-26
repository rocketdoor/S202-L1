from database import Database
from idolDatabase import IdolDatabase


def main():
    db = Database("bolt://34.239.119.224", "neo4j", "deserters-packs-levers")
    db.drop_all()
    idb = IdolDatabase(db)
    option = ""
    while option != "5":
        print("Select an option:")
        print("1. Idol")
        print("2. Group")
        print("3. Company")
        print("4. Show")
        print("5. Exit")
        option = input()
        if option == "1":
            print("Select an option:")
            print("1. Create")
            print("2. Insert")
            print("3. Read")
            print("4. Update")
            print("5. Delete")
            print("6. Exit")
            option = input()
            if option == "1":
                name = input("Enter the name of the idol: ")
                age = input("Enter the age of the idol: ")
                country = input("Enter the country of the idol: ")
                full_name = input("Enter the full name of the idol: ")
                idol_id = input("Enter the ID of the idol: ")
                idb.create_idol(name, age, country, full_name, idol_id)
            elif option == "2":
                print("1. Into Group")
                print("2. Into Show")
                print("3. Exit")
                option = input()
                if option == "1":
                    idol_id = input("Enter the ID of the idol: ")
                    group_id = input("Enter the ID of the group: ")
                    idb.insert_idol_group(idol_id, group_id)
                elif option == "2":
                    idol_id = input("Enter the ID of the idol: ")
                    show_id = input("Enter the ID of the show: ")
                    idb.insert_idol_show(idol_id, show_id)
                elif option == "3":
                    break

            elif option == "3":
                idol_id = input("Enter ID of the idol: ")
                idol = idb.get_idol(idol_id)
                print(idol)
            elif option == "4":
                print("Everything will be updated, if you don't want to update something, just input the previous value")
                idol_id = input("Enter the ID to search for the idol: ")
                new_idol_id = input("Enter the new ID of the idol: ")
                name = input("Enter the new name of the idol: ")
                age = input("Enter the new age of the idol: ")
                country = input("Enter the new country of the idol: ")
                full_name = input("Enter the new full name of the idol: ")
                idb.update_idol(idol_id, new_idol_id, name, age, country, full_name)
            elif option == "5":
                idol_id = input("Enter the ID of the idol: ")
                idb.delete_idol(idol_id)
            elif option == "6":
                break
        elif option == "2":
            print("Select an option:")
            print("1. Create")
            print("2. Insert")
            print("3. Read")
            print("4. Update")
            print("5. Delete")
            print("6. Exit")
            option = input()
            if option == "1":
                name = input("Enter the name of the group: ")
                debut = input("Enter the debut of the group: ")
                group_id = input("Enter the ID of the group: ")
                idb.create_group(name, debut, group_id)
            elif option == "2":
                print("1. Into Company")
                print("2. Into Show")
                print("3. Exit")
                option = input()
                if option == "1":
                    group_id = input("Enter the ID of the group: ")
                    company_id = input("Enter the ID of the company: ")
                    idb.insert_group_company(group_id, company_id)
                elif option == "2":
                    group_id = input("Enter the ID of the group: ")
                    show_id = input("Enter the ID of the show: ")
                    idb.insert_group_show(group_id, show_id)
                elif option == "3":
                    break
            elif option == "3":
                group_id = input("Enter the ID of the group: ")
                group = idb.get_group(group_id)
                print(group)
            elif option == "4":
                print("Everything will be updated, if you don't want to update something, just input the previous value")
                group_id = input("Enter the ID to search the group: ")
                new_group_id = input("Enter the new group id of the group: ")
                name = input("Enter the new name of the group: ")
                debut = input("Enter the new debut of the group: ")
                idb.update_group(group_id, new_group_id, name, debut)
            elif option == "5":
                group_id = input("Enter the ID of the group: ")
                idb.delete_group(group_id)
            elif option == "6":
                break
        elif option == "3":
            print("Select an option:")
            print("1. Create")
            print("2. Read")
            print("3. Update")
            print("4. Delete")
            print("5. Exit")
            option = input()
            if option == "1":
                name = input("Enter the name of the company: ")
                company_id = input("Enter the ID of the company: ")
                idb.create_company(name, company_id)
            elif option == "2":
                company_id = input("Enter the ID of the company: ")
                company = idb.get_company(company_id)
                print(company)
            elif option == "3":
                print("Everything will be updated, if you don't want to update something, just input the previous value")
                company_id = input("Enter the ID to search for the company: ")
                new_company_id = input("Enter the new ID of the company: ")
                name = input("Enter the enw name of the company: ")
                idb.update_company(company_id, new_company_id, name)
            elif option == "4":
                company_id = input("Enter the ID of the company: ")
                idb.delete_company(company_id)
            elif option == "5":
                break
        elif option == "4":
            print("Select an option:")
            print("1. Create")
            print("2. Read")
            print("3. Update")
            print("4. Delete")
            print("5. Exit")
            option = input()
            if option == "1":
                name = input("Enter the name of the show: ")
                weekday = input("Enter the weekday of the show: ")
                show_id = input("Enter the ID of the show: ")
                idb.create_show(name, weekday, show_id)
            elif option == "2":
                show_id = input("Enter the ID of the show: ")
                show = idb.get_show(show_id)
                print(show)
            elif option == "3":
                print("Everything will be updated, if you don't want to update something, just input the previous value")
                show_id = input("Enter the ID to search for the show: ")
                new_show_id = input("Enter the new ID of the show: ")
                name = input("Enter the new name of the show: ")
                weekday = input("Enter the new weekday of the show: ")
                idb.update_show(show_id, new_show_id, name, weekday)
            elif option == "4":
                show_id = input("Enter the ID of the show: ")
                idb.delete_show(show_id)
            elif option == "5":
                break

if __name__ == "__main__":
    main()