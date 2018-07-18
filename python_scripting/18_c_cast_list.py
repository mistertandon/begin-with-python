def create_cast_list(filename):
    cast_list = []
    with open(filename, 'r') as file_data:
        for line in file_data:
            cast_list.append(line.strip().split(",")[0].title())

    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    return cast_list

cast_list = create_cast_list('./18_d_flying_circus_cast.txt')
for actor in cast_list:
    print(actor)