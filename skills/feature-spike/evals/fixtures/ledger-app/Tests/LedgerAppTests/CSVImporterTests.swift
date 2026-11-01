import Testing

@testable import LedgerApp

@Test func importsWellFormedRows() throws {
    let csv = "date,amount_cents,category,memo\n2026-10-03,1250,Groceries,Market\n2026-10-04,300,Transit,Bus"
    let transactions = try CSVImporter().parse(csv)
    #expect(transactions.map(\.amountCents) == [1_250, 300])
    #expect(transactions.map(\.category) == ["Groceries", "Transit"])
}

@Test func reportsTheMalformedRow() {
    let csv = "date,amount_cents,category,memo\n2026-10-03,twelve,Groceries,Market"
    #expect(throws: CSVImportError.malformedRow(2)) {
        try CSVImporter().parse(csv)
    }
}
