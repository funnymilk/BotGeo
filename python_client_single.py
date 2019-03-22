from zeep import Client, Settings
import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

my_login = 'cTdaIrOlTDVptr'
my_password = 'xRQbKXQhUx20'
#barcode = 'RA644000001RU'
headerArr = {}

settings = Settings(strict=False, xml_huge_tree=True, extra_http_headers=headerArr)
client = Client('https://tracking.russianpost.ru/rtm34?wsdl',
                settings=settings)
def get_loc(barcode):
    requestData = {
        'OperationHistoryRequest': {
            'Barcode': barcode,
            'MessageType': 0,
            'Language': 'RUS',
        },
        'AuthorizationHeader': {
            'login': my_login,
            'password': my_password,
        }

    }
    res = client.service.getOperationHistory(**requestData)

    sFile = open ("otv.txt",'w')
    sFile.write(str(res))
    sFile.close()
    test = ''
    for rec in res:
        test = test + str(
            rec.OperationParameters.OperDate) + ', ' + rec.AddressParameters.OperationAddress.Description + ', ' + rec.OperationParameters.OperAttr.Name + '\n'
    return test



