from database import Database
from idolDatabase import IdolDatabase


def main():
    db = Database("bolt://52.91.18.4", "neo4j", "point-installations-views")
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

            ## IDOL
            if option == "1":
                print("Select an option:")
                print("6. Create")
                print("7. Insert")
                print("8. Read")
                print("9. Update")
                print("10. Delete")
                print("11. Exit")
                option = input()

                ## CREATE
                if option == "6":
                    name = input("Enter the name of the idol: ")
                    age = input("Enter the age of the idol: ")
                    country = input("Enter the country of the idol: ")
                    full_name = input("Enter the full name of the idol: ")
                    idol_id = input("Enter the ID of the idol: ")
                    idb.create_idol(name, age, country, full_name, idol_id)

                ## INSERT
                elif option == "7":
                    print("12. Into Group")
                    print("13. Into Show")
                    print("14. Exit")
                    option = input()
                    if option == "12":
                        idol_id = input("Enter the ID of the idol: ")
                        group_id = input("Enter the ID of the group: ")
                        idb.insert_idol_group(idol_id, group_id)
                    elif option == "13":
                        idol_id = input("Enter the ID of the idol: ")
                        show_id = input("Enter the ID of the show: ")
                        idb.insert_idol_show(idol_id, show_id)

                ## READ
                elif option == "8":
                    idol_id = input("Enter ID of the idol: ")
                    idol = idb.get_idol(idol_id)
                    print(idol)

                ## UPDATE
                elif option == "9":
                    print("Everything will be updated, if you don't want to update something, just input the previous value")
                    idol_id = input("Enter the ID to search for the idol: ")
                    new_idol_id = input("Enter the new ID of the idol: ")
                    name = input("Enter the new name of the idol: ")
                    age = input("Enter the new age of the idol: ")
                    country = input("Enter the new country of the idol: ")
                    full_name = input("Enter the new full name of the idol: ")
                    idb.update_idol(idol_id, new_idol_id, name, age, country, full_name)

                ## DELETE
                elif option == "10":
                    idol_id = input("Enter the ID of the idol: ")
                    idb.delete_idol(idol_id)

            ## GROUP
            elif option == "2":
                print("Select an option:")
                print("6. Create")
                print("7. Insert")
                print("8. Read")
                print("9. Update")
                print("10. Delete")
                print("11. Exit")
                option = input()

                ## CREATE
                if option == "6":
                    name = input("Enter the name of the group: ")
                    debut = input("Enter the debut of the group: ")
                    group_id = input("Enter the ID of the group: ")
                    idb.create_group(name, debut, group_id)

                ## INSERT
                elif option == "7":
                    print("12. Into Company")
                    print("13. Into Show")
                    print("14. Exit")
                    option = input()
                    if option == "12":
                        group_id = input("Enter the ID of the group: ")
                        company_id = input("Enter the ID of the company: ")
                        idb.insert_group_company(group_id, company_id)
                    elif option == "13":
                        group_id = input("Enter the ID of the group: ")
                        show_id = input("Enter the ID of the show: ")
                        idb.insert_group_show(group_id, show_id)

                ## READ
                elif option == "8":
                    group_id = input("Enter the ID of the group: ")
                    group = idb.get_group(group_id)
                    print(group)

                ## UPDATE
                elif option == "9":
                    print("Everything will be updated, if you don't want to update something, just input the previous value")
                    group_id = input("Enter the ID to search the group: ")
                    new_group_id = input("Enter the new group id of the group: ")
                    name = input("Enter the new name of the group: ")
                    debut = input("Enter the new debut of the group: ")
                    idb.update_group(group_id, new_group_id, name, debut)

                ## DELETE
                elif option == "10":
                    group_id = input("Enter the ID of the group: ")
                    idb.delete_group(group_id)

            ## COMPANY
            elif option == "3":
                print("Select an option:")
                print("6. Create")
                print("7. Read")
                print("8. Update")
                print("9. Delete")
                print("10. Exit")
                option = input()

                ## CREATE
                if option == "6":
                    name = input("Enter the name of the company: ")
                    company_id = input("Enter the ID of the company: ")
                    idb.create_company(name, company_id)

                ## READ
                elif option == "7":
                    company_id = input("Enter the ID of the company: ")
                    company = idb.get_company(company_id)
                    print(company)

                ## UPDATE
                elif option == "8":
                    print("Everything will be updated, if you don't want to update something, just input the previous value")
                    company_id = input("Enter the ID to search for the company: ")
                    new_company_id = input("Enter the new ID of the company: ")
                    name = input("Enter the enw name of the company: ")
                    idb.update_company(company_id, new_company_id, name)

                ## DELETE
                elif option == "9":
                    company_id = input("Enter the ID of the company: ")
                    idb.delete_company(company_id)

            ## SHOW
            elif option == "4":
                print("Select an option:")
                print("6. Create")
                print("7. Read")
                print("8. Update")
                print("9. Delete")
                print("10. Exit")

                option = input()
                if option == "6":
                    name = input("Enter the name of the show: ")
                    weekday = input("Enter the weekday of the show: ")
                    show_id = input("Enter the ID of the show: ")
                    idb.create_show(name, weekday, show_id)
                elif option == "7":
                    show_id = input("Enter the ID of the show: ")
                    show = idb.get_show(show_id)
                    print(show)
                elif option == "8":
                    print("Everything will be updated, if you don't want to update something, just input the previous value")
                    show_id = input("Enter the ID to search for the show: ")
                    new_show_id = input("Enter the new ID of the show: ")
                    name = input("Enter the new name of the show: ")
                    weekday = input("Enter the new weekday of the show: ")
                    idb.update_show(show_id, new_show_id, name, weekday)
                elif option == "9":
                    show_id = input("Enter the ID of the show: ")
                    idb.delete_show(show_id)


if __name__ == "__main__":
    main()