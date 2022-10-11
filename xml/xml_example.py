import xml.etree.ElementTree as ET

class Person:
    def __init__(self, name, last_name, birthday_year, phone_code, phone_number):
        self.name = name
        self.last_name = last_name
        self.birthday_year = birthday_year
        self.phone_code = phone_code
        self.phone_number = phone_number
    def dump_to_xml(self):
        person = ET.Element("person")#создаем тег (или ветку) <person>
        name = ET.SubElement(person, "name")#создаем тег (или ветку) <name>, которая лежит в <person>
        name.text = self.name
        last_name = ET.SubElement(person, "last_name")#создаем тег (или ветку) <last_name>, которая лежит в <person>
        last_name.text = self.last_name
        birthday_year = ET.SubElement(person, "birthday_year")  # создаем тег (или ветку) <birthday_year>, которая лежит в <person>
        birthday_year.text = str(self.birthday_year)
        phone = ET.SubElement(person, "phone")
        phone_code = ET.SubElement(phone, "phone_code")
        phone_code.text = str(self.phone_code)
        phone_number = ET.SubElement(phone, "phone_number")
        phone_number.text = str(self.phone_number)
        return person

def save_department(file_name):
    person_Ivan = Person("Ivan", "Ivanov", 1980, 933, 5550000)
    person_Petr = Person("Petr", "Petrov", 1988, 977, 1112222)
    person_Ivan_xml = person_Ivan.dump_to_xml()
    person_Petr_xml = person_Petr.dump_to_xml()
    department = ET.Element("department")
    department.append(person_Ivan_xml)
    department.append(person_Petr_xml)
    department_xml_str = ET.tostring(department, encoding="unicode")
    with open(file_name, "w") as file:
        print(type(department_xml_str))
        file.write(department_xml_str)
# ctrl + alt +l


def main():
    department_file_name = "department.xml"
    save_department(department_file_name)

if __name__ == '__main__':
   main()
