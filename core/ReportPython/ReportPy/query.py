
connection_string = (
    "Driver={SQL Server};"
    "Server=10.108.0.0;"
    "Database=DataBase;"
    "UID=Lectura;"
    "PWD=Credential123;"
    )

#--------------------------------------------------------------------------#
#--------------------------------------------------------------------------#

query_generic =         "SELECT distinct "\
                        "Documento.IdDeposito, "\
                        "Venta.IdCaja, "\
                        "Documento.NumeroDoc, "\
                        "FORMAT(Documento.Fecha, 'yyyy-MM-dd') AS FechaDoc, "\
                        "CAST(Venta.Total AS FLOAT) AS Total, "\
                        "CAST(VentaLinea.PorcDesc AS FLOAT) AS PorcDesc, "\
                        "CAST(VentaLinea.PorcDescG AS FLOAT) AS PorcDescG, "\
                        "CAST(VentaLinea.Precio AS FLOAT) AS Precio, "\
                        "CAST(VentaLinea.PrecioImp AS FLOAT) AS PrecioImp, "\
                        "Documento.Comentario, "\
                        "Documento.IdTipoDocumento, "\
                        "Venta.IdMoneda, "\
                        "VentaLinea.IdArticulo, "\
                        "VentaLinea.Descripcion, "\
                        "Vendedor.Nombre, "\
                        "CAST(VentaLinea.Cantidad AS FLOAT) AS Cantidad, "\
                        "Cliente.Numero, "\
                        "Cliente.Nombre, "\
                        "FORMAT(Cliente.FechaNacimiento, 'dd-MM') AS FechaN, "\
                        "FormaPago.Descripcion, "\
                        "CAST(VentaLinea.PorcImp1 AS FLOAT) AS PorcImp1, "\
                        "CAST(VentaLinea.PorcImp2 AS FLOAT) AS PorcImp2, "\
                        "Vendedor.Numero, "\
                        "Documento.Comentario, "\
                        "FormaPago.IdFormaPago "\
                        "FROM Documento "\
                        "INNER JOIN VentaLinea ON VentaLinea.IdDocumento = Documento.IdDocumento "\
                        "INNER JOIN Venta ON Venta.IdDocumento = Documento.IdDocumento "\
                        "INNER JOIN Historico ON Historico.NumeroDoc = Documento.NumeroDoc "\
                        "INNER JOIN PersonaEmpresa AS Cliente ON Cliente.IdPersonaEmpresa = Venta.IdCliente "\
                        "INNER JOIN PersonaEmpresa AS Vendedor ON Vendedor.IdPersonaEmpresa = Venta.IdVendedor "\
                        "INNER JOIN MovCaja ON MovCaja.IdDocumento = Venta.IdDocumento "\
                        "INNER JOIN FormaPago ON MovCaja.IdFormaPago = FormaPago.IdFormaPago "\
                        "WHERE CONVERT(varchar, Documento.Fecha, 112) = ? "\
                        "AND CONVERT(varchar, Documento.Fecha, 112) = ? "\
                        "ORDER BY Documento.IdDeposito asc;"


query_tarj =            "SELECT "\
                        "Documento.IdDeposito, "\
                        "Venta.IdCaja, "\
                        "Documento.NumeroDoc, "\
                        "FORMAT(Documento.Fecha, 'yyyy-MM-dd') AS FechaDoc, "\
                        "CAST(Venta.Total AS FLOAT) AS Total, "\
                        "CAST(VentaLinea.PorcDescG AS FLOAT) AS PorcDescG, "\
                        "CAST(VentaLinea.PorcDesc AS FLOAT) AS PorcDesc, "\
                        "Documento.IdTipoDocumento, "\
                        "PersonaEmpresa.Numero, "\
                        "PersonaEmpresa.Nombre, "\
                        "FormaPago.Descripcion, "\
                        "TarjetaTrans.NroTarjeta, "\
                        "TarjetaTrans.Autoriz, "\
                        "TarjetaTrans.NroBIN, "\
                        "TarjetaTrans.Cuota, "\
                        "FormaPago.IdFormaPago "\
                        "FROM Documento "\
                        "INNER JOIN Venta ON Documento.IdDocumento = Venta.IdDocumento "\
                        "INNER JOIN MovCaja ON MovCaja.IdDocumento = Venta.IdDocumento "\
                        "INNER JOIN FormaPago ON MovCaja.IdFormaPago = FormaPago.IdFormaPago "\
                        "INNER JOIN Promocion ON Venta.IdPromocion = Promocion.IdPromocion "\
                        "INNER JOIN PersonaEmpresa ON PersonaEmpresa.IdPersonaEmpresa = Venta.IdCliente "\
                        "INNER JOIN VentaLinea ON VentaLinea.IdDocumento = Documento.IdDocumento "\
                        "INNER JOIN TarjetaTrans ON Documento.IdDocumento = TarjetaTrans.IdDocumento "\
                        "WHERE CONVERT(varchar, Documento.Fecha, 112) = ? "\
                        "AND TarjetaTrans.Cuota > 6;"\


query_pres = "SELECT "\
                        "Documento.IdDeposito, "\
                        "Documento.NumeroDoc, "\
                        "FORMAT(Documento.Fecha, 'yyyy-MM-dd') AS FechaDoc, "\
                        "Documento.IdTipoDocumento, "\
                        "CAST(MovCaja.Monto AS FLOAT) AS Monto, "\
                        "FormaPago.Descripcion, "\
                        "FormaPago.IdFormaPago "\
                        "FROM MovCaja "\
                        "INNER JOIN Documento ON MovCaja.IdDocumento = Documento.IdDocumento "\
                        "INNER JOIN FormaPago ON MovCaja.IdFormaPago = FormaPago.IdFormaPago "\
                        "WHERE CONVERT(varchar, Documento.Fecha, 112) >= ? "\
                        "AND CONVERT(varchar, Documento.Fecha, 112) <= ? "\
                        "AND Documento.IdTipoDocumento IN ('VCO', 'DCO') "\
                        "AND FormaPago.IdFormaPago = ? ;"\


query_pres_manuales =   "SELECT "\
                        "Documento.IdDeposito, "\
                        "Documento.NumeroDoc, "\
                        "FORMAT(Documento.Fecha, 'yyyy-MM-dd') AS FechaDoc, "\
                        "Documento.IdTipoDocumento, "\
                        "CAST(MovCaja.Monto AS FLOAT) AS Monto, "\
                        "FormaPago.Descripcion, "\
                        "FormaPago.IdFormaPago "\
                        "FROM MovCaja "\
                        "INNER JOIN Documento ON MovCaja.IdDocumento = Documento.IdDocumento "\
                        "INNER JOIN FormaPago ON MovCaja.IdFormaPago = FormaPago.IdFormaPago "\
                        "WHERE CONVERT(varchar, Documento.Fecha, 112) >= ? "\
                        "AND CONVERT(varchar, Documento.Fecha, 112) <= ? "\
                        "AND Documento.IdTipoDocumento IN ('VCO', 'DCO') "\
                        "AND FormaPago.IdFormaPago IN (?,?,?,?,?,?,?,?,?) ;"\


query_cierre_tarj =     "SELECT "\
                        "Documento.IdDeposito, "\
                        "Venta.IdCaja, "\
                        "Documento.NumeroDoc, "\
                        "FORMAT(Documento.Fecha, 'yyyy-MM-dd') AS FechaDoc, "\
                        "CAST(MovCaja.Monto AS FLOAT) AS Monto, "\
                        "Documento.IdTipoDocumento, "\
                        "FormaPago.Descripcion, "\
                        "FormaPago.IdFPTipo, "\
                        "TarjetaTrans.NroTarjeta, "\
                        "TarjetaTrans.Autoriz, "\
                        "TarjetaTrans.NroBIN, "\
                        "TarjetaTrans.Cuota, "\
                        "TarjetaTrans.FechaCierre, "\
                        "Documento.Hora "\
                        "FROM TarjetaTrans "\
                        "INNER JOIN Documento ON TarjetaTrans.IdDocumento = Documento.IdDocumento "\
                        "INNER JOIN Venta ON TarjetaTrans.IdDocumento = Venta.IdDocumento "\
                        "INNER JOIN MovCaja ON TarjetaTrans.IdDocumento = MovCaja.IdDocumento "\
                        "INNER JOIN FormaPago ON MovCaja.IdFormaPago = FormaPago.IdFormaPago "\
                        "WHERE CONVERT(varchar, Documento.Fecha, 112) = ? ;"\

    
query_promo =           "SELECT "\
                        "Documento.IdDeposito, "\
                        "Venta.IdCaja, "\
                        "Documento.NumeroDoc, "\
                        "FORMAT(Documento.Fecha, 'yyyy-MM-dd') AS FechaDoc, "\
                        "Documento.IdTipoDocumento, "\
                        "CAST(MovCaja.Monto AS FLOAT) AS Monto, "\
                        "FormaPago.Descripcion, "\
                        "TarjetaTrans.NroTarjeta, "\
                        "TarjetaTrans.Autoriz, "\
                        "TarjetaTrans.NroBIN, "\
                        "TarjetaTrans.Cuota, "\
                        "Promocion.Descripcion, "\
                        "Documento.Comentario "\
                        "FROM TarjetaTrans "\
                        "INNER JOIN Documento ON TarjetaTrans.IdDocumento = Documento.IdDocumento "\
                        "INNER JOIN MovCaja ON TarjetaTrans.IdDocumento = MovCaja.IdDocumento "\
                        "INNER JOIN Venta ON TarjetaTrans.IdDocumento = Venta.IdDocumento "\
                        "INNER JOIN Promocion ON Venta.IdPromocion = Promocion.IdPromocion "\
                        "INNER JOIN FormaPago ON MovCaja.IdFormaPago = FormaPago.IdFormaPago "\
                        "WHERE CONVERT(varchar, Documento.Fecha, 112) >= ? "\
                        "AND CONVERT(varchar, Documento.Fecha, 112) <= ? "\
                        "AND Promocion.IdPromocion = ? ;"
