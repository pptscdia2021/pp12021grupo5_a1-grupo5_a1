import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class accion:
    def obtenerCotizacionesMayorGanancia(dataframe, cantidad):
        dataframe["% Dif."]=dataframe["% Dif."].str.replace(',', '.').astype(float)
        dfordenado=dataframe.sort_values(by="% Dif.", ascending=False)
        
        return dfordenado.head(cantidad)[["Nombre","% Dif."]]

    def obtenerCotizacionesMayorPerdida(dataframe,cantidad):
        dataframe["% Dif."]=dataframe["% Dif."].str.replace(',', '.').astype(float)
        dfordenado=dataframe.sort_values(by="% Dif.", ascending=False)
        return dfordenado.tail(cantidad)[["Nombre","% Dif."]]
    
    
    def obtenerCotizacionesYahoo(acciones, accionesbolsamadrid):
        lista=list()
        for indice in range(0, len(acciones)):
            df=yf.download(acciones[indice],group_by='ticker', period="1d")
            df['Nombre']=accionesbolsamadrid[indice]
            lista.append(df)
        
        dff=pd.concat(lista)
        dff.to_csv('yahoocomp.csv')
    
    def tablaComparacion(bolsaMadrid, bolsaYahoo):
        bolsaMadrid=bolsaMadrid.loc[:,['Nombre','Valor']].sort_values(by='Nombre').reset_index(drop=True)
        bolsaYahoo=bolsaYahoo.loc[:,['Nombre','Close']].sort_values(by='Nombre').reset_index(drop=True)
        df=pd.concat([bolsaMadrid,bolsaYahoo['Close']],axis=1)

        df=df.rename(columns={'Valor':'Bolsa Madrid','Close':'Yahoo Finance'})
        return df
    
    def graficar(datafram,ejeX,tituloGrafico,nombreArchivo):
        plt.style.use('seaborn')
        datafram.set_index(ejeX).plot.bar(rot=0, title=tituloGrafico, figsize=(5,5), fontsize=12)
        plt.savefig(nombreArchivo, bbox_inches='tight')
        plt.tight_layout();plt.show()