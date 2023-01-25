# Dictionaries

# Declaraciones
print("**************** Declarando dict **************")
my_dict = dict()
my_other_dict =  {}
print(f"tipo de my_dict: {type(my_dict)}")

persona = {
  "name": "Gabriel",
  "surname": "Cervantes",
  "age": 32,
  "is_marred" : False,
  "skills" : ["Js","Css","Html"],
  "social":{
    "twitter": "@gabrielcehu",
    "instagram" : "gabo_cervantes"
  }
}
print(f"persona: {persona}")


# Accediendo a los datos
print("**************** Declarando dict **************")
print(f"accediendo a name: {persona['name']}")
print(f"accediendo a skills Css: {persona['skills'][1]}")
# print(f"accediendo a height: {persona[height]}") NameError: name 'height' is not defined

print(f"usando get para name: {persona.get('name')}")
print(f"usando get para skills: {persona.get('skills')}")
print(f"usando get para height: {persona.get('hight')}")


# Verificando valores
print("**************** Verificando valores en dict **************")
print(f"persona original: {persona}")
print(f"age in persona: {'age' in persona}")
print(f"height in persona: {'height' in persona}")


# Agregando valores
print("**************** Agregando al dict **************")
print(f"persona original: {persona}")
persona["height"] = 1.72
print(f"agregando height:{persona['height']}")
persona["skills"].append('React')
print(f"agrandando otra skill: {persona['skills']}")


# Modificando valores
print("**************** Modificando valores en dict **************")
print(f"persona original: {persona}")
persona["age"] = 25
print(f"age modificada: {persona['age']}")
persona["skills"][3] = 'Next js'
print(f"skills modificadas: {persona['skills']}")


# Eliminando valore
print("**************** Eliminando valores en dict **************")
print(f"persona original: {persona}")
print(f"is_marred in persona: {'is_marred' in persona}")
persona.pop('is_marred')
print(f"eliminando is_marred: {'is_marred' in persona}")


# Obtener claves y valores
print("**************** Obtener claves y valores en dict **************")
print(f"persona.keys(): {persona.keys()}")
print(f"persona.values(): {persona.values()}")
print(f"persona.items(): {persona.items()}")


# Diccionarios vacios
print("**************** Dict vacios **************")

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))

my_new_dict = dict.fromkeys(persona)
print(my_new_dict)

my_new_dict = dict.fromkeys(persona, 'Gabriel')
print(my_new_dict)

