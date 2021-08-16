#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[5]:


#Upload do arquivo
from google.colab import files
arq = files.upload()


# In[ ]:


#Criando nosso DataFrame
df = pd.read_excel("AdventureWorks.xlsx")


# In[7]:


#Visualizando as 5 primeiras linhas
df.head()


# In[8]:


#Quantidade de linhas e colunas
df.shape


# In[9]:


#Verificando os tipos de dados
df.dtypes


# In[10]:


#Qual a Receita total?
df["Valor Venda"].sum()


# In[ ]:


#Qual o custo Total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna de custo


# In[12]:


df.head(1)


# In[13]:


#Qual o custo Total?
round(df["custo"].sum(), 2)


# In[ ]:


#Agora que temos a receita e custo e o total, podemos achar o Lucro total
#Vamos criar uma coluna de Lucro que será Receita - Custo
df["lucro"]  = df["Valor Venda"] - df["custo"] 


# In[15]:


df.head(1)


# In[16]:


#Total Lucro
round(df["lucro"].sum(),2)


# In[ ]:


#Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]


# In[18]:


df.head(1)


# **Agora, queremos saber a média do tempo de envio para cada Marca, e para isso precisamos transformar a coluna Tempo_envio em númerica**

# In[ ]:


#Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days


# In[20]:


df.head(1)


# In[21]:


#Verificando o tipo da coluna Tempo_envio
df["Tempo_envio"].dtype


# In[22]:


#Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()


#  **Missing Values**

# In[23]:


#Verificando se temos dados faltantes
df.isnull().sum()


# **E, se a gente quiser saber o Lucro por Ano e Por Marca?**

# In[26]:


#Vamos Agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()


# In[ ]:


pd.options.display.float_format = '{:20,.2f}'.format


# In[27]:


#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano


# In[28]:


#Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)


# In[29]:


#Gráfico Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");


# In[30]:


df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");


# In[31]:


df.groupby(df["Data Venda"].dt.year)["lucro"].sum()


# In[ ]:


#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]


# In[33]:


df_2009.head()


# In[34]:


df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");


# In[35]:


df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');


# In[36]:


df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');


# In[37]:


df["Tempo_envio"].describe()


# In[38]:


#Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"]);


# In[39]:


#Histograma
plt.hist(df["Tempo_envio"]);


# In[40]:


#Tempo mínimo de envio
df["Tempo_envio"].min()


# In[41]:


#Tempo máximo de envio
df['Tempo_envio'].max()


# In[42]:


#Identificando o Outlier
df[df["Tempo_envio"] == 20]


# In[ ]:


df.to_csv("df_vendas_novo.csv", index=False)


# In[ ]:




