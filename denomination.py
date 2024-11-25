print("==================================================")

user = input("USERNAME : ")
amount = eval(input("AMOUNT   : "))

print("\n==================================================")
print(input("\nPress any key to proceed on PH denomination... "))
print("==================================================")
print(f"Hi, {user} your deposit exchange in PH denomation are as follow :")

isang_libo = amount // 1000;                        sukli_libo = amount % 1000     
limang_daan = sukli_libo // 500;                    sukli_limang_daan = sukli_libo % 500
dalawang_daan = sukli_limang_daan // 200;           sukli_dalawang_daan = sukli_limang_daan % 200
isang_daan = sukli_dalawang_daan // 100;            sukli_isang_daan = sukli_limang_daan % 100
pipti = sukli_isang_daan // 50;                     sukli_pipti = sukli_isang_daan % 50
bente = sukli_pipti // 20;                          sukli_bente = sukli_pipti % 20
sampo = sukli_bente // 10;                          sukli_sampo = sukli_bente % 10
lima = sukli_sampo // 5;                            sukli_lima = sukli_sampo % 5
piso = sukli_lima // 1;                             sukli_piso = sukli_lima % 1

print(isang_libo, "- 1000php")
print(limang_daan, "- 500php")
print(dalawang_daan, "- 200php")
print(isang_daan, "- 100php")
print(pipti, "- 50php")
print(bente, "- 20php")
print(sampo, "- 10php")
print(lima, "- 5php")
print(piso, "- 1php")
