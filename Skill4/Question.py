from pymongo import MongoClient


def main():
    while (True):
        choice = int(input('Enter your Choice'))
        if choice == 1:
            try:
                Name = input('Enter Name of the Student : ')
                roll_number = int(input('Enter Roll Number of The Student : '))
                branch = input('Enter branch of the Student : ')
                db.Skill.insert_one(
                    {
                        "_id": roll_number,
                        "name": Name,
                        "Branch": branch
                    }
                )
            except Exception as e:
                print(e)
        elif choice == 2:
            try:
                Roll_num = int(input('Enter Roll Number to delete : '))
                db.Skill.delete_one({"_id": Roll_num})
                print('Deletion Successfully......!')
            except Exception as e:
                print(e)
        elif choice == 3:
            try:
                pfsd = db.Skill.find()
                for val in pfsd:
                    print(val)
            except Exception as e:
                print(e)
        elif choice == 4:
            try:
                Num = input('Enter Roll Number to update : ')
                Name = input('Enter the name to update : ')
                db.Skill.update_one({
                    "_id": Num
                },
                    {
                        "$set": {
                            "name": Name
                        }
                    })
            except Exception as e:
                print(e)
        else:
            print("Improper selection")
            exit()

client = MongoClient('localhost:27017')
db = client.pfsd
main()