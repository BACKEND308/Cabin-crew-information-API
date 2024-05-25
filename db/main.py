from connect import connectDB,connect_mysql, fetch_data_from_mongodb, create_table_and_insert_data
import bson
import random

# Code for Crew API

def insert_cabin_crew(db, cabin_crew_data):
    """Inserts or updates a single cabin crew document in the MongoDB collection."""
    cabin_crew_collection = db.cabin_crew
    if cabin_crew_data["Role"].lower() == "chef":
        chef_data = prepare_chef_data(cabin_crew_data)
        return insert_chef(db, chef_data)
    else:
        result = cabin_crew_collection.update_one(
            {"CrewID": cabin_crew_data["CrewID"]},  # Query matches documents with the same CrewID
            {"$set": cabin_crew_data},  # Update the document with the data provided
            upsert=True  # Insert a new document if no matching document is found
        )
        if result.upserted_id is not None:
            return result.upserted_id
        else:
            return result.matched_count  # Return the number of documents matched, which should be 1 if updated

# Performing a validation check for crew members:
def validate_crew_composition(db, flight_number):
    """Validates the crew composition for a given flight."""
    roster_entry_collection = db.roster_entry
    crew_entries = list(roster_entry_collection.find({"FlightNumber": flight_number}))

    roles_count = {"chief": 0, "regular": 0, "chef": 0}

    for entry in crew_entries:
        crew_id = entry["CrewID"]
        cabin_crew = db.cabin_crew.find_one({"_id": crew_id})
        if cabin_crew:
            role = cabin_crew["Role"].lower()
            if role in roles_count:
                roles_count[role] += 1

    return roles_count


def prepare_chef_data(cabin_crew_data):
    """Prepares chef-specific data including validating dishes."""
    if len(cabin_crew_data["Dishes"]) < 2 or len(cabin_crew_data["Dishes"]) > 4:
        raise ValueError("Chef must have between 2 and 4 dishes.")
    featured_dish = random.choice(cabin_crew_data["Dishes"])
    cabin_crew_data["Featured_Dish"] = featured_dish
    return cabin_crew_data


def insert_chef(db, chef_data):
    """Inserts a single chef document into the MongoDB chefs collection."""
    chef_collection = db.chefs
    result = chef_collection.insert_one(chef_data)
    return result.inserted_id


def input_chef_data():
    """Collect data specific to chefs, including the dishes they are known for."""
    dishes = []
    while len(dishes) < 2 or len(dishes) > 4:
        num_dishes = int(input("Enter the number of dishes (2-4) the chef can prepare: "))
        dishes = [input(f"Enter dish name {i + 1}: ") for i in range(num_dishes)]

    # Select one dish to feature on the flight menu randomly
    featured_dish = random.choice(dishes)

    return {
        "Dishes": dishes,
        "Featured_Dish": featured_dish
    }


def input_document_data(prompts):
    """Collects user inputs based on given prompts and adds special handling for chefs."""
    data = {}
    for key, prompt in prompts.items():
        data[key] = input(prompt)  # Input values for each key based on the prompt.

    if data.get("Role", "").lower() == "chef":
        print("Entering chef-specific information...")
        data["Dishes"] = [input(f"Enter dish {i + 1} name: ") for i in
                          range(int(input("How many dishes does this chef prepare (2-4)? ")))]

    return data


def main():
    db = connectDB()

    sample_cabin_crew = [
        {
            "CrewID": 1,
            "MemberName": "Alice Johnson",
            "Age": 34,
            "Gender": "Female",
            "Nationality": "American",
            "Known_Languages": ["English", "Spanish"],
            "Aircraft_Restrictions": ["Boeing 747", "Airbus A320"],
            "Role": "chief",
            "Assigned_Seat": "1A"
        },
        {
            "CrewID": 2,
            "MemberName": "Bob Smith",
            "Age": 29,
            "Gender": "Male",
            "Nationality": "British",
            "Known_Languages": ["English", "French"],
            "Aircraft_Restrictions": ["Boeing 777"],
            "Role": "regular",
            "Assigned_Seat": "1B"
        },
        {
            "CrewID": 3,
            "MemberName": "Carlos Ruiz",
            "Age": 41,
            "Gender": "Male",
            "Nationality": "Spanish",
            "Known_Languages": ["Spanish", "English", "Portuguese"],
            "Aircraft_Restrictions": ["Airbus A330"],
            "Role": "chef",
            "Assigned_Seat": "2A",
            "Dishes": ["Paella", "Tortilla Española"],
            "Featured_Dish": "Paella"
        },
        {
            "CrewID": 4,
            "MemberName": "Amina Khan",
            "Age": 25,
            "Gender": "Female",
            "Nationality": "Pakistani",
            "Known_Languages": ["Urdu", "English"],
            "Aircraft_Restrictions": ["Boeing 737"],
            "Role": "chef",
            "Assigned_Seat": "2B",
            "Dishes": ["Biryani", "Chicken Karahi"],
            "Featured_Dish": "Biryani"
        },
        {
            "CrewID": 5,
            "MemberName": "Lucas Bertoni",
            "Age": 38,
            "Gender": "Male",
            "Nationality": "Italian",
            "Known_Languages": ["Italian", "English"],
            "Aircraft_Restrictions": ["Airbus A380"],
            "Role": "chief",
            "Assigned_Seat": "3A"
        },
        {
            "CrewID": 6,
            "MemberName": "Sophie Dubois",
            "Age": 31,
            "Gender": "Female",
            "Nationality": "French",
            "Known_Languages": ["French", "English"],
            "Aircraft_Restrictions": ["Boeing 787"],
            "Role": "regular",
            "Assigned_Seat": "3B"
        },
        {
            "CrewID": 7,
            "MemberName": "Liu Wei",
            "Age": 45,
            "Gender": "Male",
            "Nationality": "Chinese",
            "Known_Languages": ["Mandarin", "English"],
            "Aircraft_Restrictions": ["Airbus A350"],
            "Role": "regular",
            "Assigned_Seat": "4A"
        },
        {
            "CrewID": 8,
            "MemberName": "Fatima Al-Fassi",
            "Age": 27,
            "Gender": "Female",
            "Nationality": "Moroccan",
            "Known_Languages": ["Arabic", "French", "English"],
            "Aircraft_Restrictions": ["Boeing 747"],
            "Role": "chef",
            "Assigned_Seat": "4B",
            "Dishes": ["Couscous", "Tagine"],
            "Featured_Dish": "Couscous"
        },
        {
            "CrewID": 9,
            "MemberName": "Oliver Smith",
            "Age": 30,
            "Gender": "Male",
            "Nationality": "Australian",
            "Known_Languages": ["English"],
            "Aircraft_Restrictions": ["Boeing 737", "Airbus A320"],
            "Role": "chief",
            "Assigned_Seat": "5A"
        },
        {
            "CrewID": 10,
            "MemberName": "Maria Fernández",
            "Age": 22,
            "Gender": "Female",
            "Nationality": "Mexican",
            "Known_Languages": ["Spanish", "English"],
            "Aircraft_Restrictions": ["Airbus A380"],
            "Role": "chef",
            "Assigned_Seat": "5B",
            "Dishes": ["Tacos", "Enchiladas", "Guacamole"],
            "Featured_Dish": "Tacos"
        }
    ]

    for data in sample_cabin_crew:
        insert_cabin_crew(db, data)
        print(f"Inserted {data['MemberName']} with Role: {data['Role']}")

    cabin_crew_prompts = {
        "CrewID": "Enter Crew ID: ",
        "MemberName": "Enter Cabin Crew Member Name: ",
        "Age": "Enter Age: ",
        "Gender": "Enter Gender: ",
        "Nationality": "Enter Nationality: ",
        "Known_Languages": "Enter Known Languages: ",
        "Aircraft_Restrictions": "Enter Aircraft Restrictions (comma-separated):",
        "Role": "Enter Cabin Crew Role (chief, regular, chef): ",
        "Assigned_Seat": "Enter Assigned Seat (if applicable): "
    }

    cabin_crew_data = input_document_data(cabin_crew_prompts) # This is for getting the data through the prompts
    cabin_crew_id = insert_cabin_crew(db, cabin_crew_data) # This is for inserting into collection on MongoDB

# The code below is for converting a NoSQL collection into my MySQL collection
#     engine, session = connect_mysql()
#
#     # Example: Transfer 'cabin_crew' from MongoDB to a new MySQL table 'cabin_crew_sql'
#     collection_name = 'cabin_crew'  # Adjust the collection name as needed
#     data = fetch_data_from_mongodb(db, collection_name)
#     if data:
#         print(f"Fetched {len(data)} documents from MongoDB collection '{collection_name}'")
#         create_table_and_insert_data(engine, data, 'passengers_sql')  # Adjust the SQL table name as needed
#     else:
#         print(f"No data found in MongoDB collection '{collection_name}'")
#
if __name__ == '__main__':
    main()
