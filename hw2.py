import mtm_elections


def send_city_details(file, mtm_elections_system):
        next_line = file.readline()
        if not next_line == "citizens\n":
                city_details = next_line.split(",")
                mtm_elections.mtmElectionsAddCity(mtm_elections_system,
                                                  str(city_details[0]),
                                                  int(city_details[1]))
        file.readline()


def send_citizens_details(file, mtm_elections_system):
        citizen = file.readline()
        while not citizen == "candidates\n":
                citizen_details = citizen.split(",")
                mtm_elections.mtmElectionsAddCitizen(mtm_elections_system,
                                                     str(citizen_details[0]),
                                                     int(citizen_details[1]),
                                                     int(citizen_details[2]),
                                                     int(citizen_details[3]),
                                                     int(citizen_details[4]))
                print(citizen_details[0])
                citizen = file.readline()


def send_candidates_details(file, mtm_elections_system):
        candidate = file.readline()
        while not candidate == "support\n":
                candidate_details = candidate.split(",")
                mtm_elections.mtmElectionsAddCandidate(mtm_elections_system,
                                                       int(candidate_details[0]),
                                                       int(candidate_details[1]))
                candidate = file.readline()
                print(candidate_details[0])


def send_support_details(file, mtm_elections_system):
        support = file.readline()
        while not support == "output\n":
                support_details = support.split(",")
                mtm_elections.mtmElectionsSupportCandidate(mtm_elections_system,
                                                           int(support_details[0]),
                                                           int(support_details[1]),
                                                           int(support_details[2]))

                support=file.readline()


def find_mayor(file, mtm_elections_system):
        output = file.readline()
        output_details = output.split(",")
        file_out_name = output_details[1].split("\n")
        print(file_out_name)
        result, mayor_id = mtm_elections.mtmElectionsMayorOfCity(mtm_elections_system,
                                                                 int(output_details[0]),
                                                                 str(file_out_name[0]))


mtm_elections_system = mtm_elections.mtmElectionsCreate()
file = open('input.txt', 'r')
new_line = file.readline()
send_city_details(file, mtm_elections_system)
send_citizens_details(file, mtm_elections_system)
send_candidates_details(file, mtm_elections_system)
send_support_details(file, mtm_elections_system)
find_mayor(file, mtm_elections_system)
mtm_elections.mtmElectionsDestroy(mtm_elections_system)
print("a")
file.close()
