import pandas as pd

serie = pd. Series([1, "hola", 3, False, ])

data = pd.read_csv("base.csv")
print(data.head(5))
frecuencia_sexo = data["Sexo"].value_counts()
frecuencia_sexo_norm = data["Sexo"].value_counts(normalize=True)
print(frecuencia_sexo)

distribucion = pd.DataFrame({"frecuencia": frecuencia_sexo,"Porcentaje (%)": frecuencia_sexo_norm})
sexo = {0: "Masculino", 1:"Femenino"}
distribucion.rename(index=sexo, inplace=True)
print(distribucion)

