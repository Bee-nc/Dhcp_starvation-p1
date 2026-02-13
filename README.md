# Práctica P1 - DHCP Starvation
** Viensy Pérez 
**Matrícula:** 20241203  

## Descripción
## Descripción
Repositorio individual para la práctica P1: ataque DHCP Starvation en la asignatura Seguridad de Redes.  
Este ataque consiste en enviar múltiples solicitudes DHCP falsas con direcciones MAC aleatorias para agotar el pool de direcciones del servidor legítimo, impidiendo que los clientes obtengan una IP válida.

## Archivos incluidos
- `Viensy_20241203_Starvation_P1.py` → Script en Python para el ataque.
- `Viensy_20241203_Informe_P1.pdf` → Informe con explicación, capturas y resultados.
- `capturas/` → Evidencias gráficas del ataque.
- `Viensy_20241203_P1.zip` → Paquete final con todos los entregables.

## Direccionamiento IP
El laboratorio utiliza direccionamiento basado en la matrícula:
- Red: `192.168.120.0/24`
- Router (R1): `192.168.120.1`
- Kali: `192.168.120.99`
- VPCS (PC1): `192.168.120.5` (asignado por DHCP)

## Ejecución del script
En Kali:
```bash
python3 Viensy_20241203_Starvation_P1.py
