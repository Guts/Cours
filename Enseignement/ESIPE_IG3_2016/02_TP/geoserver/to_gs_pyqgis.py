from qgis.utils import iface
from qgis.core import QgsMapLayerRegistry, QgsRasterLayer

# sample from QGIS layer general properties
# contextualWMSLegend=0&crs=EPSG:4326&dpiMode=7&featureCount=10&format=image/png&layers=ESIPE_IG3:Camera_WGS84&password=geoserver&styles=&url=http://localhost:8080/geoserver/ows?version%3D1.3.0%26&username=admin

# URI components
uri_separator = "&"
uri_url = "url=http://localhost:8080/geoserver/ows?contextualWMSLegend=0&featureCount=10"
uri_username = "username=admin"
uri_password = "password=geoserver"
uri_format = "format=image/png"
uri_layers = "layers=ESIPE_IG3:Camera_WGS84"
uri_crs = "crs=EPSG:4326"
uri_service = "SERVICE=WMS"
uri_version = "version%3D1.3.0%26"
uri_request = "REQUEST=GetMap"
uri_dpi="dpiMode=7"
uri_style = "style="

# URI construction
wms_url_complete = uri_url + uri_separator.join((uri_service,
                                                 uri_version,
                                                 uri_request,
                                                 uri_username,
                                                 uri_password,
                                                 uri_format,
                                                 uri_layers,
                                                 uri_crs,
                                                 uri_style,
                                                 uri_dpi))
                                      
print(wms_url_complete)

rlayer = QgsRasterLayer(wms_url_complete, 'norther', 'wms')

if rlayer.isValid():
    pass
else:
    print(rlayer.error().message())

QgsMapLayerRegistry.instance().addMapLayer(rlayer)


### With QgsDatSourceURI

uri = QgsDataSourceURI()
uri.setParam('url', 'http://localhost:8080/geoserver/wms?')
uri.setParam("layers", "ESIPE_IG3:Camera_WGS84")
uri.setParam("service", "WMS")
uri.setParam("request", "GetMap")
uri.setParam("version", "version%3D1.3.0%26")
uri_layer = QgsRasterLayer(str(uri.encodedUri()), 'WMSlayer', 'wms')

if uri_layer.isValid():
    pass
else:
    print(uri_layer.error().message())
