from typing import Tuple

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    street_prefixes = (
        "Strada",
        "Aleea",
        "Intrarea",
        "Bulevardul",
        "Soseaua",
        "Drumul",
    )
    street_name_formats = (
        "{{street_prefix}} {{last_name}}",
        "{{street_prefix}} {{first_name}} {{last_name}}",
        "{{street_prefix}} {{last_name}}",
    )
    street_address_formats = (
        "{{street_name}}",
        "{{street_name}} {{building_number}}",
        "{{street_name}} {{building_number}} {{secondary_address}}",
    )
    address_formats = ("{{street_address}}\n{{city}}, {{postcode}}",)
    building_number_formats = ("Nr. %#", "Nr. %##")
    secondary_address_formats = ("Bl. %#  Sc. %# Ap. %##",)
    postcode_formats = (
        "1#####",
        "2#####",
        "3#####",
        "4#####",
        "5#####",
        "6#####",
        "7#####",
        "8#####",
        "9#####",
    )
    city_formats = ("{{city_name}}",)
    cities = (
        "Cluj-Napoca",
        "Timisoara",
        "Iasi",
        "Constanta",
        "Craiova",
        "Brasov",
        "Galati",
        "Ploiesti",
        "Oradea",
        "Braila",
        "Arad",
        "Pitesti",
        "Sibiu",
        "Bacau",
        "Targu Mures",
        "Baia Mare",
        "Buzau",
        "Botosani",
        "Satu Mare",
        "Suceava",
        "Ramnicu Valcea",
        "Drobeta-Turnu Severin",
        "Piatra-Neamt",
        "Targoviste",
        "Targu Jiu",
        "Focsani",
        "Tulcea",
        "Resita",
        "Slatina",
        "Bistrita",
        "Calarasi",
        "Giurgiu",
        "Deva",
        "Hunedoara",
        "Zalau",
        "Barlad",
        "Alba Iulia",
        "Sfantu Gheorghe",
        "Roman",
        "Vaslui",
        "Turda",
        "Medias",
        "Alexandria",
        "Voluntari",
        "Pipera (Voluntari)",
        "Slobozia",
        "Lugoj",
        "Medgidia",
        "Onesti",
        "Miercurea-Ciuc",
        "Petrosani",
        "Tecuci",
        "Mangalia",
        "Odorheiu Secuiesc",
        "Ramnicu Sarat",
        "Sighetu Marmatiei",
        "Campina",
        "Navodari",
        "Campulung",
        "Caracal",
        "Sacele",
        "Fagaras",
        "Dej",
        "Rosiori de Vede",
        "Mioveni",
        "Curtea de Arges",
        "Husi",
        "Reghin",
        "Sighisoara",
        "Pantelimon",
        "Pascani",
        "Oltenita",
        "Turnu Magurele",
        "Caransebes",
        "Falticeni",
        "Radauti",
        "Lupeni",
        "Dorohoi",
        "Vulcan",
        "Campia Turzii",
        "Zarnesti",
        "Borsa",
        "Popesti-Leordeni",
        "Codlea",
        "Carei",
        "Moinesti",
        "Petrila",
        "Sebes",
        "Tarnaveni",
        "Floresti",
        "Gherla",
        "Fetesti-Gara",
        "Buftea",
        "Cugir",
        "Moreni",
        "Gheorgheni",
        "Comanesti",
        "Salonta",
        "Cernavoda",
        "Targu Secuiesc",
        "Bailesti",
        "Campulung Moldovenesc",
        "Aiud",
        "Dragasani",
        "Valea Caselor (Dragasani)",
        "Bals",
        "Bocsa",
        "Motru",
        "Corabia",
        "Bragadiru",
        "Urziceni",
        "Rasnov",
        "Rasnov Romacril",
        "Buhusi",
        "Zimnicea",
        "Marghita",
        "Mizil",
        "Cisnadie",
        "Targu Neamt",
        "Calafat",
        "Vatra Dornei",
        "Adjud",
        "Gaesti",
        "Tandarei",
        "Gura Humorului",
        "Chitila",
        "Viseu de Sus",
        "Otopeni",
        "Ludus",
        "Brad",
        "Dragu-Brad",
        "Valu lui Traian",
        "Cumpana",
        "Sannicolau Mare",
        "Valenii de Munte",
        "Jilava",
        "Dabuleni",
        "Filiasi",
        "Blaj",
        "Ovidiu",
        "Simleu Silvaniei",
        "Matca",
        "Pecica",
        "Rovinari",
        "Videle",
        "Baicoi",
        "Pucioasa",
        "Jimbolia",
        "Baia Sprie",
        "Targu Frumos",
        "Vicovu de Sus",
        "Orsova",
        "Sinaia",
        "Negresti-Oas",
        "Beius",
        "Santana",
        "Pechea",
        "Simeria",
        "Boldesti-Scaeni",
        "Poienile de sub Munte",
        "Valea lui Mihai",
        "Covasna",
        "Targu Ocna",
        "Toplita",
        "Sovata",
        "Otelu Rosu",
        "Oravita",
        "Moisei",
        "Harsova",
        "Murfatlar",
        "Beclean",
        "Poiana Mare",
        "Huedin",
        "Babadag",
        "Marasesti",
        "Topoloveni",
        "Sangeorgiu de Mures",
        "Jibou",
        "Sabaoani",
        "Hateg",
        "Avrig",
        "Darmanesti",
        "Marginea",
        "Moldova Veche",
        "Ineu",
        "Bolintin-Vale",
        "Mihail Kogalniceanu",
        "Macin",
        "Tomesti",
        "Nasaud",
        "Uricani",
        "Rosu",
        "Calan",
        "Borcea",
        "Afumati",
        "Domnesti",
        "Draganesti-Olt",
        "Cristuru Secuiesc",
        "1 Decembrie",
        "Lumina",
        "Fetesti",
        "Mogosoaia",
        "Modelu",
        "Dumbravita",
        "Seini",
        "Alesd",
        "Sangeorz-Bai",
        "Curtici",
        "Darabani",
        "Nadlac",
        "Victoria",
        "Amara",
        "Branesti",
        "Harlau",
        "Lipova",
        "Techirghiol",
        "Agnita",
        "Sacueni",
        "Titu",
        "Siret",
        "Segarcea",
        "Odobesti",
        "Podu Iloaiei",
        "Ocna Mures",
        "Urlati",
        "Strehaia",
        "Tasnad",
        "Cajvana",
        "Tuzla",
        "Sadova",
        "Vlahita",
        "Stei",
        "Diosig",
        "Cobadin",
        "Gilau",
        "Vladimirescu",
        "Dancu",
        "Bumbesti-Jiu",
        "Busteni",
        "Peretu",
        "Cudalbi",
        "Bosanci",
        "Balotesti",
        "Lunca Cetatuii",
        "Dragalina",
        "Fieni",
        "Chisineu-Cris",
        "Balan",
        "Sandominic",
        "Strejnicu",
        "Baciu",
        "Fundulea",
        "Remetea",
        "Fagetel (Remetea)",
        "Ianca",
        "Roseti",
        "Breaza de Sus",
        "Cornetu",
        "Insuratei",
        "Apahida",
        "Berceni",
        "Vicovu de Jos",
        "Savinesti (Poiana Teiului)",
        "Savinesti",
        "Teius",
        "Barbulesti",
        "Plosca",
        "Toflea",
        "Magurele",
        "Feldru",
        "Anina",
        "Negresti",
        "Valea Mare (Negresti)",
        "Peris",
        "Fundeni",
        "Giroc",
        "Baile Borsa",
        "Oituz",
        "Rucar",
        "Curcani",
        "Babeni",
        "Valea Mare (Babeni)",
        "Rodna",
        "Deta",
        "Ruscova",
        "Intorsura Buzaului",
        "Pancota",
        "Glina",
        "Talmaciu",
        "Copsa Mica",
        "Motatei",
        "Gugesti",
        "Schela Cladovei",
        "Sancraiu de Mures",
        "Iernut",
        "Targu Lapus",
        "Maieru",
        "Prejmer",
        "Pogoanele",
        "Dobroesti",
        "Baraolt",
        "Arbore",
        "Homocea",
        "Corund",
        "Tufesti",
        "Giarmata",
        "Baia",
        "Dumbraveni",
        "Eforie Nord",
        "Horodnic de Sus",
        "Greci",
        "Tudora",
        "Straja",
        "Rasinari",
        "Sebis",
        "Raducaneni",
        "Siria",
        "Paunesti",
        "Saveni",
        "Tunari",
    )

    states: Tuple[Tuple[str, str], ...] = (
        ("AB", "Alba"),
        ("AG", "Argeș"),
        ("AR", "Arad"),
        ("B", "București"),
        ("BC", "Bacău"),
        ("BH", "Bihor"),
        ("BN", "Bistrița-Năsăud"),
        ("BR", "Brăila"),
        ("BT", "Botoșani"),
        ("BV", "Brașov"),
        ("BZ", "Buzău"),
        ("CJ", "Cluj"),
        ("CL", "Călărași"),
        ("CS", "Caraș Severin"),
        ("CT", "Constanța"),
        ("CV", "Covasna"),
        ("DB", "Dâmbovița"),
        ("DJ", "Dolj"),
        ("GJ", "Gorj"),
        ("GL", "Galați"),
        ("GR", "Giurgiu"),
        ("HD", "Hunedoara"),
        ("HR", "Harghita"),
        ("IF", "Ilfov"),
        ("IL", "Ialomița"),
        ("IS", "Iași"),
        ("MH", "Mehedinți"),
        ("MM", "Maramureș"),
        ("MS", "Mureș"),
        ("NT", "Neamț"),
        ("OT", "Olt"),
        ("PH", "Prahova"),
        ("SB", "Sibiu"),
        ("SJ", "Sălaj"),
        ("SM", "Satu Mare"),
        ("SV", "Suceava"),
        ("TL", "Tulcea"),
        ("TM", "Timiș"),
        ("TR", "Teleorman"),
        ("VL", "Vâlcea"),
        ("VN", "Vrancea"),
        ("VS", "Vaslui"),
    )

    def street_prefix(self) -> str:
        """
        :example 'Strada'
        """
        return self.random_element(self.street_prefixes)

    def secondary_address(self) -> str:
        """
        :example 'Bl. 123 Sc. 2 Ap. 15'
        """
        return self.numerify(self.random_element(self.secondary_address_formats))

    def city_name(self) -> str:
        return self.random_element(self.cities)

    def city_with_postcode(self) -> str:
        return self.postcode() + " " + self.random_element(self.cities)

    def administrative_unit(self) -> str:
        """
        example: u'Timiș'
        """
        return self.random_element(self.states)[1]  # type: ignore

    state = administrative_unit

    def state_abbr(self) -> str:
        """
        example: u'TM'
        """
        return self.random_element(self.states)[0]  # type: ignore
