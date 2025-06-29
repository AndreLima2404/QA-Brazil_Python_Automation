import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Cria o driver do Chrome
driver = webdriver.Chrome()

# Substitua o link abaixo pelo SEU link gerado do servidor Urban Routes
driver.get("https://cnt-3ce7f643-02c0-4619-96cc-eb76a5735e8c.containerhub.tripleten-services.com?lng=pt")

# Espera 2 segundos para garantir que a página carregue completamente
time.sleep(2)

# Encontra o elemento único do logotipo usando seletor CSS
logo_element = driver.find_element(By.CSS_SELECTOR, "img.logo-image")
print("Elemento do logotipo encontrado:", logo_element)

# Encontra todos os elementos com a classe .mode (botões de modo de transporte)
mode_elements = driver.find_elements(By.CSS_SELECTOR, ".mode")
print("Quantidade de modos encontrados:", len(mode_elements))

# Mostra os textos de cada modo
for mode in mode_elements:
    print("Modo:", mode.text)

# Tarefa 1
# Encontra o elemento com a etiqueta "Platform" usando a classe .logo-disclaimer
platform_label = driver.find_element(By.CSS_SELECTOR, ".logo-disclaimer")

# Imprime o texto encontrado
print("Tarefa 1 OK - Texto da etiqueta encontrada:", platform_label.text)

# Tarefa 2
# Encontra todos os elementos com class="dst-picker-marker" usando XPath relativo
markers = driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']")

# Verifica se mais de um elemento foi encontrado
assert len(markers) > 1, "Erro: Menos de dois elementos com a classe 'dst-picker-marker' foram encontrados."

# Imprime a quantidade encontrada
print("Tarefa 2 OK - Total de marcadores encontrados:", len(markers))

# Tarefa 3
# Encontra os campos de entrada pelos seus IDs
from_input = driver.find_element(By.ID, "from")
to_input = driver.find_element(By.ID, "to")

# Recupera os valores dos placeholders
from_placeholder = from_input.get_attribute("placeholder")
to_placeholder = to_input.get_attribute("placeholder")

# Verifica se os valores estão corretos
assert from_placeholder == "East 2nd Street, 601", f"Placeholder incorreto em 'De': {from_placeholder}"
assert to_placeholder == "1300 1st St", f"Placeholder incorreto em 'Para': {to_placeholder}"

print("Placeholders verificados com sucesso!")


# Encerra o WebDriver e fecha o navegador
driver.quit()
