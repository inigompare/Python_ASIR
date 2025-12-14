pago_mensual = 10
total_pagado = 0

print(f"Mes 1: {pago_mensual} euros")
total_pagado = pago_mensual

for mes in range(2, 21):
    pago_mensual = pago_mensual * 2
    total_pagado += pago_mensual
    print(f"Mes {mes}: {pago_mensual} euros")

print(f"El total pagado después de 20 meses es: {total_pagado} euros")
