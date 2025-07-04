metros1 = float(input('Uma distância em metros: '))
print(
    f'A medida {metros1:.1f}m corresponde a:\n'
      f'{metros1/1000:.3f}km\n'
      f'{metros1/100:.2f}hm\n'
      f'{metros1/10:.1f}dam\n'
      f'{metros1*10:.0f}dm\n'
      f'{metros1*100:.0f}cm\n'
      f'{metros1*1000:.0f}mm'
    )
