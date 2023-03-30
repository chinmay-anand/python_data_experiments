import pandas as pd;

connection_string = 'mysql+mysqlconnector://test:test@localhost:3306/'+'testdb';
# connection_string = "sqlite:///database.db";

def user_match(profile_record_json, gender, location):
    '''
    accepts the profile record of a user and matches 
    '''
    return profile_record_json["gender"] == gender and profile_record_json["location"] == location

def find_matching_users(df_users, user_gender, user_location):
    return df[df.apply(lambda row: user_match(row['profile'], user_gender, user_location), axis=1)]

if __name__=="__main__":

    df = pd.read_sql_table('users', connection_string);

    print("\n---------- COMPLETE USER LIST ----------")
    print(df);

    print("\n---------- USER LIST for 'male', 'Hyderabad' ----------")
    print(find_matching_users(df, 'male', 'Hyderabad'))
