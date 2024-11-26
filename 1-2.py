inp = 'BCAADDBCBDxCCADDBxBBBBDABCDCBCxCDCADAxDBDCBBDDBxADBBCABDCxBACCAxCCBACxCBDADAxCACABBDBADCACBDACACBCDDxDBADBCCxBCAAxDAAAAxBDDCBCxACDAxBCBDBBBCBDDDCACABxACACDBDDDBBACCxDDBCDBACBDBADBDCBCDDBCAABBACDACDAxCABCACBDBACACACBDADDAxxAABDCCBBAxDCDACDDCCADCCxDxABDBBCDACAADBDCBACxBBCBBAxCBBDDCADCDBCAxCxADACDDDDBBCCABDBDDDDBADxBBACBBADCADAABDBBABAACxDCDCxDBABBBDDBDABAADxDBBCACBBCCBCABBCAAACABxCCCBBCACDDDBCABDBCCCDABCADBADADxxADBxACDACBBxDDDBCxCDBDCADBCDBADCDBCDBxCADABBAxCACCBCADBDBDCBAAABBDDDCDxBAABCCxBxBBDxADBxBBDAxDABDAABDADCCCCDDCABBDBCABBADADDAAxCDCBADBBACxDCCADCxDDBAxBxCDBxxDCDDABCABDADBABxAABDDCDxADDDBBxAABDBBDCBAABAxDBABCBxCDxDxCDAxDDBACDAADBDxCBCAADBAACABDBDDADDDCCBxBDABxADBDCDDBDxBAxCBCCADCxBCBBDCAxDDCCADABBDCDAxBAACCBxBBCBxBDDBDAxDDxCBxDABADAADDCABDBBABABBBBCxBBBCACDCxCCAxDCADDxBABABDCADCBDCACxBxCBABCBxBBCxCABAADADBDCABxCCBCBBxDBADxDCDDBDBCABDxAACBAxBBCBABDDAACxACABBBDDxCDxBDCACCACDCBDDxDxCBxCxBxAAxBDDAAADDDCxBABCCDBBxDDCADBBDxCxxAADBCCCACDDBAxCCxAADDBBBBBCCAxDADAxDDACDACADBABCxAAABxxDDDxACBDAxCCBDCCDCAxABCBxACACCxxADBCCDDCCDCxxBDDDADAxCACxxBABCCCDBADACxBCDDCxxCADCxBBACAADBDDDDCDCBCDDCCDCABADCDCBDCABABDDxDDDxDDDABCxADBADCCDACxBxAADCxBCDBBBxCACBBDDCDBDCCxDCxBBBABACADABxDAACxBCCDDCCDxCDBACDxDCCBCBDCBCxBBAABCCCACCCCBACAABCBDBACxDCCDCDxBDxxAxBAxBDDACxDBBAxCACDxxDCBxDDDBBABBDCDBDCCCCADCBCxBBxBADCAACxCACBCADxxxxxCBCDBAAACCDABDDCCCCBACxBDBBABBDCBxDAADDCDDADDABDBBDDxACBxCBCCACCABBDxCABDCCDACABBCDADCDDDCxCDDDCxBBBBxBxDCDACCCDBBCDACDxADxCAxBCACCADxCABCBBCADCBDCDDCCxBDABABABAxABBABBBCBACDxBDDBCCCBACCADBAAxABABDADADBCBDCBACDDxCADBCDBDCBACDBxACBDAADCACxxAxDACADxCBxCCCDDAADxCDABBxACBAxDCADCABDCDBBxxDCxABBADxDCBACCBBCBCAADCDBCCDABCxCxxBBDAAxCBAAxDBCxAABxDCBBBxADCDDxBDCDADCBACBBBDDDBDBABDCACBDAADADACADDBCCCCBADCDBCDAACxAAADBBBAAAxBCDAxDxDABDDACBCxDxAxDCADCCCDADxDAABDADCxCCAADBxBAxCBBABDDCDBCADADAACCDDADAxADDDAxCBABDBCxBDCBAxBCABAADDCDCABCAAxABxDBBBBCDABDxCDxBDADBBCxDDDCCCDAxCCBDDAxCBxxCACBDBBCCDDAxxABDCCAADBCBACDCBADCAAABDBBCADBDDBACDADCCAxxDCCDDABBCCAxxDACBCBDABDBxCDCxCBAAABCBDCxABDCxB'

vals = {'A': 0, 'x': 0, 'B': 1, 'C': 3, 'D': 5}
totalPotions = 0

for i in range(0, len(inp), 2):
    fir, sec = inp[i], inp[i+1]
    totalPotions += vals[fir]
    totalPotions += vals[sec]
    if fir != 'x' and sec != 'x':
        totalPotions += 2

print(totalPotions, len(inp))