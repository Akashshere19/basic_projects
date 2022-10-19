from pyModbusTCP.client import ModbusClient
c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)
c = ModbusClient()
c.host("localhost")
c.port(502)
c.unit_id(1)
c.open()
regs = c.read_holding_registers(0, 2)
if regs:
    print(regs)
else:
    print("read error")
if c.write_multiple_registers(10, [44,55]):
    print("write ok")
else:
    print("write error")    