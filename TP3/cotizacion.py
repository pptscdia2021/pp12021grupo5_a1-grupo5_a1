import yfinance as yf

class cotizacion:
    def obtenerCotizacion(moneda):
        dol=yf.Ticker(moneda)
        return dol.info['ask']