import degree


def main():

    print("------------------------")
    print("| codedrome.com        |")
    print("| Eratosthenes and the |")
    print("| Size of Planet Earth |")
    print("------------------------\n")


    print("Eratosthenes Values\n-------------------\n")

    separation_ancient = degree.Degree(degrees = 7, minutes = 12, seconds = 0)

    separation_ancient_decimal = separation_ancient.to_decimal()

    distance_stades = 5000

    stades_per_degree = distance_stades / separation_ancient_decimal

    circumference_stades = stades_per_degree * 360

    stades_to_km_Greek = circumference_stades * 0.185

    stades_to_km_Egyptian = circumference_stades * 0.1575

    print(f"Separation                      {separation_ancient}\n")
    print(f"Separation decimal              {separation_ancient_decimal}\n")
    print(f"Distance in stades              {distance_stades}\n")
    print(f"Stades per degree               {stades_per_degree:.2f}\n")
    print(f"Circumference in stades         {circumference_stades}\n")
    print(f"Stades to kilometres (Greek)    {stades_to_km_Greek}\n")
    print(f"Stades to kilometres (Egyptian) {stades_to_km_Egyptian}\n")


    print("\nModern Values\n-------------\n")

    # Latitude of current Bibliotheca Alexandrina
    latitude_Alexandria = degree.Degree(degrees = 31, minutes = 12, seconds = 32)

    # Latitude of current Aswan
    latitude_Syene = degree.Degree(degrees = 24, minutes = 5, seconds = 20)

    separation = degree.Degree()
    separation.set_between(latitude_Alexandria, latitude_Syene)

    fraction_of_circle = separation.fraction_of_circle()

    distance_km = 791.7

    circumference_km = distance_km / fraction_of_circle

    print(f"Latitude of Alexandria         {latitude_Alexandria}\n")
    print(f"Latitude of Syene              {latitude_Syene}\n")
    print(f"Separation                     {separation}\n")
    print(f"Fraction of Circle             {fraction_of_circle:.4f}\n")
    print(f"Distance in km                 {distance_km} kilometres\n")
    print(f"Circumference                  {circumference_km:.2f} kilometres\n")


if __name__ == "__main__":

    main()
