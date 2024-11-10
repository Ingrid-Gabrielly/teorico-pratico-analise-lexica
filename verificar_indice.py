import re #Importa o módulo de expressões regulares para trabalhar com padrões de texto

def is_valid_index(input_string):
    """
    Verifica se a string de entrada corresponde a um índice válido no formato x[indices].
    
    """

    #Verifica se a expressão está no formato x[indices] usando uma expressão regular
    match = re.match(r'^x\[(.*)\]$', input_string)
    if not match:
        return False #Retorna False se o formato básico não corresponder
    
    indices = match.group(1) #Extrai a parte dentro dos colchetes

    #Definição dos padrões de expressões regulares para diferentes tipos de índices

    integer_pattern = r'^(-[1-9]\d*|0|[1-9]\d*)$'  #Padrão para índices inteiros

    numeric_interval_pattern = r'^(?:\d+:\d+)|(?:-[1-9]\d*:-[1-9]\d*)$' #Padrão para intervalos numéricos

    names_in_quotes_pattern = r'^(?:"[^"]+"|\'[^\']+\')$' #Padrão para nomes dentro de aspas simples ou duplas

    interval_names_in_quotes_pattern = r'^(?:"[^"]+"|\'[^\']+\'):(?:"[^"]+"|\'[^\']+\')$' #Padrão para intervalos de nomes dentro de aspas

    #Lista de todos os padrões a serem verificados
    patterns = [
        integer_pattern,
        numeric_interval_pattern,
        names_in_quotes_pattern,
        interval_names_in_quotes_pattern
    ]

    #Itera sobre cada padrão e verifica se o índice corresponde a algum deles
    for pattern in patterns:
        if re.match(pattern, indices):
            return True #Retorna True se corresponder a pelo menos um padrão
        
    return False #Retorna False se não corresponder a nenhum padrão

def main():
    """
    A função principal que testa vários exemplos de índices para verificar sua validade.
    
    """

    #Lista de exemplos de índices para testar
    exemplos = [
        "x[0]",              
        "x[-0]", 
        "x[10]",             
        "x[-5]",             
        "x[1:5]",            
        "x[-10:-1]",  
        "x[-0:-0]",       
        "x[-10:1]",
        'x["Date"]',         
        "x['New Column']",   
        'x["Data":"State"]', 
        "x['Tested':'Data']",    
        "x[""Tested':'Data']",     
        "x[1:]",            
        "x[:5]",             
        "x[1:5:2]",          
        "x[nome]",           
        "x['nome",           
        "x[\"nome']",        
        "y[1]",              
        "x[1,2]",            
        "x[]",                    
    ]

    # Itera sobre cada exemplo, verifica sua validade e imprime o resultado
    for exemplo in exemplos:
        if is_valid_index(exemplo):
            resultado = "Válido"
        else:
            resultado = "Inválido"
        print(f"{exemplo}: {resultado}")

if __name__ == "__main__":
    main()
