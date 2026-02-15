import uuid
import pandas as pd
from database import engine

#Extrai os dados da planilha
companies = pd.read_excel(
    "Excel/fornecedores.xlsx", 
    sheet_name="Empresas", 
    skiprows=7
    )

#Cria as colunas ID e preferencial para os fornecedores
companies["supplier_id"] = [str(uuid.uuid4()) for _ in range(len(companies))]

#Define quais colunas vão para cada tabela
supplierColumns = ["supplier_id", "Empresa", "CNPJ", "Localização", "Representante", "Contato", "Email", "Site", "Descrição"]
supplierItemColums = ["supplier_id", "Produtos/Serviço", "Categoria"]
itemColumns = ["Produtos/Serviço", "Categoria"]

#Tabela suppliers
suppliers = companies[supplierColumns]
suppliers["preferred_supplier"] = False

def treatPhoneNumber(phoneNumber):
    phoneNumber = str(phoneNumber)
    match len(phoneNumber):
        case 14 | 15:
            phoneNumber = phoneNumber.replace("(", "").replace(")","")
        case 16 | 17:
            phoneNumber = phoneNumber.replace("+55 ", "")
        case _:
            phoneNumber
    
    return phoneNumber

suppliers["Contato"] = list(
    map(
        lambda x : treatPhoneNumber(x),
        suppliers["Contato"]
    )
)

suppliers["Representante"] = list(
    map(
        lambda x : None if x == "-" else x,
        suppliers["Representante"]
    )
)

#Tabela relacionamento suppliers_items
supplierItems = companies[supplierItemColums].dropna(subset="Produtos/Serviço")

supplierItems["Produtos/Serviço"] = list(
    map(
        lambda x : str(x).replace(",", ";").split(";"), 
        supplierItems["Produtos/Serviço"])
    )

supplierItems = supplierItems.explode("Produtos/Serviço").reset_index(drop=True)

supplierItems["Produtos/Serviço"] = list(
    map(
        lambda x : str(x).strip().capitalize(),
        supplierItems["Produtos/Serviço"]
    )
)

#Tabela items
items = supplierItems[itemColumns].drop_duplicates(subset="Produtos/Serviço")
items["item_id"] = [str(uuid.uuid4()) for _ in range(len(items))]


#Join que busca o ID do produto para a tabela relacionamento
supplierItems = supplierItems[["supplier_id", "Produtos/Serviço"]].merge(items, on="Produtos/Serviço")
supplierItems = supplierItems[["item_id", "supplier_id"]]

#Renomea as tabelas de acordo com o DB
suppliers = suppliers.rename(
    columns={
        'supplier_id': 'id', 
        'Empresa': 'name',
        'CNPJ' : 'cnpj', 
        'Localização' : 'location', 
        'Representante' : 'representative',
        'Contato' : 'phone_number', 
        'Email' : 'email', 
        'Site' : 'site', 
        'Descrição' : 'description'
        }
    )

items = items.rename(
    columns={
        'item_id' : 'id',
        'Produtos/Serviço' : 'name',
        'Categoria' : 'category'
        }
    )

#Usa a engine do SQLAlchemy para popular as tabelas no banco
suppliers.to_sql("suppliers", engine, if_exists="append", index=False)
items.to_sql("items", engine, if_exists="append", index=False)
supplierItems.to_sql("item_supplier", engine, if_exists="append", index=False)