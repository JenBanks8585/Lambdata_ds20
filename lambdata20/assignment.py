from pandas import DataFrame

def add_state_names_column(my_df):
    """
    Add a column of corresponding state names to a dataframe.
    Params (my_df) a DataFrame with a column called "abbrev" that has state abbrevations
    Returns a copy of the original dataframe, but with an extra column
    """
    new_df = my_df.copy()

    names_map = {"FL": "Florida", "GA": "Georgia", "CO": "Colorado"}

    new_df['name'] = new_df['Abbrev'].map(names_map)
    
    #breakpoint()
    return new_df


if __name__ == "__main__":
    df= DataFrame({'Abbrev':['FL', 'GA', 'CO']})
    print(df.head())
    
    mapped_df = add_state_names_column(df)
    print(mapped_df.head())
