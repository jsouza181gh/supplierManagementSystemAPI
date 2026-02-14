import pandas as pd
import uuid

#Extrai os dados da planilha
companies = pd.read_excel(
    "fornecedores.xlsx", 
    sheet_name="Empresas", 
    skiprows=7
    )

#Cria uma coluna de ID para os fornecedores
companies["supplier_id"] = [str(uuid.uuid4()) for _ in range(len(companies))]

#Define quais colunas vão para cada tabela
supplierColumns = ["supplier_id", "Empresa", "CNPJ", "Localização", "Representante", "Contato", "Email", "Site", "Descrição"]
supplierItemColums = ["supplier_id", "Produtos/Serviço", "Categoria"]
itemColumns = ["Produtos/Serviço", "Categoria"]

#Tabela suppliers
suppliers = companies[supplierColumns]

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
items["product_id"] = [str(uuid.uuid4()) for _ in range(len(items))]

#Join que busca o ID do produto para a tabela relacionamento
supplierItems = supplierItems[["supplier_id", "Produtos/Serviço"]].merge(items, on="Produtos/Serviço")
supplierItems = supplierItems[["supplier_id", "product_id"]]